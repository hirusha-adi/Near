import aiohttp

import discord
from discord import app_commands
from discord.ext import commands
from bs4 import BeautifulSoup
from loguru import logger

from near.utils import embeds


class Crypto(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="btc", description="Get the current Bitcoin Rates")
    async def btc(self, interaction: discord.Interaction):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR') as response:
                    r = await response.json()

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Bitcoin",
                thumbnail="crypto_btc",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="eth", description="Get the current Etherium Rates")
    async def eth(self, interaction: discord.Interaction):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR') as response:
                    r = await response.json()

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Ethereum",
                thumbnail="crypto_eth",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="xmr", description="Get the current Monero Rates")
    async def xmr(self, interaction: discord.Interaction):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR') as response:
                    r = await response.json()

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Monero",
                thumbnail="crypto_xmr",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="doge", description="Get the current Doge Coin Rates")
    async def doge(self, interaction: discord.Interaction):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR') as response:
                    r = await response.json()

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Doge Coin",
                thumbnail="crypto_doge",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="xrp", description="Get the current XRP Rates")
    async def xrp(self, interaction: discord.Interaction):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR') as response:
                    r = await response.json()

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Ripple",
                thumbnail="crypto_xrp",
            )
            embed.add_field(name="USD", value=f"{r['USD']}$", inline=False)
            embed.add_field(name="EUR", value=f"{r['EUR']}€", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="rvn", description="Get the current Raven Coin Rates")
    async def rvn(self, interaction: discord.Interaction):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://www.coindesk.com/price/ravencoin/') as response:
                    soup = BeautifulSoup(response.content, "html.parser")
                    raven_coin_value = soup.find_all("span", {"class": "currency-pricestyles__Price-sc-1rux8hj-0 jxzQXk"})[0].text
                    change_percentage = soup.find_all("h6", {"class": "typography__StyledTypography-owin6q-0 hZxwDe"})[0].text

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Ravencoin",
                thumbnail="crypto_rvn",
            )
            embed.add_field(name="USD", value=f"{raven_coin_value}", inline=False)
            embed.add_field(name="24 Hour Change %", value=f"{change_percentage}", inline=False)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(Crypto(client))
