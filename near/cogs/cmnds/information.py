import discord
import requests
from json import loads as loadjsonstring
import discord
import requests
import aiohttp

from near.utils import embeds
from near.utils import errors
from near.utils import input_sanitization


class Cmnds_Information:

    @errors.handle_error
    async def ipinfo(interaction: discord.Interaction, ip: str):
        if input_sanitization.is_ipaddr(ip):
            r = requests.get(f"https://ipapi.co/{ip}/json").json()
            rc = requests.get(f"https://api.worldbank.org/v2/country/{r['country_code']}?format=json").json()
            embed = embeds.Common(
                interaction=interaction,
                title="IP Information",
                thumbnail="https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png",
            )
            embed.add_field(name="IP Info", value="IP Address: " + str(r["ip"]) + "\nCity: " + str(r["city"]) + "\nRegion: " + str(r["region"]) + "\nCountry Name: " + str(r["country_name"]) + "\nLatitude: " + str(r["latitude"]) + "\nLongitude: " + str(r["longitude"]) + "\nTime Zone: " + str(r["timezone"]) + "\nUTC Offset: " + str(r["utc_offset"]) + "\nPostal Code: " + str(r["postal"]) + str("\nISP: " + r["org"]) + "\nASN: " + str(r["asn"]) + "\nCountry Code: " + str(r["country_code"]) + "\nCountry TLD: " + str(r["country_tld"]) + "\nPopulation: " + str(r["country_population"]) + "\nCurrency: " + str(r["currency"]) + "\n Curreny Name: " + str(r["currency_name"]) + "\nCountry Area: " + str(r["country_area"]) + "\nLanguages: " + str(r["languages"]) + "\nCalling Code: " + str(r["country_calling_code"]) + "\nGOOGLE MAPS Link: " + f"https://maps.google.com/?q={r['latitude']},{r['longitude']}", inline=False)
            embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]))
            return await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput
    
    @errors.handle_error
    async def countryinfo(interaction: discord.Interaction, country: str):
        if input_sanitization.check_input(country):
            rc = requests.get(f"https://api.worldbank.org/v2/country/{country}?format=json").json()
            embed = embeds.Common(
                interaction=interaction,
                title="Country Information",
                thumbnail="https://user-images.githubusercontent.com/36286877/129850352-33345963-273b-42bf-b2bc-5523c8158229.png",
            )
            embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
            return await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput
    
    @errors.handle_error
    async def covid(interaction: discord.Interaction):
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
                
        embed = embeds.Common(
            interaction=interaction,
            title="COVID-19 Stats Global - All Info",
            thumbnail="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png",
        )
        embed.add_field(name="Last Updated", value=update_date_time)
        embed.add_field(name="New Cases", value=global_new_cases)
        embed.add_field(name="Total Cases", value=global_total_cases)
        embed.add_field(name="Total Deaths", value=global_deaths)
        embed.add_field(name="New Deaths", value=global_new_deaths)
        embed.add_field(name="Total Recovered", value=global_recovered)
        embed.add_field(name="Total PCR Testing Count", value=total_pcr_testing_count)
        embed.add_field(name="Total Antigen Testing Count", value=total_antigen_testing_count)
        return await interaction.response.send_message(embed=embed)
    
    @errors.handle_error
    async def avatar(interaction: discord.Interaction, user: discord.User = None):
        user = user or interaction.user
        
        format_ = "gif"
        if user.display_avatar.is_animated() != True:
                format_ = "png"

        avatar = user.display_avatar.with_format(format_ if format_ != "gif" else None).url
        
        embed = embeds.Common(
            interaction=interaction,
            title=f"Profile Picture of {user.name}",
        )
        embed.set_image(url=avatar)
        return await interaction.response.send_message(embed=embed)
    
    @errors.handle_error
    async def serverinfo(interaction: discord.Interaction):
        date_format = "%a, %d %b %Y %I:%M %p"

        # Consider weather to keep this or remove this
        # this will take a huge amount of time if there are 1000s of bans in large servers
        # bans = [entry async for entry in interaction.guild.bans(limit=None)]

        embed = embeds.Common(
            interaction=interaction,
            title=f"Server Info of {interaction.guild.name}:",
            description=f"**Members -** {interaction.guild.member_count}\n**Roles -** {len(interaction.guild.roles)}\n**Text-Channels -**{len(interaction.guild.text_channels)}\n**Voice-Channels -**{len(interaction.guild.voice_channels)}\n**Categories -**{len(interaction.guild.categories)}",
        )
        embed.add_field(name="Server created at", value=f"{interaction.guild.created_at.strftime(date_format)}")
        embed.add_field(name="Server Owner", value=f"<@{interaction.guild.owner_id}>")
        embed.add_field(name="Server ID", value=f"{interaction.guild.id}")
        embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, interaction.guild.members))))
        # embed.add_field(name="Banned members", value=len(bans))
        embed.add_field(name="Invites", value=len(await interaction.guild.invites()))
        try:
            embed.set_thumbnail(url=f"{interaction.guild.icon.url}")
        except:
            pass
        
        return await interaction.response.send_message(embed=embed)
    
    @errors.handle_error
    async def userinfo(interaction: discord.Interaction, user: discord.Member = None):
        target = user or interaction.user

        fields = [("Name", str(target), True),
                      ("ID", target.id, True),
                      ("Bot?", target.bot, True),
                      ("Top role", target.top_role.mention, True),
                      ("Status", str(target.status).title(), True),
                      ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
                      ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                      ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                      ("Boosted", bool(target.premium_since), True)]
        
        embed = embeds.Common(
            interaction=interaction,
            title=f"User Information",
            description=f"**Members -** {interaction.guild.member_count}\n**Roles -** {len(interaction.guild.roles)}\n**Text-Channels -**{len(interaction.guild.text_channels)}\n**Voice-Channels -**{len(interaction.guild.voice_channels)}\n**Categories -**{len(interaction.guild.categories)}",
        )
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        embed.set_thumbnail(url=f"{target.avatar.url}")

        return await interaction.response.send_message(embed=embed)
        
