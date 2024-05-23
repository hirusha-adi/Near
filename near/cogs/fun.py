import random
from json import loads as loadjsonstring

import aiohttp
import discord
import requests
from bs4 import BeautifulSoup
from discord import app_commands
from discord.ext import commands

from near.utils import embeds


class Fun(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="inspire", description="Get an inspirational quote")
    async def inspire(self, interaction: discord.Interaction):
        try:
            r = requests.get("https://zenquotes.io/api/random")
            json_data = loadjsonstring(r.text)
            quote = json_data[0]['q'] + " - " + json_data[0]['a']

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Inspirational isn't it?",
                description=str(quote),
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


    @app_commands.command(name="meme", description="Get a random meme")
    async def meme(self, interaction: discord.Interaction):
        try:
            url = 'https://www.memedroid.com/memes/tag/programming'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            divs = soup.find_all('div', class_='item-aux-container')
            imgs = []
            for div in divs:
                img = div.find('img')['src']
                if img.startswith('http') and img.endswith('jpeg'):
                    imgs.append(img)
            meme = random.choice(imgs)
            
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="a Meme",
            )
            embed.set_image(url=str(meme))
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="dadjoke", description="Get a random dad joke")
    async def dadjoke(self, interaction: discord.Interaction):
        try:
            headers = {
                "Accept": "application/json"
            }

            async with aiohttp.ClientSession() as session:
                async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
                    r = await req.json()
            
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="a Dad Joke",
                description=f"{r['joke']}",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879303282139463680/480px-Happy_smiley_face.png"
            )

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="wyr", description="Would You Rather...?")
    async def wyr(self, interaction: discord.Interaction):
        try:
            r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text

            soup = BeautifulSoup(r, 'html.parser')
            qa = soup.find(id='qa').text
            qor = soup.find(id='qor').text
            qb = soup.find(id='qb').text
            
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Would You Rather",
                description=f"{qa}\n{qor}\n{qb}",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="advice", description="Get advice for your life")
    async def advice(self, interaction: discord.Interaction):
        try:
            r = requests.get("https://api.adviceslip.com/advice").json()
            c = r['slip']['advice']

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="an Advice",
                description=str(c),
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/880034306720956456/download_1.jfif"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="joke2", description="Get a Joke, but from Another API")
    async def joke(self, interaction: discord.Interaction):
        try:
            r = requests.get("https://some-random-api.ml/joke").json()

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="a Joke",
                description=f"{r['joke']}",
                thumbnail="https://media.discordapp.net/attachments/877796755234783273/880742956552822794/mr-bean-avatar-character-cartoon-rowan-atkinson-png-image-33.png?width=454&height=584"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(Fun(client))
