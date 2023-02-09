import io
from datetime import datetime as datet

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds


class Mods(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name='avatar', description="Get the User Avatar")
    @app_commands.describe(user="User to get the Profile Picture of. Defaults to the Author")
    async def avatar(self, interaction: discord.Interaction, user: discord.User = None):

        try:
            format = "gif"
            user = user or interaction.user

            if user.display_avatar.is_animated() != True:
                format = "png"

            avatar = user.display_avatar.with_format(
                format=format if format != "gif" else None).url

            async with aiohttp.ClientSession() as session:
                async with session.get(str(avatar)) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await interaction.response.send_message(file=discord.File(file, f"Avatar.{format}"))

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.default_avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name='serverinfo', description="Get Information about the Server")
    async def serverinfo(self, interaction: discord.Interaction):
        try:

            date_format = "%a, %d %b %Y %I:%M %p"
            embed = discord.Embed(title=f"Server Info of {interaction.guild.name}:",
                                  description=f"**Members -** {interaction.guild.member_count}\n**Roles -** {len(interaction.guild.roles)}\n**Text-Channels -**{len(interaction.guild.text_channels)}\n**Voice-Channels -**{len(interaction.guild.voice_channels)}\n**Categories -**{len(interaction.guild.categories)}",
                                  timestamp=datet.utcnow(), color=get_embeds.Common.COLOR)
            embed.add_field(name="Server created at",
                            value=f"{interaction.guild.created_at.strftime(date_format)}")
            embed.add_field(name="Server Owner",
                            value=f"<@{interaction.guild.owner_id}>")
            embed.add_field(name="Server ID", value=f"{interaction.guild.id}")
            embed.add_field(name="Bots", value=len(
                list(filter(lambda m: m.bot, interaction.guild.members))))
            embed.add_field(name="Banned members", value=len(await interaction.guild.bans()))
            embed.add_field(name="Invites", value=len(await interaction.guild.invites()))
            embed.set_footer(text=f"Requested by {interaction.author.name}")
            embed.set_thumbnail(url=f"{interaction.guild.icon_url}")
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar.url}")
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.default_avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name='userinfo', description="Get Information about a User")
    @app_commands.describe(user="User to get the Information of. Defaults to the Author")
    async def userinfo(self, interaction: discord.Interaction, user: discord.Member = None):
        try:
            target = user or interaction.user

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

            embed.set_thumbnail(url=f"{target.default_avatar.url}")
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.default_avatar.url}")
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.default_avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)


async def setup(client: commands.Bot):
    await client.add_cog(Mods(client))
