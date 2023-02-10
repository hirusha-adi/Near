import asyncio
import re

import discord
import wavelink
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds

from .checks import in_same_channel, player_connected, voice_connected
from .player import DisPlayer


class Music(commands.Cog, name="Music", description="Play any music easily!"):
    """Music commands"""

    def __init__(self, bot):
        self.bot = bot
        self.URL_REG = re.compile(r"https?://(?:www\.)?.+")

        if not hasattr(self.bot, "wavelink"):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        for node in self.bot.lava_nodes:
            try:
                await self.bot.wavelink.initiate_node(**node)
            except Exception as e:
                print(e)

        for guild in self.bot.guilds:
            if guild.me.voice:
                player: DisPlayer = self.bot.wavelink.get_player(
                    guild.id, cls=DisPlayer
                )
                try:
                    await player.connect(guild.me.voice.channel.id)
                    print(
                        f"Connected to existing voice -> {guild.me.voice.channel.id}")
                except Exception as e:
                    print(e)

    @app_commands.command(name="connect", description="Connect to Voice Channel")
    @voice_connected()
    async def connect_(self, interaction: discord.Interaction):
        """Connect the player"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if player.is_connected:
            if not player.bound_channel:
                player.bound_channel = interaction.channel

            if player.channel_id == interaction.user.voice.channel.id:
                return await interaction.response.send_message(
                    "Player is already connected to your voice channel."
                )

            return await interaction.response.send_message(
                f"Player is connected to a different voice channel. Can' join this."
            )

        channel = interaction.user.voice.channel
        self.bot.voice_users[interaction.user.id] = channel.id

        msg = await interaction.response.send_message(f"Connecting to **`{channel.name}`**")
        await player.connect(channel.id)
        player.bound_channel = interaction.channel
        await msg.edit(
            content=f"Connected to **`{channel.name}`** and bounded to {interaction.channel.mention}"
        )

    @app_commands.command(name="disconnect", description="Disconnect bot from Voice Channel")
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def disconnect_(self, interaction: discord.Interaction):
        """Destroy the player"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)
        await player.destroy()

    @app_commands.command(name="play", description="Play the song")
    @app_commands.describe(query="Song name or URL")
    @voice_connected()
    async def play_(self,  interaction: discord.Interaction, query: str):
        """Play or add song to queue"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if not player.is_connected:
            # BUG
            await interaction.invoke(self.connect_)

        if interaction.channel != player.bound_channel and player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )
        player.bound_channel = interaction.channel

        msg = await interaction.response.send_message(f"Searching for `{query}` :mag_right:")
        query = query.strip("<>")
        if not self.URL_REG.match(query):
            query = f"ytsearch:{query}"

        tracks = await self.bot.wavelink.get_tracks(query)

        if not tracks:
            return await msg.edit(content="Could not find any song with that query.")

        if isinstance(tracks, wavelink.TrackPlaylist):
            for track in tracks.tracks:
                await player.queue.put(track)

            msg.edit(
                content=f'Added the playlist **{tracks.data["playlistInfo"]["name"]}** with **{len(tracks.tracks)}** songs to the queue.'
            )
        else:
            await player.queue.put(tracks[0])

            await msg.edit(content=f"Added **{str(tracks[0])}** to the queue.")

        if not player.is_playing:
            await player.do_next()

    @app_commands.command(name="skip", description="Skip the currently playing song")
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def skip(self, interaction: discord.Interaction):
        """Skip currently playing song"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if interaction.channel != player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        current_loop = player.loop
        player.loop = "NONE"

        await player.stop()

        if current_loop != "CURRENT":
            player.loop = current_loop

    @app_commands.command(name="pause", description="Pause the music")
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def pause(self, interaction: discord.Interaction):
        """Pause the player"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if interaction.channel != player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if player.is_playing:
            if player.is_paused:
                return await interaction.response.send_message("Player is already paused.")

            await player.set_pause(pause=True)
            return await interaction.response.send_message("Player is now paused.")

        await interaction.response.send_message("Player is not playing anything.")

    @app_commands.command(name="resume", description="Resume the music")
    @player_connected()
    @voice_connected()
    @in_same_channel()
    async def resume(self, interaction: discord.Interaction):
        """Resume the player"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if interaction.channel != player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if player.is_playing:
            if not player.is_paused:
                return await interaction.response.send_message("Player is not paused.")

            await player.set_pause(pause=False)
            return await interaction.response.send_message("Player is now resumed.")

        await interaction.response.send_message("Player is not playing anything.")

    @app_commands.command(name="seek", description="Skip the given seconds of the playing song")
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def seek(self, interaction: discord.Interaction, seconds: int, reverse: bool = False):
        """Seek the player backward or forward"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if interaction.channel != player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if player.is_playing:
            if not player.is_paused:
                if not reverse:
                    new_position = player.position + (seconds * 1000)
                    if new_position > player.current.length:
                        new_position = player.current.length
                else:
                    new_position = player.position - (seconds * 1000)
                    if new_position < 0:
                        new_position = 0

                await player.seek(new_position)
                return await interaction.response.send_message(f"Player has been seeked {seconds} seconds.")

            return await interaction.response.send_message(
                "Player is paused. Resume the player to use this command."
            )

        await interaction.response.send_message("Player is not playing anything.")

    @app_commands.command(name="volume", description="Change the volume of the song")
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def volume(self, interaction: discord.Interaction, vol: int, forced=False):
        """Set volume"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if interaction.channel != player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if vol < 0:
            return await interaction.response.send_message("Volume can't be less than 0")

        if vol > 100 and not forced:
            return await interaction.response.send_message("Volume can't greater than 100")

        await player.set_volume(vol)

    @app_commands.command(name="loop", description="Play music in a loop")
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def loop(self, interaction: discord.Interaction, type: str = None):
        """Set loop to `NONE`, `CURRENT` or `PLAYLIST`"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if interaction.channel != player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        valid_types = ["NONE", "CURRENT", "PLAYLIST"]

        if not type:
            current_loop = player.loop
            if valid_types.index(current_loop) >= 2:
                type = "NONE"
            else:
                type = valid_types[valid_types.index(current_loop) + 1]

            queue = player.queue._queue
            if type == "PLAYLIST" and len(queue) < 1:
                type = "NONE"

        else:
            type = type.upper()

        if type not in valid_types:
            return await interaction.response.send_message("Loop type must be `NONE`, `CURRENT` or `PLAYLIST`.")

        if len(player.queue._queue) < 1 and type == "PLAYLIST":
            return await interaction.response.send_message(
                "There must be 2 songs in the queue in order to use the PLAYLIST loop"
            )

        if not player.is_playing:
            return await interaction.response.send_message("Player is not playing any track. Can't loop")

        player.loop = type

        await interaction.response.send_message(f"Player is now looping `{type}`")

    @app_commands.command(name="nowplaying", description="Show the song which is being played right now")
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def nowplaying(self, interaction: discord.Interaction):
        """What's playing now?"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if interaction.channel != player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        if not player.current:
            return await interaction.response.send_message("Nothing is playing.")

        await player.invoke_player()

    @app_commands.command(name="queue", description="Diplay the songs waiting to be played")
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def queue(self, interaction: discord.Interaction):
        """Player's current queue"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if interaction.channel != player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        queue = player.queue._queue
        if len(queue) < 1:
            return await interaction.response.send_message("Nothing is in the queue.")

        embed = discord.Embed(color=get_embeds.Common.COLOR)
        embed.set_author(
            name="Queue", icon_url="https://cdn.shahriyar.dev/list.png")

        tracks = ""
        if player.loop == "CURRENT":
            next_song = f"Next > [{player.current.title}]({player.current.uri}) \n\n"
        else:
            next_song = ""

        if next_song:
            tracks += next_song

        for index, track in enumerate(queue):
            tracks += f"{index + 1}. [{track.title}]({track.uri}) \n"

        embed.description = tracks

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="equalizer", description="Maybe tune the song to your liking?")
    @voice_connected()
    @player_connected()
    @in_same_channel()
    async def equalizer(self, interaction: discord.Interaction):
        """Set equalizer"""
        player: DisPlayer = self.bot.wavelink.get_player(
            interaction.guild.id, cls=DisPlayer)

        if interaction.channel != player.bound_channel:
            return await interaction.response.send_message(
                f"Player is bounded to {player.bound_channel.mention}", delete_after=5
            )

        eqs = {
            "1️⃣": ["Flat", wavelink.eqs.Equalizer.flat()],
            "2️⃣": ["Boost", wavelink.eqs.Equalizer.boost()],
            "3️⃣": ["Metal", wavelink.eqs.Equalizer.metal()],
            "4️⃣": ["Piano", wavelink.eqs.Equalizer.piano()],
        }

        embed = discord.Embed(title="Select Equalizer")
        embed.description = f"Current Eq - **{player.eq.name}**\n\n1. Flat \n2. Boost\n3. Metal\n4. Piano"
        embed.set_thumbnail(url="https://cdn.shahriyar.dev/equalizer.png")

        msg = await interaction.response.send_message(embed=embed)

        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("4️⃣")

        def check(reaction, user):
            return (
                reaction.message.id == msg.id
                and user.id == interaction.user.id
                and reaction.emoji in ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]
            )

        while True:
            try:
                reaction, user = await self.bot.wait_for(
                    "reaction_add", timeout=60.0, check=check
                )
            except:
                await msg.delete()
                break

            selected_eq = eqs[reaction.emoji][1]
            await player.set_equalizer(selected_eq)

            embed.description = (
                f"Current Eq - **{eqs[reaction.emoji][0]}**\n\n"
                "1. Flat \n2. Boost\n3. Metal\n4. Piano"
            )

            await msg.edit(embed=embed)
