import asyncio
import os
from collections import defaultdict
from pathlib import Path
import typing as t

import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get

from near.utils import youtube

from bot.music import Queue

class Music(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.music_queues = defaultdict(Queue)
        
        # TODO: Add filters
        # -----------------------
        # self.equalizer_presets = {
        #     "female": "equalizer=f=100:t=q:w=1:g=-10,f=500:t=q:w=1:g=5,f=2000:t=q:w=1:g=-10,f=5000:t=q:w=1:g=10",
        #     "male": "equalizer=f=100:t=q:w=1:g=10,f=500:t=q:w=1:g=-5,f=2000:t=q:w=1:g=5,f=5000:t=q:w=1:g=-5",
        #     "bass_boost": "equalizer=f=60:t=q:w=1:g=15,f=170:t=q:w=1:g=10,f=300:t=q:w=1:g=5",
        #     "robotic": "equalizer=f=100:t=q:w=1:g=-5,f=400:t=q:w=1:g=-10,f=1200:t=q:w=1:g=5,f=3000:t=q:w=1:g=-10",
        #     "treble_boost": "equalizer=f=1000:t=q:w=1:g=15,f=5000:t=q:w=1:g=10,f=12000:t=q:w=1:g=10",
        # }
        # -----------------------

    async def ensure_connected_to_vc(self, interaction: discord.Interaction) -> t.Optional[discord.VoiceClient]:
        guild = interaction.guild
        user_voice = interaction.user.voice

        # Check if the user is in a voice channel
        if not user_voice or not user_voice.channel:
            await interaction.response.send_message("You must be in a voice channel to use this command!")
            return None
        
        user_channel = user_voice.channel
        bot_voice: t.Optional[discord.VoiceClient] = guild.voice_client

        # If bot is not in a voice channel, join the user's channel
        if not bot_voice:
            await user_channel.connect()
            return guild.voice_client
        elif bot_voice.channel != user_channel:
            await interaction.response.send_message(f"I'm already connected to `{bot_voice.channel.name}`. Please join my channel or disconnect me first!", )
            return None
        
        return bot_voice
    
    @app_commands.command(name="join", description="Joins a voice channel")
    @app_commands.describe(channel="Mention a voice channel (optional)")
    @app_commands.describe(force="Force join even if already in a voice channel")
    async def join(self, interaction: discord.Interaction, channel: discord.VoiceChannel = None, force: bool = False):
        # If no channel is provided, use the user's current voice channel
        if not channel:
            if interaction.user.voice and interaction.user.voice.channel:
                channel = interaction.user.voice.channel
            else:
                await interaction.response.send_message("You need to be in a voice channel or mention one!")
                return

        # Check if bot is already connected
        # Skip if force is True
        if not force:
            if interaction.guild.voice_client:
                await interaction.response.send_message("I'm already in a voice channel!")
                return

        # Check bot permissions
        permissions = channel.permissions_for(interaction.guild.me)
        if not permissions.connect:
            await interaction.response.send_message("I don't have permission to connect to that voice channel!")
            return
        if not permissions.speak:
            await interaction.response.send_message("I don't have permission to speak in that voice channel!")
            return

        # Connect to the channel
        await channel.connect()
        await interaction.response.send_message(f"Joined {channel.name}!")

    @app_commands.command(name="leave", description="Leaves the voice channel")
    async def leave(self, interaction: discord.Interaction):
        _guild = interaction.guild
        voice: discord.VoiceClient = get(self.client.voice_clients, guild=_guild)
        queue = self.music_queues.get(_guild)

        if voice:
            if voice.is_connected():
                voice.stop()
                if queue:
                    queue.clear()
                await voice.disconnect()
                await interaction.response.send_message("Leaving voice channel.")
        else:
            await interaction.response.send_message("I'm not connected to a voice channel.")

    @app_commands.command(name="play", description="Plays a song from YouTube by URL or search query")
    async def play(self, interaction: discord.Interaction, url: str):
        voice_client = await self.ensure_connected_to_vc(interaction)
        if not voice_client:
            return
        
        await interaction.response.send_message(f"Processing `{url}`...")

        # await interaction.response.defer()

        guild: discord.Guild = interaction.guild
        music_queue = self.music_queues[guild]

        # this will always return a voice client
        # since the bot is connected to a voice channel at this point
        voice: discord.VoiceClient = get(self.client.voice_clients, guild=guild)
        channel: discord.VoiceChannel = interaction.user.voice.channel

        video_id, video_filename = youtube.download_video(url)

        if not video_filename or not Path(video_filename).exists():
            await interaction.followup.send("Failed to download the audio.")
            return

        music_queue.append(video_filename)

        if not voice.is_playing():
            await self.play_next_song(voice, guild)
        else:
            await interaction.followup.send("Added to queue.")
        
        voice.play(discord.FFmpegPCMAudio(video_filename))

    async def inactivity_disconnect(self, guild: discord.Guild):
        """Disconnects the bot after 5 minutes of inactivity."""
        await asyncio.sleep(300)  # Wait for 5 minutes
        voice = get(self.client.voice_clients, guild=guild)
        if voice and not voice.is_playing():
            await voice.disconnect()

    async def play_next_song(self, voice: discord.VoiceClient, guild: discord.Guild):
        """Plays the next song in the queue and handles disconnection if inactive."""
        if self.music_queues[guild]:
            next_song = self.music_queues[guild].pop(0)  # Get next song from queue
            
            def after_playing(error):
                if error:
                    print(f"Error playing audio: {error}")
                asyncio.run_coroutine_threadsafe(self.play_next_song(voice, guild), self.client.loop)

            voice.play(discord.FFmpegPCMAudio(next_song), after=after_playing)
        else:
            # Start the inactivity timer when the queue is empty
            asyncio.create_task(self.inactivity_disconnect(guild))

    # Volume control (FFmpeg volume filter)
    async def set_volume(self, voice: discord.VoiceClient, volume: float):
        """Adjusts the volume of the currently playing song."""
        if volume < 0.1 or volume > 2:
            return "Volume must be between 0.1 and 2!"
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume
        return f"Volume set to {volume * 100}%"

    @app_commands.command(name="volume", description="Sets the volume of the music.")
    async def volume(self, interaction: discord.Interaction, volume: float):
        """Adjust the volume of the bot's playback."""
        voice: t.Optional[discord.VoiceClient] = interaction.guild.voice_client
        if not voice or not voice.is_playing():
            await interaction.response.send_message("No song is currently playing!")
            return

        result = await self.set_volume(voice, volume)
        await interaction.response.send_message(result)

    @app_commands.command(name="stop", description="Stops music and clears the queue")
    @app_commands.checks.has_permissions(ban_members=True)
    async def stop(self, interaction: discord.Interaction):
        guild: discord.Guild = interaction.guild
        music_queue = self.music_queues[guild]
        voice: discord.VoiceClient = get(self.client.voice_clients, guild=guild)

        if not voice:
            await interaction.response.send_message("I'm not connected to a voice channel.")
            return

        if voice.is_playing() or voice.is_paused():
            voice.stop()

        music_queue.clear()
        await voice.disconnect()

        await interaction.response.send_message("Music has been stopped, and the queue has been cleared.")

    @app_commands.command(name="skip", description="Skip the current song")
    async def skip(self, interaction: discord.Interaction):
        guild: discord.Guild = interaction.guild
        music_queue = self.music_queues[guild]
        voice: discord.VoiceClient = get(self.client.voice_clients, guild=guild)

        if not voice:
            await interaction.response.send_message("I'm not connected to a voice channel.")
            return

        if not music_queue:
            await interaction.response.send_message("The queue is empty, no song to skip.")
            return

        # Stop the current song
        if voice.is_playing() or voice.is_paused():
            voice.stop()

        # Play the next song
        await self.play_next_song(voice, guild)

        await interaction.response.send_message("Skipped to the next song!")

    @app_commands.command(name="queue", description="Shows the current song queue")
    async def queue(self, interaction: discord.Interaction):
        guild: discord.Guild = interaction.guild
        music_queue = self.music_queues[guild]
        if not music_queue:
            await interaction.response.send_message("The queue is currently empty.")
            return

        queue_list = "\n".join([f"{index + 1}. {Path(song).stem}" for index, song in enumerate(music_queue)])
        await interaction.response.send_message(f"**Music Queue:**\n```\n{queue_list}\n```")

async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
