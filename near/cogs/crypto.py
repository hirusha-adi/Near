import discord
import requests
from bs4 import BeautifulSoup
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds
from near.utils import errors

class CryptoCommand:
    
    @errors.handle_error
    async def btc(interaction: discord.Interaction):
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        embed = discord.Embed(title="Bitcoin", color=get_embeds.Common.COLOR)
        embed.set_author(name=f"Near", icon_url=f"https://user-images.githubusercontent.com/36286877/208341567-6706e40f-03b5-4e29-836c-760708f2e619.png")
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
        embed.add_field(name="USD", value=f"{usd}$", inline=False)
        embed.add_field(name="EUR", value=f"{eur}€", inline=False)
        embed.set_footer(text=f"Requested by {interaction.user.name}")
        return await interaction.response.send_message(embed=embed)
    
    @errors.handle_error
    async def btc(interaction: discord.Interaction):
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        embed = discord.Embed(title="Bitcoin", color=get_embeds.Common.COLOR)
        embed.set_author(name=f"Near", icon_url=f"https://user-images.githubusercontent.com/36286877/208341567-6706e40f-03b5-4e29-836c-760708f2e619.png")
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
        embed.add_field(name="USD", value=f"{usd}$", inline=False)
        embed.add_field(name="EUR", value=f"{eur}€", inline=False)
        embed.set_footer(text=f"Requested by {interaction.user.name}")
        return await interaction.response.send_message(embed=embed)
 

class Crypto(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="btc", description="Get the current Bitcoin Rates")
    async def btc(self, interaction: discord.Interaction):
        await CryptoCommand.btc(interaction=interaction)

    @app_commands.command(name="eth", description="Get the current Etherium Rates")
    async def eth(self, interaction: discord.Interaction):
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        
        embed = discord.Embed(title="Ethereum", color=get_embeds.Common.COLOR)
        embed.set_author(name=f"Near", icon_url=f"{self.client.user.avatar.url}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png")
        embed.add_field(name="USD", value=f"{usd}$", inline=False)
        embed.add_field(name="EUR", value=f"{eur}€", inline=False)
        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="xmr", description="Get the current Monero Rates")
    async def xmr(self, interaction: discord.Interaction):
            r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
            NegroPuket = r.json()

            eur = NegroPuket['EUR']
            usd = NegroPuket['USD']

            embed = discord.Embed(title="Monero", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"Near", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073564308979597312/monero-xmr-logo.png")
            embed.add_field(name="USD", value=f"{usd}", inline=False)
            embed.add_field(name="EUR", value=f"{eur}", inline=True)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

    @app_commands.command(name="doge", description="Get the current Doge Coin Rates")
    async def doge(self, interaction: discord.Interaction):
            r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
            NegroPuketDOGE = r.json()

            eur = NegroPuketDOGE['EUR']
            usd = NegroPuketDOGE['USD']

            embed = discord.Embed(title="Doge Coin", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"Near", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073564685061861388/Dogecoin_Logo.png")
            embed.add_field(name="USD", value=f"{usd}", inline=False)
            embed.add_field(name="EUR", value=f"{eur}", inline=True)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

    @app_commands.command(name="xrp", description="Get the current XRP Rates")
    async def xrp(self, interaction: discord.Interaction):
            r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
            kekistan = r.json()

            eur = kekistan['EUR']
            usd = kekistan['USD']

            embed = discord.Embed(title="Ripple", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"Near", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073565079410319430/free-ripple-coin-icon-2208-thumb.png")
            embed.add_field(name="USD", value=f"{usd}", inline=False)
            embed.add_field(name="EUR", value=f"{eur}", inline=True)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

        

    @app_commands.command(name="rvn", description="Get the current Raven Coin Rates")
    async def rvn(self, interaction: discord.Interaction):
            c = requests.get('https://www.coindesk.com/price/ravencoin/')
            soup = BeautifulSoup(c.content, "html.parser")
            raven_coin_value = soup.find_all("span", {"class": "currency-pricestyles__Price-sc-1rux8hj-0 jxzQXk"})[0].text

            change_percentage = soup.find_all("h6", {"class": "typography__StyledTypography-owin6q-0 hZxwDe"})[0].text

            embed = discord.Embed(title="Ravencoin", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"Near", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073566855593197600/ravencoin-rvn-logo.png")
            embed.add_field(name="USD", value=f"{raven_coin_value}", inline=False)
            embed.add_field(name="24 Hour Change %", value=f"{change_percentage}", inline=False)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

        


async def setup(client: commands.Bot):
    await client.add_cog(Crypto(client))
