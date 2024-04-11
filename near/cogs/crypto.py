import aiohttp
from bs4 import BeautifulSoup

import discord
from discord import app_commands
from discord.ext import commands

from near.utils import embeds


class Crypto(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
    @app_commands.command(name="btc", description="Get the current Bitcoin Rates")
    async def btc(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR') as response:
                    r = await response.json()

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Bitcoin",
                thumbnail="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)
            
    @app_commands.command(name="eth", description="Get the current Etherium Rates")
    async def eth(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR') as response:
                    r = await response.json()

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Ethereum",
                thumbnail="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="xmr", description="Get the current Monero Rates")
    async def xmr(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR') as response:
                    r = await response.json()
            
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Monero",
                thumbnail="https://cdn.discordapp.com/attachments/940889393974104084/1073564308979597312/monero-xmr-logo.png",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="doge", description="Get the current Doge Coin Rates")
    async def doge(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR') as response:
                    r = await response.json()
            
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Doge Coin",
            thumbnail="https://cdn.discordapp.com/attachments/940889393974104084/1073564685061861388/Dogecoin_Logo.png",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="xrp", description="Get the current XRP Rates")
    async def xrp(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR') as response:
                    r = await response.json()
            
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Ripple",
                thumbnail="https://cdn.discordapp.com/attachments/940889393974104084/1073565079410319430/free-ripple-coin-icon-2208-thumb.png",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="rvn", description="Get the current Raven Coin Rates")
    async def rvn(self, interaction: discord.Interaction):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://www.coindesk.com/price/ravencoin/') as response:
                    soup = BeautifulSoup(response.content, "html.parser")
                    raven_coin_value = soup.find_all("span", {"class": "currency-pricestyles__Price-sc-1rux8hj-0 jxzQXk"})[0].text
                    change_percentage = soup.find_all("h6", {"class": "typography__StyledTypography-owin6q-0 hZxwDe"})[0].text
            
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Ravencoin",
                thumbnail="https://cdn.discordapp.com/attachments/940889393974104084/1073566855593197600/ravencoin-rvn-logo.png",
            )
            embed.add_field(name="USD", value=f"{raven_coin_value}", inline=False)
            embed.add_field(name="24 Hour Change %", value=f"{change_percentage}", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(Crypto(client))
