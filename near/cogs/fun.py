import random
from json import loads as loadjsonstring

import aiohttp
import discord
import requests
from bs4 import BeautifulSoup
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds
from near.utils import input_sanitization, errors


class Fun(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="inspire", description="Get an inspirational quote")
    async def inspire(self, interaction: discord.Interaction):
        try:
            r = requests.get("https://zenquotes.io/api/random")
            json_data = loadjsonstring(r.text)
            quote = json_data[0]['q'] + " - " + json_data[0]['a']

            embed = discord.Embed(title="Inspirational isn't it?", description=str(quote), color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png")
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="bored", description="Bored? What to do now?")
    async def bored(self, interaction: discord.Interaction):

        try:
            r = requests.get('http://www.boredapi.com/api/activity/')
            data = r.json()
            embed = discord.Embed(title="Heres an Activity for you", description=f"**{data['activity']}**", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.add_field(name="Type", value=f"{data['type']}", inline=True)
            embed.add_field(name="Participants", value=f"{data['participants']}", inline=True)
            embed.add_field(name="Accessibility", value=f"{data['accessibility']}", inline=True)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/884694742716268554/unnamed.png")
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

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

            embed = discord.Embed(title="a Meme", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_image(url=str(meme))

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="dadjoke", description="Get a random dad joke")
    async def dadjoke(self, interaction: discord.Interaction):

        try:
            headers = {
                "Accept": "application/json"
            }

            # Get data from the API with the above mentioned headers
            async with aiohttp.ClientSession()as session:
                async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
                    r = await req.json()

            embed = discord.Embed(title="a Dad Joke", description=f"{r['joke']}", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/881007500588089404/912620134974251018/senior-caucasian-man-wearing-business-260nw-1860664027.png")
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="joke", description="Get a random joke")
    async def joke(self, interaction: discord.Interaction):

        try:
            r = requests.get("https://v2.jokeapi.dev/joke/Any")
            c = r.json()

            try:
                jokeit = c["joke"]
            except:
                jokeit = c["setup"]

            embed = discord.Embed(title=":grin: a Joke", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879303282139463680/480px-Happy_smiley_face.png")
            embed.add_field(name="Joke", value=f"{jokeit}", inline=False)
            embed.add_field(name="Information", value=f"Category: {c['category']} \nType: {c['type']} \nNSFW: {c['flags']['nsfw']} \nReligious: {c['flags']['religious']} \nPolitical: {c['flags']['political']} \nRacist: {c['flags']['racist']} \nSexist: {c['flags']['sexist']} \nExplicit: {c['flags']['explicit']} \nLanguage: {c['lang']}", inline=True)
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="wyr", description="Would You Rather...?")
    async def wyr(self, interaction: discord.Interaction):

        try:
            r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text

            soup = BeautifulSoup(r, 'html.parser')
            qa = soup.find(id='qa').text
            qor = soup.find(id='qor').text
            qb = soup.find(id='qb').text
            embed = discord.Embed(title="Would You Rather", description=f"{qa}\n{qor}\n{qb}", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg")
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="advice", description="Get advice for your life")
    async def advice(self, interaction: discord.Interaction):

        try:
            r = requests.get("https://api.adviceslip.com/advice").json()
            c = r['slip']['advice']

            embed = discord.Embed(title="an Adive", description=str(c), color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880034306720956456/download_1.jfif")
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="joke2", description="Get a Joke, but from Another API")
    async def joke2(self, interaction: discord.Interaction):

        try:
            r = requests.get("https://some-random-api.ml/joke").json()

            embed = discord.Embed(title="a Joke", description=f"{r['joke']}", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880742956552822794/mr-bean-avatar-character-cartoon-rowan-atkinson-png-image-33.png?width=454&height=584")
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)


async def setup(client: commands.Bot):
    await client.add_cog(Fun(client))
