import discord
from discord import app_commands
from discord.ext import commands

from .cmnds.information import Cmnds_Information


class Information(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="ipinfo", description="IP Address Lookup")
    @app_commands.describe(ip="IP Address to look for")
    async def ipinfo(self, interaction: discord.Interaction, ip: str):
        await Cmnds_Information.ipinfo(interaction=interaction, ip=ip)

    @app_commands.command(name="countryinfo", description="Country Information Lookup")
    @app_commands.describe(country="Country Code. Eg :- us, au, ca, sg, uk, nz")
    async def countryinfo(self, interaction: discord.Interaction, country: str):
        await Cmnds_Information.countryinfo(interaction=interaction, country=country)

    @app_commands.command(name="covid", description="Global Covid-19 Statistics")
    async def covid(self, interaction: discord.Interaction):
        await Cmnds_Information.covid(interaction=interaction)


    @app_commands.command(name='avatar', description="Get the User Avatar")
    @app_commands.describe(user="User to get the Profile Picture of. Defaults to the Author")
    async def avatar(self, interaction: discord.Interaction, user: discord.User = None):
        await Cmnds_Information.avatar(interaction=interaction, user=user)

    @app_commands.command(name='serverinfo', description="Get Information about the Server")
    async def serverinfo(self, interaction: discord.Interaction):
        await Cmnds_Information.serverinfo(interaction=interaction)

    @app_commands.command(name='userinfo', description="Get Information about a User")
    @app_commands.describe(user="User to get the Information of. Defaults to the Author")
    async def userinfo(self, interaction: discord.Interaction, user: discord.Member = None):
        await Cmnds_Information.userinfo(interaction=interaction, user=user)


async def setup(client: commands.Bot):
    await client.add_cog(Information(client))
