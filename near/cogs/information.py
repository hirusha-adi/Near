import aiohttp

import discord
from discord import app_commands
from discord.ext import commands
from loguru import logger

from near.utils import errors
from near.utils import embeds
from near.utils import input_sanitization


class Information(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="ipinfo", description="IP Address Lookup")
    @app_commands.describe(ip="IP Address to look for")
    async def ipinfo(self, interaction: discord.Interaction, ip: str):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            if input_sanitization.is_ipaddr(ip):
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://ipapi.co/{ip}/json") as response:
                        r = await response.json()

                    async with session.get(f"https://api.worldbank.org/v2/country/{r['country_code']}?format=json") as response:
                        rc = await response.json()

                embed = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="IP Information",
                    thumbnail="information_ipinfo",
                )
                embed.add_field(name="IP Info", value="IP Address: " + str(r["ip"]) + "\nCity: " + str(r["city"]) + "\nRegion: " + str(r["region"]) + "\nCountry Name: " + str(r["country_name"]) + "\nLatitude: " + str(r["latitude"]) + "\nLongitude: " + str(r["longitude"]) + "\nTime Zone: " + str(r["timezone"]) + "\nUTC Offset: " + str(r["utc_offset"]) + "\nPostal Code: " + str(r["postal"]) + str("\nISP: " + r["org"]) + "\nASN: " + str(r["asn"]) + "\nCountry Code: " + str(r["country_code"]) + "\nCountry TLD: " + str(r["country_tld"]) + "\nPopulation: " + str(r["country_population"]) + "\nCurrency: " + str(r["currency"]) + "\n Curreny Name: " + str(r["currency_name"]) + "\nCountry Area: " + str(r["country_area"]) + "\nLanguages: " + str(r["languages"]) + "\nCalling Code: " + str(r["country_calling_code"]) + "\nGOOGLE MAPS Link: " + f"https://maps.google.com/?q={r['latitude']},{r['longitude']}", inline=False)
                embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name='avatar', description="Get the User Avatar")
    @app_commands.describe(user="User to get the Profile Picture of. Defaults to the Author")
    async def avatar(self, interaction: discord.Interaction, user: discord.User = None):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            format = "gif"
            user = user or interaction.user
            if user.display_avatar.is_animated() != True:
                format = "png"

            avatar = user.display_avatar.with_format(format if format != "gif" else None).url

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title=f"Profile Picture of {user.name}",
            )
            embed.set_image(url=avatar)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name='serverinfo', description="Get Information about the Server")
    async def serverinfo(self, interaction: discord.Interaction):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            date_format = "%a, %d %b %Y %I:%M %p"

            # Consider weather to keep this or remove this
            # this will take a huge amount of time if there are 1000s of bans in large servers
            bans = [entry async for entry in interaction.guild.bans(limit=None)]

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title=f"Server Information of {interaction.guild.name}:",
                description=f"**Members:** {interaction.guild.member_count}\n**Roles:** {len(interaction.guild.roles)}\n**Text Channels:** {len(interaction.guild.text_channels)}\n**Voice Channels:** {len(interaction.guild.voice_channels)}\n**Categories:** {len(interaction.guild.categories)}",
            )
            embed.add_field(name="Server created at", value=f"{interaction.guild.created_at.strftime(date_format)}")
            embed.add_field(name="Server Owner", value=f"<@{interaction.guild.owner_id}>")
            embed.add_field(name="Server ID", value=f"{interaction.guild.id}")
            embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, interaction.guild.members))))
            embed.add_field(name="Banned members", value=len(bans))
            embed.add_field(name="Invites", value=len(await interaction.guild.invites()))
            try:
                embed.set_thumbnail(url=f"{interaction.guild.icon.url}")
            except:
                pass
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name='userinfo', description="Get Information about a User")
    @app_commands.describe(user="User to get the Information of. Defaults to the Author")
    async def userinfo(self, interaction: discord.Interaction, user: discord.Member = None):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            target = user or interaction.user

            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title=f"User Information",
                thumbnail=f"{target.avatar.url}"
            )

            fields = [
                ("Name", str(target), True),
                ("ID", target.id, True),
                ("Bot?", target.bot, True),
                ("Top role", target.top_role.mention, True),
                ("Status", str(target.status).title(), True),
                ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
                ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                ("Boosted", bool(target.premium_since), True)
            ]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(Information(client))
