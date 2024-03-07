import discord
from discord import app_commands
from discord.ext import commands

from .cmnds.endecoding import Cmnds_EncodeDecode


class EncodeDecode(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="b64encode", description="Encode to Base64")
    @app_commands.describe(text="Text to process")
    async def b64encode(self, interaction: discord.Interaction, text: str):
        await Cmnds_EncodeDecode.b64encode(interaction=interaction, text=text)

    @app_commands.command(name="b64decode", description="Decode from Base64")
    @app_commands.describe(text="Text to process")
    async def b64decode(self, interaction: discord.Interaction, text: str):
        await Cmnds_EncodeDecode.b64decode(interaction=interaction, text=text)

    @app_commands.command(name="md5", description="Get MD5 Hash")
    @app_commands.describe(text="Text to process")
    async def md5(self, interaction: discord.Interaction, text: str):
        await Cmnds_EncodeDecode.md5(interaction=interaction, text=text)

    @app_commands.command(name="sha1", description="Get SHA1 Hash")
    @app_commands.describe(text="Text to process")
    async def sha1(self, interaction: discord.Interaction, text: str):
        await Cmnds_EncodeDecode.sha1(interaction=interaction, text=text)

    @app_commands.command(name="sha224", description="Get SHA224 Hash")
    @app_commands.describe(text="Text to process")
    async def sha224(self, interaction: discord.Interaction, text: str):
        await Cmnds_EncodeDecode.sha224(interaction=interaction, text=text)

    @app_commands.command(name="sha512", description="Get SHA512 Hash")
    @app_commands.describe(text="Text to process")
    async def sha512(self, interaction: discord.Interaction, text: str):
        await Cmnds_EncodeDecode.sha512(interaction=interaction, text=text)

    @app_commands.command(name="leet", description="Convert text to L33T format")
    @app_commands.describe(text="Text to process")
    async def leet(self, interaction: discord.Interaction, text: str):
        await Cmnds_EncodeDecode.leet(interaction=interaction, text=text)


async def setup(client: commands.Bot):
    await client.add_cog(EncodeDecode(client))
