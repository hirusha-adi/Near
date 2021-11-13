import discord
import requests
from discord.ext import commands
from near.database import get_embeds


class Texts(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def goodnight(ctx):
        await ctx.message.delete()
        night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
        await ctx.send(night)

    @commands.command()
    async def smile(ctx):
        await ctx.message.delete()
        smile = '˙ ͜ʟ˙'
        await ctx.send(smile)

    @commands.command()
    async def iloveu(ctx):
        await ctx.message.delete()
        love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
        await ctx.send(love)

    @commands.command()
    async def sword(ctx):
        await ctx.message.delete()
        sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
        await ctx.send(sword)

    @commands.command()
    async def what(ctx):
        await ctx.message.delete()
        what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
        await ctx.send(what)

    @commands.command()
    async def fuckyou(ctx):
        await ctx.message.delete()
        middlef = '╭∩╮(･◡･)╭∩╮'
        await ctx.send(middlef)


def setup(client: commands.Bot):
    client.add_cog(Texts(client))
