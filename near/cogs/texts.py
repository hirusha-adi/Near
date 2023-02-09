import discord
from discord.ext import commands


class Texts(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def goodnight(self, ctx):
        await ctx.message.delete()
        night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
        await ctx.send(night)

    @commands.command()
    async def smile(self, ctx):
        await ctx.message.delete()
        smile = '˙ ͜ʟ˙'
        await ctx.send(smile)

    @commands.command()
    async def iloveu(self, ctx):
        await ctx.message.delete()
        love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
        await ctx.send(love)

    @commands.command()
    async def sword(self, ctx):
        await ctx.message.delete()
        sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
        await ctx.send(sword)

    @commands.command()
    async def what(self, ctx):
        await ctx.message.delete()
        what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
        await ctx.send(what)

    @commands.command()
    async def fuckyou(self, ctx):
        await ctx.message.delete()
        middlef = '╭∩╮(･◡･)╭∩╮'
        await ctx.send(middlef)


async def setup(client: commands.Bot):
    await client.add_cog(Texts(client))
