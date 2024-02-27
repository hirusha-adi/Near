import discord
from discord import app_commands
from discord.ext import commands

from .cmnds.crypto import Cmnds_Crypto


class Crypto(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="btc", description="Get the current Bitcoin Rates")
    async def btc(self, interaction: discord.Interaction):
        await Cmnds_Crypto.btc(interaction=interaction)

    @app_commands.command(name="eth", description="Get the current Etherium Rates")
    async def eth(self, interaction: discord.Interaction):
        await Cmnds_Crypto.eth(interaction=interaction)

    @app_commands.command(name="xmr", description="Get the current Monero Rates")
    async def xmr(self, interaction: discord.Interaction):
        await Cmnds_Crypto.xmr(interaction=interaction)

    @app_commands.command(name="doge", description="Get the current Doge Coin Rates")
    async def doge(self, interaction: discord.Interaction):
        await Cmnds_Crypto.doge(interaction=interaction)

    @app_commands.command(name="xrp", description="Get the current XRP Rates")
    async def xrp(self, interaction: discord.Interaction):
        await Cmnds_Crypto.xrp(interaction=interaction)

    @app_commands.command(name="rvn", description="Get the current Raven Coin Rates")
    async def rvn(self, interaction: discord.Interaction):
        await Cmnds_Crypto.rvn(interaction=interaction)


async def setup(client: commands.Bot):
    await client.add_cog(Crypto(client))
