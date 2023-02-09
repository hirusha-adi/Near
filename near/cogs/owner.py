import discord
import aiohttp
import io
from discord.ext import commands
from near.database import get_embeds
from datetime import datetime as datet


class Mods(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=get_embeds.PleaseWait.AUTHOR_NAME, icon_url=get_embeds.PleaseWait.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)

    @commands.command(aliases=["avatar", "pfp"])
    async def av(self, ctx, *, user: discord.User = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:

            format = "gif"
            user = user or ctx.author

            if user.is_avatar_animated() != True:
                format = "png"

            avatar = user.avatar_url_as(
                format=format if format != "gif" else None)

            async with aiohttp.ClientSession() as session:
                async with session.get(str(avatar)) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await loading_message.delete()
                await ctx.send(file=discord.File(file, f"Avatar.{format}"))

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
    async def serverinfo(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:

            date_format = "%a, %d %b %Y %I:%M %p"
            embed = discord.Embed(title=f"Server Info of {ctx.guild.name}:",
                                  description=f"**Members -** {ctx.guild.member_count}\n**Roles -** {len(ctx.guild.roles)}\n**Text-Channels -**{len(ctx.guild.text_channels)}\n**Voice-Channels -**{len(ctx.guild.voice_channels)}\n**Categories -**{len(ctx.guild.categories)}",
                                  timestamp=datet.utcnow(), color=get_embeds.Common.COLOR)
            embed.add_field(name="Server created at",
                            value=f"{ctx.guild.created_at.strftime(date_format)}")
            embed.add_field(name="Server Owner",
                            value=f"<@{ctx.guild.owner_id}>")
            embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
            embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
            embed.add_field(name="Bots", value=len(
                list(filter(lambda m: m.bot, ctx.guild.members))))
            embed.add_field(name="Banned members", value=len(await ctx.guild.bans()))
            embed.add_field(name="Invites", value=len(await ctx.guild.invites()))
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
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
    async def userinfo(self, ctx, target: discord.Member = None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            target = target or ctx.author

            embed = discord.Embed(title="User Information",
                                  color=target.color, timestamp=datet.utcnow())
            fields = [("Name", str(target), True),
                      ("ID", target.id, True),
                      ("Bot?", target.bot, True),
                      ("Top role", target.top_role.mention, True),
                      ("Status", str(target.status).title(), True),
                      ("Activity",
                       f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
                      ("Created at", target.created_at.strftime(
                          "%d/%m/%Y %H:%M:%S"), True),
                      ("Joined at", target.joined_at.strftime(
                          "%d/%m/%Y %H:%M:%S"), True),
                      ("Boosted", bool(target.premium_since), True)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_thumbnail(url=f"{target.avatar_url}")
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
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


async def setup(client: commands.Bot):
    await client.add_cog(Mods(client))
