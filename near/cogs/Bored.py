import aiohttp
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from near.database import get_embeds


class Bored(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=get_embeds.PleaseWait.AUTHOR_NAME, icon_url=get_embeds.PleaseWait.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)

    @commands.command()
    async def bored(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('http://www.boredapi.com/api/activity/')
            data = r.json()
            what_to_do_when_bored = f'[+] Activity: {data["activity"]} \n[+] Type: {data["type"]} \n[+] Participants: {data["participants"]} \n[+] Key: {data["key"]} \n[+] Accessibility: {data["accessibility"]} '
            embed = discord.Embed(title="Heres an Activity for you",
                                  description="If you are bored, consider doing this", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.add_field(name="Activity",
                            value=f"{data['activity']}", inline=False)
            embed.add_field(name="Type", value=f"{data['type']}", inline=False)
            embed.add_field(name="Participants",
                            value=f"{data['participants']}", inline=False)
            embed.add_field(name="Key", value=f"{data['key']}", inline=False)
            embed.add_field(name="Accessibility",
                            value=f"{data['accessibility']}", inline=False)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/884694742716268554/unnamed.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

def setup(client: commands.Bot):
    client.add_cog(Bored(client))
