import discord
from discord import app_commands
from discord.ext import commands

from .cmnds.fun import Cmnds_Fun


class Fun(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="inspire", description="Get an inspirational quote")
    async def inspire(self, interaction: discord.Interaction):
        await Cmnds_Fun.inspire(interaction=interaction)

    @app_commands.command(name="bored", description="Bored? What to do now?")
    async def bored(self, interaction: discord.Interaction):
        await Cmnds_Fun.bored(interaction=interaction)

    @app_commands.command(name="meme", description="Get a random meme")
    async def meme(self, interaction: discord.Interaction):
        await Cmnds_Fun.meme(interaction=interaction)

    @app_commands.command(name="dadjoke", description="Get a random dad joke")
    async def dadjoke(self, interaction: discord.Interaction):
        await Cmnds_Fun.dadjoke(interaction=interaction)

    @app_commands.command(name="joke", description="Get a random joke")
    async def joke(self, interaction: discord.Interaction):
        await Cmnds_Fun.joke(interaction=interaction)

    @app_commands.command(name="wyr", description="Would You Rather...?")
    async def wyr(self, interaction: discord.Interaction):
        await Cmnds_Fun.wyr(interaction=interaction)

    @app_commands.command(name="advice", description="Get advice for your life")
    async def advice(self, interaction: discord.Interaction):
        await Cmnds_Fun.advice(interaction=interaction)


    @app_commands.command(name="joke2", description="Get a Joke, but from Another API")
    async def joke2(self, interaction: discord.Interaction):
        await Cmnds_Fun.joke2(interaction=interaction)

async def setup(client: commands.Bot):
    await client.add_cog(Fun(client))
