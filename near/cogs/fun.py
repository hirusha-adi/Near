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
        self.headers_json = {"Accept": "application/json"}

    @app_commands.command(name="inspire", description="Get an inspirational quote")
    async def inspire(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://zenquotes.io/api/random") as response:
                    json_data = await response.json()
                    quote = json_data[0]["q"] + " - " + json_data[0]["a"]

                    embed = embeds.Common(
                        client=self.client,
                        interaction=interaction,
                        title="Inspirational isn't it?",
                        description=str(quote),
                        thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png",
                    )
                    await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="bored", description="Bored? What to do now?")
    async def bored(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("http://www.boredapi.com/api/activity/") as response:
                    data = await response.json()

                    embed = embeds.Common(
                        client=self.client,
                        interaction=interaction,
                        title="Here's an Activity for you",
                        description=f"**{data['activity']}**",
                        thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png",
                    )
                    embed.add_field(name="Type", value=f"{data['type']}", inline=True)
                    embed.add_field(name="Participants", value=f"{data['participants']}", inline=True)
                    embed.add_field(name="Accessibility", value=f"{data['accessibility']}", inline=True)
                    await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="meme", description="Get a random meme")
    async def meme(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://www.memedroid.com/memes/tag/programming") as response:
                    html_content = await response.text()

                    soup = BeautifulSoup(html_content, "html.parser")
                    divs = soup.find_all("div", class_="item-aux-container")
                    imgs = [div.find("img")["src"] for div in divs if div.find("img")["src"].startswith("http") and div.find("img")["src"].endswith("jpeg")]
                    
                    meme_url = random.choice(imgs)

                    embed = embeds.Common(
                        client=self.client,
                        interaction=interaction,
                        title="A Programming Meme",
                    )
                    embed.set_image(url=str(meme_url))
                    await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="dadjoke", description="Get a random dad joke")
    async def dadjoke(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://icanhazdadjoke.com", headers=self.headers_json) as response:
                    r = await response.json()

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="a Dad Joke",
                description=f"{r['joke']}",
                thumbnail="https://cdn.discordapp.com/attachments/881007500588089404/912620134974251018/senior-caucasian-man-wearing-business-260nw-1860664027.png",
            )
            return await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="joke", description="Get a random joke")
    async def joke(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://v2.jokeapi.dev/joke/Any") as r:
                    c = await r.json()

            try:
                jokeit = c["joke"]
            except:
                jokeit = c["setup"]

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title=":grin: a Joke",
                description=f"{r['joke']}",
            )
            embed.add_field(name="Joke", value=f"{jokeit}", inline=False)
            embed.add_field(
                name="Information",
                value=f"Category: {c['category']} \nType: {c['type']} \nNSFW: {c['flags']['nsfw']} \nReligious: {c['flags']['religious']} \nPolitical: {c['flags']['political']} \nRacist: {c['flags']['racist']} \nSexist: {c['flags']['sexist']} \nExplicit: {c['flags']['explicit']} \nLanguage: {c['lang']}",
                inline=True,
            )
            return await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="wyr", description="Would You Rather...?")
    async def wyr(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://www.conversationstarters.com/wyrqlist.php", headers=self.headers_json) as response:
                    html_content = await response.text()

            soup = BeautifulSoup(html_content, "html.parser")
            qa = soup.find(id="qa").text
            qor = soup.find(id="qor").text
            qb = soup.find(id="qb").text

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Would You Rather",
                description=f"{qa}\n{qor}\n{qb}",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg",
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="advice", description="Get advice for your life")
    async def advice(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.adviceslip.com/advice", headers=self.headers_json) as response:
                    data = await response.json()

            advice_text = data["slip"]["advice"]

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="An Advice",
                description=f"{advice_text}",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/880034306720956456/download_1.jfif",
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="joke2", description="Get a Joke, but from Another API")
    async def joke2(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://some-random-api.ml/joke") as response:
                    data = await response.json()

            joke_text = data["joke"]

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="A Joke",
                description=f"{joke_text}",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg",
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(Fun(client))
