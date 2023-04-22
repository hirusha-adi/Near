import os

import discord
import requests
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds

try:
    from faker import Faker
except:
    if os.name == 'nt':
        os.system(f"pip install Faker")
    else:
        os.system(f"pip3 install Faker")
finally:
    from faker import Faker

try:
    from faker_vehicle import VehicleProvider
except:
    if os.name == 'nt':
        os.system(f"pip install faker-vehicle")
    else:
        os.system(f"pip3 install faker-vehicle")
finally:
    from faker_vehicle import VehicleProvider


class SelectFakeHelp(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Main", emoji="⚡", description="The Main Set of Commands"),
            discord.SelectOption(label="Personal", emoji="🙍‍♂️", description="Fake Personal Information Related Commands"),
            discord.SelectOption(label="Location", emoji="📌", description="Fake Location Related Commands"),
            discord.SelectOption(label="Bank Cards", emoji="💳", description="Fake Bank Card Related Commands"),
            discord.SelectOption(label="Crypto", emoji="🪙", description="Fake Cryptocurrency Related Commands"),
            discord.SelectOption(label="Money", emoji="💵", description="Fake Money Related Commands"),
            discord.SelectOption(label="Date", emoji="📆", description="Fake Date Related Commands"),
            discord.SelectOption(label="File", emoji="🗃️", description="Fake File Related Commands"),
            discord.SelectOption(label="Unix", emoji="🖥️", description="Fake Unix Related Commands"),
            discord.SelectOption(label="Banking", emoji="🏦", description="Fake Banking Related Commands"),
            discord.SelectOption(label="Technical", emoji="⚙️", description="Fake Technical Information Related Commands"),
            discord.SelectOption(label="ISBN", emoji="💸", description="Fake ISBN Related Commands"),
            discord.SelectOption(label="Name", emoji="👧", description="Fake Name Related Commands"),
            discord.SelectOption(label="Texts", emoji="🧾", description="Fake Texts Related Commands"),
            discord.SelectOption(label="Phone Number", emoji="📞", description="Fake Phone Number Related Commands"),
            discord.SelectOption(label="User Agents", emoji="🕸️", description="Fake User Agents Related Commands"),
            discord.SelectOption(label="Platform Tokens", emoji="💻", description="Fake Platform Tokens Related Commands"),
            discord.SelectOption(label="Vehicle", emoji="🚓", description="Fake Vehicle Related Commands"),
            discord.SelectOption(label="Machine", emoji="⚒️", description="Fake Machine Related Commands"),
            discord.SelectOption(label="Others", emoji="🧸", description="Other Fake Commands")
        ]
        super().__init__(
            placeholder="Select an option",
            max_values=1,
            min_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        option = self.values[0]

        embed = discord.Embed(
            title=":gear: A Guide to All Available Commands :gear:",
            description="To access the complete list of commands and their respective descriptions, kindly select a category from the drop-down menu. For additional information and a comprehensive list of commands, please visit our website at https://teamsds.net/nearbot",
            color=get_embeds.Common.COLOR
        )
        embed.set_author(name=f"NearBot", icon_url=f"https://cdn.discordapp.com/attachments/953475157605892099/1073516633798225980/Avatar.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073538553335783454/7047060.png")
        embed.set_footer(text=f"Requested by {interaction.user.name}")

        if option == "Main":
            embed.add_field(name="/fake high", value="Generate a high amount of information", inline=False)
            embed.add_field(name="/fake low", value="Generate a low amount of information", inline=False)
            embed.add_field(name="/fake help", value="Show this / List all commands", inline=False)
            embed.add_field(name="/fakeprofiles [number=3]", value="Create several fake profiles with high information", inline=False)
        elif option == "Personal":
            embed.add_field(name="Fake Personal Information Related Commands", value=f"`/fake job`, \n`/fake licenseplate`, \n`/fake bs`, \n`/fake ssn`", inline=False)
        elif option == "Location":
            embed.add_field(name="Fake Location Related Commands", value=f"`/fake country`, \n`/fake postcode`, \n`/fake street addr`, \n`/fake street addr`, \n`/fake addr`, \n`/fake zipcode`, \n`/fake city`", inline=False)
        elif option == "Bank Cards":
            embed.add_field(name="Fake Bank Cards Related Commands", value=f"`/fake cc`, \n`/fake cc ex`, \n`/fake cc no`, \n`/fake cc pr`, \n`/fake cc cvv`", inline=False)
        elif option == "Crypto":
            embed.add_field(name="Fake Crypto Related Commands", value=f"`/fake crypto`, \n`/fake crypto code`, \n`/fake crypto name`", inline=False)
        elif option == "Money":
            embed.add_field(name="Fake Money Related Commands", value=f"`/fake curr`, \n`/fake curr code`, \n`/fake curr name`, \n`/fake curr symbol`, \n`/fake pricetag`", inline=False)
        elif option == "Date":
            embed.add_field(name="Fake Date Related Commands", value=f"`/fake date`, \n`/fake century`, \n`/fake dob`", inline=False)
        elif option == "File":
            embed.add_field(name="Fake File Related Commands", value=f"`/fake file name`, \n`/fake file ex`, \n`/fake file path`", inline=False)
        elif option == "Unix":
            embed.add_field(name="Fake Unix Related Commands", value=f"`/fake unix device`, \n`/fake unix partition`", inline=False)
        elif option == "Banking":
            embed.add_field(name="Fake Banking Related Commands", value=f"`/fake aba`, \n`/fake bank country`, \n`/fake bban`, \n`/fake iban`", inline=False)
        elif option == "Technical":
            embed.add_field(name="Fake Technical Information Related Commands", value=f"`/fake email`, \n`/fake cemail`, \n`/fake email free`, \n`/fake domain`, \n`/fake hostname`, \n`/fake http method`n \n`/fake img url`, \n`/fake ipv4`, \n`/fake ipv4 class`, \n`/fake ipv4 private`, \n`/fake ipv4 public`, \n`/fake ipv6`, \n`/fake macaddr`, \n`/fake nic handle`, \n`/fake port`, \n`/fake ripeid`, \n`/fake slug`, \n`/fake tld`, \n`/fake uri`, \n`/fake uri ex`, \n`/fake url`, \n`/fake username`", inline=False)
        elif option == "ISBN":
            embed.add_field(name="Fake ISBN Related Commands", value=f"`/fake isbn10`, \n`/fake isbn13`", inline=False)
        elif option == "Name":
            embed.add_field(name="Fake Name Related Commands", value=f"`/fake name`, \n`/fake fname`, \n`/fake fname male`, \n`/fake fname female`, \n`/fake fname nb`, \n`/fake lname`n \n`/fake lname male`, \n`/fake lname female`, \n`/fake lname nb`, \n`/fake name female`, \n`/fake name male`, \n`/fake name nb`, \n`/fake prefix`, \n`/fake suffix`", inline=False)
        elif option == "Texts":
            embed.add_field(name="Fake Texts Related Commands", value=f"`/fake paragraph`, \n`/fake sentence`, \n`/fake text`", inline=False)
        elif option == "Phone Number":
            embed.add_field(name="Fake Phone Number Related Commands", value=f"`/fake callingcode`, \n`/fake msisdn`, \n`/fake pno`", inline=False)
        elif option == "User Agents":
            embed.add_field(name="Fake User Agents Related Commands", value=f"`/fake chrome`, \n`/fake firefox`, \n`/fake ie`, \n`/fake opera`, \n`/fake safari`, \n`/fake ua`", inline=False)
        elif option == "Platform Tokens":
            embed.add_field(name="Fake Platform Tokens Related Commands", value=f"`/fake apt`, \n`/fake iospt`n \n`/fake linuxpt`, \n`/fake linuxproc`, \n`/fake macpt`, \n`/fake macprocessor`, \n`/fake winpt`, \n`/fake ua`", inline=False)
        elif option == "Vehicle":
            embed.add_field(name="Fake Vehicle Related Commands", value=f"`/fake vcl ymm`, \n`/fake vcl ymmc`, \n`/fake vcl mm`, \n`/fake vcl make`, \n`/fake vcl model`, \n`/fake vcl year`, \n`/fake vcl category`, \n`/fake vcl all`", inline=False)
        elif option == "Machine":
            embed.add_field(name="Fake Machine Related Commands", value=f"`/fake mcn ymm`, \n`/fake mcn ymmc`, \n`/fake mcn mm`, \n`/fake mcn make`, \n`/fake mcn model`, \n`/fake mcn year`, \n`/fake mcn category`, \n`/fake mcn all`, \n`/bottoken`", inline=False)
        elif option == "Others":
            embed.add_field(name="Other Fake Commands", value=f"`/fake ean`, \n`/fake company suffix`, \n`/fake iana`, \n`/fake lang`, \n`/fake color`, \n`/fake cp`", inline=False)

        # works as intended, but gives this error: "This interaction failed"
        await interaction.message.edit(embed=embed)

        # Sends message everytime an option is selected. Bad idea, but no bugged Error
        # await interaction.response.send_message(embed=embed, ephemeral=True)


class SelectViewFakeHelp(discord.ui.View):
    def __init__(self, *, timeout=60):
        super().__init__(timeout=timeout)
        self.add_item(SelectFakeHelp())


class FakeInformation(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="face", description="a Fake Face")
    @app_commands.describe(gender="Gender of the Face to be generated male/m or female/f")
    async def face(self, interaction: discord.Interaction, gender: str = "any"):
        try:
            male_wl = ("male", "man", "boy", "m")
            female_wl = ("female", "girl", "egirl",  "g", "f", "lady", "woman", "wife")

            fake = Faker()

            if gender.lower() in male_wl:
                r = requests.get("https://fakeface.rest/face/json?gender=male").json()
                embed = discord.Embed(title="Here is your generated face", color=get_embeds.FakeEmbeds.COLOR)
                embed.add_field(name="Name", value=f"{fake.first_name_male()} {fake.last_name_male()}", inline=False)
                embed.add_field(name="Gender", value="Male", inline=False)
                embed.add_field(name="Age", value=f"{r['age']}", inline=True)
                embed.set_image(url=f'{r["image_url"]}')
                embed.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed)
            elif gender.lower() in female_wl:
                r = requests.get("https://fakeface.rest/face/json?gender=female").json()
                embed2 = discord.Embed(title="Here is your generated face", color=get_embeds.FakeEmbeds.COLOR)
                embed2.add_field(name="Name", value=f"{fake.first_name_female()} {fake.last_name_female()}", inline=False)
                embed2.add_field(name="Gender", value="Female", inline=False)
                embed2.add_field(name="Age", value=f"{r['age']}", inline=True)
                embed2.set_image(url=f'{r["image_url"]}')
                embed2.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed2)
            else:  # any
                r = requests.get("https://fakeface.rest/face/json").json()
                embed3 = discord.Embed(title="Here is your generated face", color=get_embeds.FakeEmbeds.COLOR)
                if r['gender'] == "male":
                    embed3.add_field(name="Name", value=f"{fake.first_name_male()} {fake.last_name_male()}", inline=False)
                elif r['gender'] == "female":
                    embed3.add_field(name="Name", value=f"{fake.first_name_female()} {fake.last_name_female()}", inline=False)
                else:
                    pass
                embed3.add_field(name="Gender", value=f"{r['gender']}", inline=False)
                embed3.add_field(name="Age", value=f"{r['age']}", inline=True)
                embed3.set_image(url=f'{r["image_url"]}')
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="fake", description="Generate fake information")
    @app_commands.describe(category="What exactly to generate. Refer to help for additional information")
    async def fake(self, interaction: discord.Interaction, category: str = "help"):

        if category == "high":
            try:
                fake = Faker()
                simple_dict = fake.profile()
                emf = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf.set_footer(text=f"Requested by {interaction.user.name}")
                emf.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf.add_field(name="Name", value=f"{str(simple_dict['name'])}")
                emf.add_field(name="Job", value=f"{str(simple_dict['job'])}")
                emf.add_field(name="Birthdate", value=f"{str(simple_dict['birthdate'])}")
                emf.add_field(name="Company", value=f"{str(simple_dict['company'])}")
                emf.add_field(name="SSN", value=f"{str(simple_dict['ssn'])}")
                emf.add_field(name="Recidence", value=f"{str(simple_dict['residence'])}")
                emf.add_field(name="Current Location", value=f"{str(simple_dict['current_location'])}")
                emf.add_field(name="Blood Group", value=f"{str(simple_dict['blood_group'])}")
                emf.add_field(name="Username", value=f"{str(simple_dict['username'])}")
                emf.add_field(name="Address", value=f"{str(simple_dict['address'])}")
                emf.add_field(name="Mail", value=f"{str(simple_dict['mail'])}")

                await interaction.response.send_message(embed=emf)
            except Exception as e:
                embed2 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed2.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed2.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed2)

        elif category == "name":
            faker = Faker()
            try:
                USname = faker.name()
                emf2 = discord.Embed(
                    title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Name", value=f"{str(USname)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "dob":
            faker = Faker()
            try:
                USdob = faker.date_of_birth()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Date Of Birth", value=f"{str(USdob)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "addr":
            faker = Faker()
            try:
                USaddress = faker.address()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Address", value=f"{str(USaddress)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "job":
            faker = Faker()
            try:
                USjob = faker.job()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Job", value=f"{str(USjob)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "color":
            faker = Faker()
            try:
                USfavColor = faker.color_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Color", value=f"{str(USfavColor)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "zipcode":
            faker = Faker()
            try:
                USzip = faker.zipcode()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Zip Code", value=f"{str(USzip)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "city":
            faker = Faker()
            try:
                UScity = faker.city()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="City", value=f"{str(UScity)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "licenseplate":
            faker = Faker()
            try:
                USnumberPlate = faker.license_plate()
                emf2 = discord.Embed(
                    title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="License Plate", value=f"{str(USnumberPlate)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "bban":
            faker = Faker()
            try:
                USbasicBankAccountNumber = faker.bban()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Basic Bank Account", value=f"{str(USbasicBankAccountNumber)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "iban":
            faker = Faker()
            try:
                USinternationalBankAccountNumber = faker.iban()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="International Bank Account",
                               value=f"{str(USinternationalBankAccountNumber)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "bs":
            faker = Faker()
            try:
                USbs = faker.bs()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="BS", value=f"{str(USbs)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "cc":
            faker = Faker()
            try:
                UScreditcard = faker.credit_card_full()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Credit Card",
                               value=f"{str(UScreditcard)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "cemail":
            faker = Faker()
            try:
                UScompanyemail = faker.company_email()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Email", value=f"{str(UScompanyemail)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "pno":
            faker = Faker()
            try:
                USphoneNumber = faker.phone_number()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Phone Number",
                               value=f"{str(USphoneNumber)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "cp":
            faker = Faker()
            try:
                UScatchPhrase = faker.catch_phrase()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Catch Phrase",
                               value=f"{str(UScatchPhrase)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ssn":
            faker = Faker()
            try:
                USssa = faker.ssn()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="SSN", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "low":
            fake_low = Faker()
            try:
                shitthing_simple = fake_low.simple_profile()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(
                    name="Name", value=f"{str(shitthing_simple['name'])}")
                emf2.add_field(
                    name="Sex", value=f"{str(shitthing_simple['sex'])}")
                emf2.add_field(
                    name="Address", value=f"{str(shitthing_simple['address'])}")
                emf2.add_field(
                    name="Mail", value=f"{str(shitthing_simple['mail'])}")
                emf2.add_field(name="Birthday",
                               value=f"{str(shitthing_simple['birthdate'])}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "country":
            faker = Faker()
            try:
                USssa = faker.country()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Country", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "postcode":
            faker = Faker()
            try:
                USssa = faker.postcode()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Postcode", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "street addr":
            faker = Faker()
            try:
                USssa = faker.street_address()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Street Address", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "street addr":
            faker = Faker()
            try:
                USssa = faker.street_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Street Name", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "aba":
            faker = Faker()
            try:
                USssa = faker.aba()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="ABA", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "bank country":
            faker = Faker()
            try:
                USssa = faker.bank_country()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Bank Cuntry", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ean":
            # The usage is like 'fake ean 10' - 10 is the length
            faker = Faker()
            try:
                try:
                    nu_of_time = category.split(" ")[-1]
                    tempshit = int(nu_of_time)
                except:
                    nu_of_time = 10

                USssa = faker.ean(length=int(nu_of_time))
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="EAN Barcode", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "company suffix":
            faker = Faker()
            try:
                USssa = faker.company_suffix()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Company Suffix", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "cc ex":
            faker = Faker()
            try:
                USssa = faker.credit_card_expire()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Credit Card Expire Date",
                               value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "cc no":
            faker = Faker()
            try:
                USssa = faker.credit_card_number()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Credit Card Number",
                               value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "cc pr":
            faker = Faker()
            try:
                USssa = faker.credit_card_provider()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Credit Card Provider",
                               value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "cc cvv":
            faker = Faker()
            try:
                USssa = faker.credit_card_security_code()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Credit Card CVV", value=f"{str(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "crypto":
            faker = Faker()
            try:
                USssa = faker.cryptocurrency()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(
                    name="Cryptocurrency", value=f"Short Name: {USssa[0]} \nFull Name: {USssa[1]}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "crypto code":
            faker = Faker()
            try:
                USssa = faker.cryptocurrency_code()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Cryptocurrency Code", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "crypto name":
            faker = Faker()
            try:
                USssa = faker.cryptocurrency_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Cryptocurrency Name", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "curr":
            faker = Faker()
            try:
                USssa = faker.currency()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(
                    name="Currency", value=f"Short Name: {USssa[0]} \nFull Name: {USssa[1]}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "curr code":
            faker = Faker()
            try:
                USssa = faker.currency_code()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Currency Code", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "curr name":
            faker = Faker()
            try:
                USssa = faker.currency_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Currency Code", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category.lower().startswith("curr symbol"):
            faker = Faker()
            try:
                try:
                    currcode = category.split(' ')[-1]
                    USssa = faker.currency_symbol(code=str(currcode))
                except:
                    USssa = faker.currency_symbol()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Currency Code", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "pricetag":
            faker = Faker()
            try:
                USssa = faker.pricetag()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Pricetag", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "date":
            faker = Faker()
            try:
                USssa = faker.date()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Date", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "century":
            faker = Faker()
            try:
                USssa = faker.century()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Century", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "file name":
            faker = Faker()
            try:
                USssa = faker.file_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="File Name", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "file ex":
            faker = Faker()
            try:
                USssa = faker.file_extension()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="File Extension", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "file path":
            faker = Faker()
            try:
                USssa = faker.file_path()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="File Extension", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category.lower().startswith("mime"):
            faker = Faker()
            try:
                subcall = category.split(" ")
                try:
                    subc = faker.mime_type(subcall[-1])
                    USssa = faker.mime_type(category=subc)
                except:
                    USssa = faker.mime_type(category=subc)

                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="File Extension", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "unix device":
            faker = Faker()
            try:
                USssa = faker.unix_device()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Unix Device", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "unix partition":
            faker = Faker()
            try:
                USssa = faker.unix_partition()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Unix Partition", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "email":
            faker = Faker()
            try:
                USssa = faker.ascii_email()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Email Address", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "email free":
            faker = Faker()
            try:
                USssa = faker.ascii_free_email()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Email Address", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "domain":
            faker = Faker()
            try:
                USssa = faker.domain_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Email Address", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "hostname":
            faker = Faker()
            try:
                USssa = faker.hostname()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Hostname", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "http method":
            faker = Faker()
            try:
                USssa = faker.http_method()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="HTTP METHOD", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "iana":
            faker = Faker()
            try:
                USssa = faker.iana_id()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="IANA Registrar ID", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "img url":
            faker = Faker()
            try:
                USssa = faker.image_url()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Image URL", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ipv4":
            faker = Faker()
            try:
                USssa = faker.ipv4()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="IPv4", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ipv4 class":
            faker = Faker()
            try:
                USssa = faker.ipv4_network_class()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="IPv4 Netwrok Class", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ipv4 private":
            faker = Faker()
            try:
                USssa = faker.ipv4_private()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="a Private IPv4 Address", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ipv4 public":
            faker = Faker()
            try:
                USssa = faker.ipv4_public()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="a Public IPv4 Address", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ipv6":
            faker = Faker()
            try:
                USssa = faker.ipv6()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="IPv6", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "macaddr":
            faker = Faker()
            try:
                USssa = faker.mac_address()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Mac Address", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "nic handle":
            faker = Faker()
            try:
                USssa = faker.nic_handle()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="NIC Handle", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "port":
            faker = Faker()
            try:
                USssa = faker.port_number()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Port Number", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ripeid":
            faker = Faker()
            try:
                USssa = faker.ripe_id()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="RIPE ID", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "slug":
            faker = Faker()
            try:
                USssa = faker.slug()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Slug", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "tld":
            faker = Faker()
            try:
                USssa = faker.tld()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="TLD", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "uri":
            faker = Faker()
            try:
                USssa = faker.uri()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="URI", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "uri ex":
            faker = Faker()
            try:
                USssa = faker.uri_extension()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="URI Extension", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "url":
            faker = Faker()
            try:
                USssa = faker.url()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="URL", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "username":
            faker = Faker()
            try:
                USssa = faker.user_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Username", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "isbn10":
            faker = Faker()
            try:
                USssa = faker.isbn10()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="ISBN 10", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "isbn13":
            faker = Faker()
            try:
                USssa = faker.isbn13()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="ISBN 13", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "paragraph":
            faker = Faker()
            try:
                USssa = faker.paragraphs()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Paragraph", value=f"{''.join(USssa)}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "sentence":
            faker = Faker()
            try:
                USssa = faker.sentence()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Sentence", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "text":
            faker = Faker()
            try:
                USssa = faker.texts()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Text", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "word":
            faker = Faker()
            try:
                USssa = faker.word()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Word", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "fname":
            faker = Faker()
            try:
                USssa = faker.first_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="First Name", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "fname male":
            faker = Faker()
            try:
                USssa = faker.first_name_male()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="First Name - Male", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "fname female":
            faker = Faker()
            try:
                USssa = faker.first_name_male()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="First Name - Female", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "fname nb":
            faker = Faker()
            try:
                USssa = faker.first_name_nonbinary()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="First Name - Non Binary",
                               value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "lang":
            faker = Faker()
            try:
                USssa = faker.language_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Language Name", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "lname":
            faker = Faker()
            try:
                USssa = faker.last_name()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Last Name", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "lname male":
            faker = Faker()
            try:
                USssa = faker.last_name_male()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Last Name - Male", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "lname female":
            faker = Faker()
            try:
                USssa = faker.last_name_female()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Last Name - Female", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "lname nb":
            faker = Faker()
            try:
                USssa = faker.last_name_nonbinary()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Last Name - Non Binary", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "name female":
            faker = Faker()
            try:
                USssa = faker.name_female()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Name - Female", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "name male":
            faker = Faker()
            try:
                USssa = faker.name_male()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Name - Male", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "name nb":
            faker = Faker()
            try:
                USssa = faker.name_nonbinary()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Name - Non Binary", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "prefix":
            faker = Faker()
            try:
                USssa = faker.prefix()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Prefix", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "suffix":
            faker = Faker()
            try:
                USssa = faker.prefix()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Prefix", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "callingcode":
            faker = Faker()
            try:
                USssa = faker.country_calling_code()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Calling Code", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "msisdn":
            faker = Faker()
            try:
                USssa = faker.msisdn()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="MSISDN", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "apt":
            faker = Faker()
            try:
                USssa = faker.android_platform_token()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Android Platform Token", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "chrome":
            faker = Faker()
            try:
                USssa = faker.chrome()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="User Agent - Chrome", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "firefox":
            faker = Faker()
            try:
                USssa = faker.firefox()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="User Agent - FireFox", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ie":
            faker = Faker()
            try:
                USssa = faker.internet_explorer()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(
                    name="User Agent - Internet Explorer", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "iospt":
            faker = Faker()
            try:
                USssa = faker.ios_platform_token()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="IOS Platform Token", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "linuxpt":
            faker = Faker()
            try:
                USssa = faker.linux_platform_token()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Linux Platform Token", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "linuxproc":
            faker = Faker()
            try:
                USssa = faker.linux_processor()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Linux Processor", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "macpt":
            faker = Faker()
            try:
                USssa = faker.mac_platform_token()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="MAC - Platform Token", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "macprocessor":
            faker = Faker()
            try:
                USssa = faker.mac_processor()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="MAC Processor", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "opera":
            faker = Faker()
            try:
                USssa = faker.opera()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="User Agent - Opera", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "safari":
            faker = Faker()
            try:
                USssa = faker.opera()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="User Agent - Safari", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "winpt":
            faker = Faker()
            try:
                USssa = faker.windows_platform_token()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="Windows - Platform Token",
                               value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category == "ua":
            faker = Faker()
            try:
                USssa = faker.user_agent()
                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                emf2.add_field(name="User Agent", value=f"{USssa}")

                await interaction.response.send_message(embed=emf2)
            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category.lower().startswith('vcl'):
            fake = Faker()
            try:
                fake.add_provider(VehicleProvider)
                try:
                    fmall = category.split(" ")
                    fmlast = fmall[-1]
                except:
                    fmlast = "all"

                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")

                try:
                    if fmlast == "ymm":
                        vinfo = fake.vehicle_year_make_model()
                        emf2.add_field(name="Vehicle Infromation", value=f"**Year, Make, Model:** \n{vinfo}")

                    elif fmlast == "ymmc":
                        vinfo = fake.vehicle_year_make_model_cat()
                        emf2.add_field(
                            name="Vehicle Infromation", value=f"**Year, Make, Model, Cat:** \n{vinfo}")

                    elif fmlast == "mm":
                        vinfo = fake.vehicle_make_model()
                        emf2.add_field(name="Vehicle Infromation", value=f"**Make, Model:** \n{vinfo}")

                    elif fmlast == "make":
                        vinfo = fake.vehicle_make()
                        emf2.add_field(name="Vehicle Infromation", value=f"**Make:** {vinfo}")

                    elif fmlast == "model":
                        vinfo = fake.vehicle_model()
                        emf2.add_field(name="Vehicle Infromation", value=f"**Model:** {vinfo}")

                    elif fmlast == "year":
                        vinfo = fake.vehicle_model()
                        emf2.add_field(name="Vehicle Infromation", value=f"**Year:** {vinfo}")

                    elif fmlast == "category":
                        vinfo = fake.vehicle_category()
                        emf2.add_field(name="Vehicle Infromation", value=f"**Category:** {vinfo}")

                    else:
                        vinfo = fake.vehicle_object()
                        emf2.add_field(name="Vehicle Infromation", value=f"**Year:** {vinfo['Year']} \n**Make:** {vinfo['Make']} \n**Model:** {vinfo['Model']} \n**Category:** {vinfo['Category']}")

                except Exception as e:
                    embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                    embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                    embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                    embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                    embed3.set_footer(text=f"Requested by {interaction.user.name}")

                    await interaction.response.send_message(embed=embed3)
                    return

                await interaction.response.send_message(embed=emf2)

            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        elif category.lower().startswith('mcn'):
            fake = Faker()
            try:
                fake.add_provider(VehicleProvider)
                try:
                    fmall = category.split(" ")
                    fmlast = fmall[-1]
                except:
                    fmlast = "all"

                emf2 = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")

                try:
                    if fmlast == "ymm":
                        vinfo = fake.machine_year_make_model()
                        emf2.add_field(name="Machine Infromation", value=f"**Year, Make, Model:** \n{vinfo}")

                    elif fmlast == "ymmc":
                        vinfo = fake.machine_year_make_model_cat()
                        emf2.add_field(name="Machine Infromation", value=f"**Year, Make, Model, Cat:** \n{vinfo}")

                    elif fmlast == "mm":
                        vinfo = fake.machine_make_model()
                        emf2.add_field(name="Machine Infromation", value=f"**Make, Model:** \n{vinfo}")

                    elif fmlast == "make":
                        vinfo = fake.machine_make()
                        emf2.add_field(name="Machine Infromation", value=f"**Make:** {vinfo}")

                    elif fmlast == "model":
                        vinfo = fake.machine_model()
                        emf2.add_field(name="Machine Infromation", value=f"**Model:** {vinfo}")

                    elif fmlast == "year":
                        vinfo = fake.machine_year()
                        emf2.add_field(name="Machine Infromation", value=f"**Year:** {vinfo}")

                    elif fmlast == "category":
                        vinfo = fake.machine_category()
                        emf2.add_field(name="Machine Infromation", value=f"**Category:** {vinfo}")

                    else:
                        vinfo = fake.machine_object()
                        emf2.add_field(name="Machine Infromation", value=f"**Year:** {vinfo['Year']} \n**Make:** {vinfo['Make']} \n**Model:** {vinfo['Model']} \n**Category:** {vinfo['Category']}")

                except Exception as e:
                    embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                    embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                    embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                    embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                    embed3.set_footer(text=f"Requested by {interaction.user.name}")

                    await interaction.response.send_message(embed=embed3)
                    return

                await interaction.response.send_message(embed=emf2)

            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

        else:
            try:
                emf2 = discord.Embed(
                    title=get_embeds.FakeEmbeds.TITLE,
                    description="Please choose a category from the options below to access a comprehensive list of all the commands available within that category.",
                    color=get_embeds.FakeEmbeds.COLOR
                )
                emf2.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                emf2.set_footer(text=f"Requested by {interaction.user.name}")
                emf2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")

                await interaction.response.send_message(embed=emf2, view=SelectViewFakeHelp(), ephemeral=False)

            except Exception as e:
                embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
                embed3.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="fakeprofiles", description="Generate a given number of fake profiles")
    @app_commands.describe(amount="Amount of fake profiles to generate")
    async def fakeprofiles(self, interaction: discord.Interaction, amount: int = 3):

        try:
            fake_how_many = int(amount)

            # This is the limit for this command to stop spamming!
            if fake_how_many <= 3:

                embed = discord.Embed(
                    title="Mass Fake Profiles", color=get_embeds.FakeEmbeds.COLOR)
                embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                embed.add_field(name=f"{interaction.user.name} requested {amount} fake profiles!", value=f"Starting to send {amount} fake profiles!", inline=True)
                embed.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed)

                for i in range(fake_how_many):
                    fake = Faker()
                    simple_dict = fake.profile()
                    emf = discord.Embed(title=get_embeds.FakeEmbeds.TITLE, color=get_embeds.FakeEmbeds.COLOR)
                    emf.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                    emf.set_footer(text=f"Requested by {interaction.user.name}")
                    emf.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                    emf.add_field(name="Name", value=f"{str(simple_dict['name'])}")
                    emf.add_field(name="Job", value=f"{str(simple_dict['job'])}")
                    emf.add_field(name="Birthdate", value=f"{str(simple_dict['birthdate'])}")
                    emf.add_field(name="Company", value=f"{str(simple_dict['company'])}")
                    emf.add_field(name="SSN", value=f"{str(simple_dict['ssn'])}")
                    emf.add_field(name="Recidence", value=f"{str(simple_dict['residence'])}")
                    emf.add_field(name="Current Location", value=f"{str(simple_dict['current_location'])}")
                    emf.add_field(name="Blood Group", value=f"{str(simple_dict['blood_group'])}")
                    emf.add_field(name="Username", value=f"{str(simple_dict['username'])}")
                    emf.add_field(name="Address", value=f"{str(simple_dict['address'])}")
                    emf.add_field(name="Mail", value=f"{str(simple_dict['mail'])}")
                    await interaction.response.send_message(embed=emf)

            else:
                embed = discord.Embed(title="Mass Fake Profiles", color=get_embeds.FakeEmbeds.COLOR)
                embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed.set_thumbnail(url=get_embeds.FakeEmbeds.THUMBNAIL)
                embed.add_field(name="Error", value="Please enter a value below 4; This is done to prevent spam!", inline=True)
                embed.set_footer(text=f"Requested by {interaction.user.name}")

                await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="discordtoken", description="Generate a fake discord token")
    async def discordtoken(self, interaction: discord.Interaction):

        try:
            r = requests.get("https://some-random-api.ml/bottoken").json()

            embed = discord.Embed(title="Fake Discord Token Generator", description=f"`{r['token']}`", color=get_embeds.FakeEmbeds.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127767330-d3e68d90-67a0-4672-b3e1-6193b323bc21.png")
            embed.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880745781966037032/new-scrabble-words-2018-beatdown-5657-57124c9f228c0258d65053fe7d3891491x.jpg")
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)


async def setup(client: commands.Bot):
    await client.add_cog(FakeInformation(client))
