import discord
import requests
from discord import app_commands
from discord.ext import commands
import io
import aiohttp
from datetime import datetime as datet

from near.database import get_embeds
from near.utils import input_sanitization, errors


class Information(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        self.filepwdlist1 = open("near/assets/tenmilpwds.txt", "r")
        self.lines = self.filepwdlist1.readlines()

    @app_commands.command(name="ipinfo", description="IP Address Lookup")
    @app_commands.describe(ip="IP Address to look for")
    async def ipinfo(self, interaction: discord.Interaction, ip: str):

        try:
            if input_sanitization.is_ipaddr(ip):
                r = requests.get(f"https://ipapi.co/{ip}/json").json()
                rc = requests.get(f"https://api.worldbank.org/v2/country/{r['country_code']}?format=json").json()
                
                embed = discord.Embed(title="IP Information",color=get_embeds.Common.COLOR)
                embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png")
                embed.set_footer(text=f"Requested by {interaction.user.name}")
                embed.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
                embed.add_field(name="IP Info", value="IP Address: " + str(r["ip"]) + "\nCity: " + str(r["city"]) + "\nRegion: " + str(r["region"]) + "\nCountry Name: " + str(r["country_name"]) + "\nLatitude: " + str(r["latitude"]) + "\nLongitude: " + str(r["longitude"]) + "\nTime Zone: " + str(r["timezone"]) + "\nUTC Offset: " + str(r["utc_offset"]) + "\nPostal Code: " + str(r["postal"]) + str("\nISP: " + r["org"]) + "\nASN: " + str(r["asn"]) + "\nCountry Code: " + str(r["country_code"]) + "\nCountry TLD: " + str(r["country_tld"]) + "\nPopulation: " + str(r["country_population"]) + "\nCurrency: " + str(r["currency"]) + "\n Curreny Name: " + str(r["currency_name"]) + "\nCountry Area: " + str(r["country_area"]) + "\nLanguages: " + str(r["languages"]) + "\nCalling Code: " + str(r["country_calling_code"]) + "\nGOOGLE MAPS Link: " + f"https://maps.google.com/?q={r['latitude']},{r['longitude']}", inline=False)
                embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput
            
        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="countryinfo", description="Country Information Lookup")
    @app_commands.describe(country="Country Code. Eg :- us, au, ca, sg, uk, nz")
    async def countryinfo(self, interaction: discord.Interaction, country: str):
        try:
            if input_sanitization.check_input(country):
                rc = requests.get(f"https://api.worldbank.org/v2/country/{country}?format=json").json()

                embed = discord.Embed(title="Country Information", color=get_embeds.Common.COLOR)
                embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/129850352-33345963-273b-42bf-b2bc-5523c8158229.png")
                embed.set_footer(text=f"Requested by {interaction.user.name}")
                embed.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
                embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="covid", description="Global Covid-19 Statistics")
    async def covid(self, interaction: discord.Interaction):
        try:
            r = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical")
            c = r.json()
            data = c['data']

            update_date_time = data['update_date_time']
            global_new_cases = data['global_new_cases']
            global_total_cases = data['global_total_cases']
            global_deaths = data['global_deaths']
            global_new_deaths = data['global_new_deaths']
            global_recovered = data['global_recovered']
            total_pcr_testing_count = data['total_pcr_testing_count']
            total_antigen_testing_count = data['total_antigen_testing_count']

            em = discord.Embed(title="COVID-19 Stats Global - All Info", color=get_embeds.Common.COLOR)
            em.set_footer(text=f"Requested by {interaction.user.name}")
            em.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
            em.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
            em.add_field(name="Last Updated", value=update_date_time)
            em.add_field(name="New Cases", value=global_new_cases)
            em.add_field(name="Total Cases", value=global_total_cases)
            em.add_field(name="Total Deaths", value=global_deaths)
            em.add_field(name="New Deaths", value=global_new_deaths)
            em.add_field(name="Total Recovered", value=global_recovered)
            em.add_field(name="Total PCR Testing Count",value=total_pcr_testing_count)
            em.add_field(name="Total Antigen Testing Count",value=total_antigen_testing_count)
            await interaction.response.send_message(embed=em)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name='avatar', description="Get the User Avatar")
    @app_commands.describe(user="User to get the Profile Picture of. Defaults to the Author")
    async def avatar(self, interaction: discord.Interaction, user: discord.User = None):
        # input sanitization not needed here
        try:
            format = "gif"
            user = user or interaction.user

            if user.display_avatar.is_animated() != True:
                format = "png"

            avatar = user.display_avatar.with_format(format if format != "gif" else None).url
            
            embed = discord.Embed(title=f"Profile Picture of {user.name}", color=get_embeds.Common.COLOR)
            embed.set_image(url=avatar)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            
            return await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name='serverinfo', description="Get Information about the Server")
    async def serverinfo(self, interaction: discord.Interaction):
        try:

            date_format = "%a, %d %b %Y %I:%M %p"
            
            embed = discord.Embed(
                title=f"Server Info of {interaction.guild.name}:",
                description=f"**Members -** {interaction.guild.member_count}\n**Roles -** {len(interaction.guild.roles)}\n**Text-Channels -**{len(interaction.guild.text_channels)}\n**Voice-Channels -**{len(interaction.guild.voice_channels)}\n**Categories -**{len(interaction.guild.categories)}",
                timestamp=datet.utcnow(), color=get_embeds.Common.COLOR
            )
            embed.add_field(name="Server created at",value=f"{interaction.guild.created_at.strftime(date_format)}")
            embed.add_field(name="Server Owner",value=f"<@{interaction.guild.owner_id}>")
            embed.add_field(name="Server ID", value=f"{interaction.guild.id}")
            embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, interaction.guild.members))))
            embed.add_field(name="Banned members", value=len(await interaction.guild.bans()))
            embed.add_field(name="Invites", value=len(await interaction.guild.invites()))
            embed.set_footer(text=f"Requested by {interaction.author.name}")
            embed.set_thumbnail(url=f"{interaction.guild.icon_url}")
            embed.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name='userinfo', description="Get Information about a User")
    @app_commands.describe(user="User to get the Information of. Defaults to the Author")
    async def userinfo(self, interaction: discord.Interaction, user: discord.Member = None):
        # input sanitization not needed here
        try:
            target = user or interaction.user
            embed = discord.Embed(title="User Information",color=target.color, timestamp=datet.utcnow())
            
            fields = [("Name", str(target), True),
                      ("ID", target.id, True),
                      ("Bot?", target.bot, True),
                      ("Top role", target.top_role.mention, True),
                      ("Status", str(target.status).title(), True),
                      ("Activity",f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
                      ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                      ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                      ("Boosted", bool(target.premium_since), True)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            embed.set_thumbnail(url=f"{target.avatar.url}")
            embed.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)


async def setup(client: commands.Bot):
    await client.add_cog(Information(client))
