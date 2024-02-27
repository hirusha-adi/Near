import discord
import aiohttp
import random
import requests
from bs4 import BeautifulSoup
from json import loads as loadjsonstring

from near.utils import embeds
from near.utils import errors


class Cmnds_Fun:

    @errors.handle_error
    async def inspire(interaction: discord.Interaction):
        r = requests.get("https://zenquotes.io/api/random")
        json_data = loadjsonstring(r.text)
        quote = json_data[0]["q"] + " - " + json_data[0]["a"]

        embed = embeds.Common(
            interaction=interaction,
            title="Inspirational isn't it?",
            description=str(quote),
            thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png",
        )
        return await interaction.response.send_message(embed=embed)

    @errors.handle_error
    async def bored(interaction: discord.Interaction):
        r = requests.get("http://www.boredapi.com/api/activity/")
        data = r.json()

        embed = embeds.Common(
            interaction=interaction,
            title="Heres an Activity for you",
            description=f"**{data['activity']}**",
            thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png",
        )
        embed.add_field(name="Type", value=f"{data['type']}", inline=True)
        embed.add_field(
            name="Participants", value=f"{data['participants']}", inline=True
        )
        embed.add_field(
            name="Accessibility", value=f"{data['accessibility']}", inline=True
        )
        return await interaction.response.send_message(embed=embed)

    @errors.handle_error
    async def meme(interaction: discord.Interaction):
        url = "https://www.memedroid.com/memes/tag/programming"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        divs = soup.find_all("div", class_="item-aux-container")
        imgs = []
        for div in divs:
            img = div.find("img")["src"]
            if img.startswith("http") and img.endswith("jpeg"):
                imgs.append(img)
        meme = random.choice(imgs)

        embed = embeds.Common(
            interaction=interaction,
            title="a Meme",
        )
        embed.set_image(url=str(meme))
        return await interaction.response.send_message(embed=embed)

    @errors.handle_error
    async def dadjoke(interaction: discord.Interaction):
        headers = {"Accept": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://icanhazdadjoke.com", headers=headers
            ) as req:
                r = await req.json()

        embed = embeds.Common(
            interaction=interaction,
            title="a Dad Joke",
            description=f"{r['joke']}",
            thumbnail="https://cdn.discordapp.com/attachments/881007500588089404/912620134974251018/senior-caucasian-man-wearing-business-260nw-1860664027.png",
        )
        return await interaction.response.send_message(embed=embed)

    @errors.handle_error
    async def dadjoke(interaction: discord.Interaction):
        headers = {"Accept": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://icanhazdadjoke.com", headers=headers
            ) as req:
                r = await req.json()

        embed = embeds.Common(
            interaction=interaction,
            title="a Dad Joke",
            description=f"{r['joke']}",
            thumbnail="https://cdn.discordapp.com/attachments/881007500588089404/912620134974251018/senior-caucasian-man-wearing-business-260nw-1860664027.png",
        )
        return await interaction.response.send_message(embed=embed)

    @errors.handle_error
    async def joke(interaction: discord.Interaction):
        r = requests.get("https://v2.jokeapi.dev/joke/Any")
        c = r.json()

        try:
            jokeit = c["joke"]
        except:
            jokeit = c["setup"]

        embed = embeds.Common(
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

    @errors.handle_error
    async def wyr(interaction: discord.Interaction):
        r = requests.get("https://www.conversationstarters.com/wyrqlist.php").text
        soup = BeautifulSoup(r, "html.parser")
        qa = soup.find(id="qa").text
        qor = soup.find(id="qor").text
        qb = soup.find(id="qb").text

        embed = embeds.Common(
            interaction=interaction,
            title="Would You Rather",
            description=f"{qa}\n{qor}\n{qb}",
            thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg",
        )
        return await interaction.response.send_message(embed=embed)

    @errors.handle_error
    async def advice(interaction: discord.Interaction):
        r = requests.get("https://www.conversationstarters.com/wyrqlist.php").text
        soup = BeautifulSoup(r, "html.parser")
        qa = soup.find(id="qa").text
        qor = soup.find(id="qor").text
        qb = soup.find(id="qb").text

        embed = embeds.Common(
            interaction=interaction,
            title="Would You Rather",
            description=f"{qa}\n{qor}\n{qb}",
            thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg",
        )
        return await interaction.response.send_message(embed=embed)
