import random
from json import loads as loadjsonstring

import aiohttp
import discord
import requests
from bs4 import BeautifulSoup
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

        try:
            r = requests.get("https://api.adviceslip.com/advice").json()
            c = r["slip"]["advice"]

            embed = discord.Embed(
                title="an Adive", description=str(c), color=get_embeds.Common.COLOR
            )
            embed.set_author(
                name=f"{self.client.user.name}",
                icon_url=f"{self.client.user.avatar.url}",
            )
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/880034306720956456/download_1.jfif"
            )
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(
                title=get_embeds.ErrorEmbeds.TITLE,
                description=get_embeds.ErrorEmbeds.DESCRIPTION,
                color=get_embeds.ErrorEmbeds.COLOR,
            )
            embed3.set_author(
                name=f"{self.client.user.name}",
                icon_url=f"{self.client.user.avatar.url}",
            )
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False
            )
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="joke2", description="Get a Joke, but from Another API")
    async def joke2(self, interaction: discord.Interaction):

        try:
            r = requests.get("https://some-random-api.ml/joke").json()

            embed = discord.Embed(
                title="a Joke",
                description=f"{r['joke']}",
                color=get_embeds.Common.COLOR,
            )
            embed.set_author(
                name=f"{self.client.user.name}",
                icon_url=f"{self.client.user.avatar.url}",
            )
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/877796755234783273/880742956552822794/mr-bean-avatar-character-cartoon-rowan-atkinson-png-image-33.png?width=454&height=584"
            )
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(
                title=get_embeds.ErrorEmbeds.TITLE,
                description=get_embeds.ErrorEmbeds.DESCRIPTION,
                color=get_embeds.ErrorEmbeds.COLOR,
            )
            embed3.set_author(
                name=f"{self.client.user.name}",
                icon_url=f"{self.client.user.avatar.url}",
            )
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False
            )
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)


async def setup(client: commands.Bot):
    await client.add_cog(Fun(client))
