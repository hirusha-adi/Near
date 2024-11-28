import aiohttp
import json
import random

import discord
from discord import app_commands
from discord.ext import commands
from bs4 import BeautifulSoup
from loguru import logger

from near.utils import embeds
from near.utils import log


class Fun(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="inspire", description="Get an inspirational quote")
    async def inspire(self, interaction: discord.Interaction):
        await log.log_command_history(command="/inspire", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://zenquotes.io/api/random") as response:
                    json_data = await response.json()
                    quote = json_data[0]['q'] + " - " + json_data[0]['a']

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Inspirational isn't it?",
                description=str(quote),
                thumbnail="fun_inspire"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


    @app_commands.command(name="meme", description="Get a random meme")
    async def meme(self, interaction: discord.Interaction):
        await log.log_command_history(command="/meme", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://www.memedroid.com/memes/tag/programming') as response:
                    html_content = await response.text()
                    soup = BeautifulSoup(html_content, 'html.parser')
                    divs = soup.find_all('div', class_='item-aux-container')
                    imgs = []
                    for div in divs:
                        img = div.find('img')['src']
                        if img.startswith('http') and img.endswith('jpeg'):
                            imgs.append(img)
                    meme = random.choice(imgs)
            
            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="a Meme",
            )
            embed.set_image(url=str(meme))
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="dadjoke", description="Get a random dad joke")
    async def dadjoke(self, interaction: discord.Interaction):
        await log.log_command_history(command="/dadjoke", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://icanhazdadjoke.com", headers={"Accept": "application/json"}) as req:
                    r = await req.json()
            
            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="a Dad Joke",
                description=f"{r['joke']}",
                thumbnail="fun_dadjoke"
            )

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="wyr", description="Would You Rather...?")
    async def wyr(self, interaction: discord.Interaction):
        await log.log_command_history(command="/wyr", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://www.conversationstarters.com/wyrqlist.php') as response:
                    html_content = await response.text()
                    soup = BeautifulSoup(html_content, 'html.parser')
                    qa = soup.find(id='qa').text
                    qor = soup.find(id='qor').text
                    qb = soup.find(id='qb').text
            
            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Would You Rather",
                description=f"{qa}\n{qor}\n{qb}",
                thumbnail="fun_wyr"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="advice", description="Get advice for your life")
    async def advice(self, interaction: discord.Interaction):
        await log.log_command_history(command="/advice", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.adviceslip.com/advice") as response:
                    data_str = await response.text()
                    data_json = json.loads(data_str)
                    c = data_json['slip']['advice']

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="an Advice",
                description=c,
                thumbnail="fun_advice"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="joke", description="Get a Joke, but from Another API")
    async def joke(self, interaction: discord.Interaction):
        await log.log_command_history(command="/joke", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            url = "https://some-random-api.ml/joke"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    json_txt = await response.text()
                    json_data = json.loads(json_txt)

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="a Joke",
                description=f"{json_data['joke']}",
                thumbnail="fun_joke"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(Fun(client))
