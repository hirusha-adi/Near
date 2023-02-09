import discord
from discord.ext import commands
from discord import app_commands


class Texts(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="goodnight", description="✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩")
    async def goodnight(self, interaction: discord.Interaction):
        await interaction.response.send_message('✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩')

    @app_commands.command(name="smile", description='˙ ͜ʟ˙')
    async def smile(self, interaction: discord.Interaction):
        await interaction.response.send_message('˙ ͜ʟ˙')

    @app_commands.command(name="iloveu", description='(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥')
    async def iloveu(self, interaction: discord.Interaction):
        await interaction.response.send_message('(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥')

    @app_commands.command(name="sword", description='ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>')
    async def sword(self, interaction: discord.Interaction):
        await interaction.response.send_message('ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>')

    @app_commands.command(name="what", description='( ʘ̆ ╭͜ʖ╮ ʘ̆ )')
    async def what(self, interaction: discord.Interaction):
        await interaction.response.send_message('( ʘ̆ ╭͜ʖ╮ ʘ̆ )')

    @app_commands.command(name="fuckyou", description='╭∩╮(･◡･)╭∩╮')
    async def fuckyou(self, interaction: discord.Interaction):
        await interaction.response.send_message('╭∩╮(･◡･)╭∩╮')


async def setup(client: commands.Bot):
    await client.add_cog(Texts(client))
