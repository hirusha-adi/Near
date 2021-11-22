import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from near.database import get_embeds


class Crypto(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=get_embeds.PleaseWait.AUTHOR_NAME, icon_url=get_embeds.PleaseWait.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)

    @commands.command(aliases=["btc"])
    async def bitcoin(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
            r = r.json()

            usd = r['USD']
            eur = r['EUR']

            embed = discord.Embed(
                title="Bitcoin", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
            embed.add_field(name="USD", value=f"{usd}$", inline=False)
            embed.add_field(name="EUR", value=f"{eur}€", inline=False)
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

    @commands.command()
    async def eth(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
            r = r.json()

            usd = r['USD']
            eur = r['EUR']

            embed = discord.Embed(
                title="Ethereum", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png")
            embed.add_field(name="USD", value=f"{usd}$", inline=False)
            embed.add_field(name="EUR", value=f"{eur}€", inline=False)
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

    @commands.command()
    async def hastebin(self, ctx, *, message):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.post(
                "https://hastebin.com/documents", data=message).json()

            try:
                embed = discord.Embed(
                    title="Hastebin", color=get_embeds.Common.COLOR)
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar_url}")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png")
                embed.add_field(
                    name="Link", value=f"https://hastebin.com/{r['key']}", inline=False)
                embed.add_field(
                    name=f"Text by {ctx.author.name}", value=f"{message}", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

            except:
                embed = discord.Embed(
                    title="Hastebin", color=get_embeds.Common.COLOR)
                embed.set_author(
                    name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar_url}")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png")
                embed.add_field(
                    name="Link", value=f"https://hastebin.com/{r['key']}", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(
                name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command()
    async def xmr(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                "https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
            NegroPuket = r.json()

            eur = NegroPuket['EUR']
            usd = NegroPuket['USD']

            embed = discord.Embed(title="XMR", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879739662837633074/monero-logo-png-transparent.png")
            embed.add_field(name="USD", value=f"{usd}", inline=False)
            embed.add_field(name="EUR", value=f"{eur}", inline=True)
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

    @commands.command()
    async def doge(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                "https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
            NegroPuketDOGE = r.json()

            eur = NegroPuketDOGE['EUR']
            usd = NegroPuketDOGE['USD']

            embed = discord.Embed(
                title="Doge Coin", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879741979183968286/Dogecoin_Logo.png")
            embed.add_field(name="USD", value=f"{usd}", inline=False)
            embed.add_field(name="EUR", value=f"{eur}", inline=True)
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

    @commands.command()
    async def xrp(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(
                "https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
            kekistan = r.json()

            eur = kekistan['EUR']
            usd = kekistan['USD']

            embed = discord.Embed(
                title="Ripple", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879741815237017680/52.png")
            embed.add_field(name="USD", value=f"{usd}", inline=False)
            embed.add_field(name="EUR", value=f"{eur}", inline=True)
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

    @commands.command()
    async def rvn(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            c = requests.get(
                'https://www.coingecko.com/en/coins/ravencoin/usd')
            soup = BeautifulSoup(c.content, "html.parser")
            raven_coin_value = soup.find_all("span", {
                "class": "no-wrap", "data-coin-symbol": "rvn", "data-target": "price.price"})[0].text

            one_day_trading_vol = soup.find_all(
                "span", {"class": "no-wrap", "data-target": "price.price", "data-no-decimal": "false"})[0].text

            circulating_supply = str(soup.find_all("span", {
                "class": "tw-text-gray-900 dark:tw-text-white tw-float-right tw-font-medium tw-mr-1"})[0].text).strip()

            total_supply = str(soup.find_all("span", {
                "class": "tw-text-gray-900 dark:tw-text-white tw-float-right tw-font-medium tw-mr-1"})[1].text).strip()

            embed = discord.Embed(
                title="Ravencoin", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/881007500588089404/912395666578374686/ravencoin-rvn-logo.png")
            embed.add_field(
                name="USD", value=f"{raven_coin_value}", inline=False)
            embed.add_field(name="24 Hour Trading Vol",
                            value=f"{one_day_trading_vol}", inline=False)
            embed.add_field(
                name="Circulating Supply", value=f"{circulating_supply}", inline=False)
            embed.add_field(name="Total Supply",
                            value=f"{total_supply}", inline=False)
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
    client.add_cog(Crypto(client))
