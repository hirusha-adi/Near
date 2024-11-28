import aiohttp

import discord
from discord import app_commands
from discord.ext import commands
from bs4 import BeautifulSoup

from near.utils import embeds
from near.utils import log


class Crypto(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="btc", description="Get the current Bitcoin Rates")
    async def btc(self, interaction: discord.Interaction):
        await log.log_command_history(command="/crypto", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
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
        await log.log_command_history(command="/eth", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
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
        await log.log_command_history(command="/xmr", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
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
        await log.log_command_history(command="/doge", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
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
        await log.log_command_history(command="/xrp", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
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


async def setup(client: commands.Bot):
    await client.add_cog(Crypto(client))
