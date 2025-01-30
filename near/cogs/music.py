import asyncio
import os
from collections import defaultdict
from pathlib import Path

import discord
import yt_dlp
from discord.ext import commands
from discord import app_commands
from discord.utils import get

from bot import config
from bot.music import Queue, Song, SongRequestError

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.music_queues = defaultdict(Queue)

    @app_commands.command(name="play", description="Plays a song from YouTube by URL or search query")
    async def play(self, interaction: discord.Interaction, url: str):
        await interaction.response.defer()
        guild = interaction.guild
        music_queue = self.music_queues[guild]
        voice = get(self.bot.voice_clients, guild=guild)

        try:
            channel = interaction.user.voice.channel
        except AttributeError:
            await interaction.followup.send("You're not connected to a voice channel.")
            return

        if voice and voice.channel != channel:
            await interaction.followup.send("You're not in my voice channel.")
            return

        if not url.startswith("https://"):
            url = f"ytsearch1:{url}"

        try:
            song = Song(url, author=interaction.user)
        except SongRequestError as e:
            await interaction.followup.send(e.args[0])
            return

        music_queue.append(song)
        await interaction.followup.send(f'Queued song: {song.title}')

        if voice is None or not voice.is_connected():
            await channel.connect()

        await self.play_all_songs(guild)

    @app_commands.command(name="stop", description="Stops music and clears the queue")
    @app_commands.checks.has_permissions(ban_members=True)
    async def stop(self, interaction: discord.Interaction):
        guild = interaction.guild
        voice = get(self.bot.voice_clients, guild=guild)
        queue = self.music_queues.get(guild)

        if voice and voice.is_connected():
            voice.stop()
            queue.clear()
            await voice.disconnect()
            await interaction.response.send_message("Stopping playback and disconnecting.")
        else:
            await interaction.response.send_message("I'm not playing anything right now.")

    @app_commands.command(name="skip", description="Vote to skip the current song")
    async def skip(self, interaction: discord.Interaction):
        guild = interaction.guild
        voice = get(self.bot.voice_clients, guild=guild)
        queue = self.music_queues.get(guild)

        if not voice or not voice.is_playing():
            await interaction.response.send_message("I'm not playing a song right now.")
            return

        if interaction.user in queue.skip_voters:
            await interaction.response.send_message("You've already voted to skip this song.")
            return

        required_votes = round(len(interaction.user.voice.channel.members) / 2)
        queue.add_skip_vote(interaction.user)

        if len(queue.skip_voters) >= required_votes:
            await interaction.response.send_message("Skipping song after successful vote.")
            voice.stop()
        else:
            await interaction.response.send_message(f"You voted to skip this song. {required_votes - len(queue.skip_voters)} more votes required.")

    @app_commands.command(name="queue", description="Shows the current song queue")
    async def queue(self, interaction: discord.Interaction):
        queue = self.music_queues.get(interaction.guild)
        if not queue:
            await interaction.response.send_message("The queue is empty.")
            return

        queue_text = "\n".join([f"{i+1}. {song.title}" for i, song in enumerate(queue)])
        embed = discord.Embed(title="Music Queue", description=queue_text, color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)

    async def play_all_songs(self, guild: discord.Guild):
        queue = self.music_queues.get(guild)
        while queue:
            song = queue.next_song()
            await self.play_song(guild, song)
        await self.inactivity_disconnect(guild)

    async def play_song(self, guild: discord.Guild, song: Song):
        audio_path = os.path.join(".", "audio", f"{guild.id}.mp3")
        voice = get(self.bot.voice_clients, guild=guild)

        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "outtmpl": audio_path,
        }

        Path("./audio").mkdir(parents=True, exist_ok=True)
        try:
            os.remove(audio_path)
        except OSError:
            pass

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song.url])

        voice.play(discord.FFmpegPCMAudio(audio_path))

    async def inactivity_disconnect(self, guild: discord.Guild):
        voice = get(self.bot.voice_clients, guild=guild)
        await asyncio.sleep(300)
        if voice and not voice.is_playing():
            await voice.disconnect()

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.tree.add_command(self.play)
        self.bot.tree.add_command(self.stop)
        self.bot.tree.add_command(self.skip)
        self.bot.tree.add_command(self.queue)
        print("Music cog loaded")

async def setup(bot):
    await bot.add_cog(Music(bot))
