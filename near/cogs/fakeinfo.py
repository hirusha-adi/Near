import os

import discord
import requests
from discord import app_commands
from discord.ext import commands
from faker import Faker
from faker_vehicle import VehicleProvider

from near.utils import embeds
from near.utils import errors


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

        embed = await embeds.Common(
            interaction=interaction,
            title=":gear: A Guide to All Available Commands :gear:",
            description="To access the complete list of commands and their respective descriptions, kindly select a category from the drop-down menu. For additional information and a comprehensive list of commands, please visit our website at https://teamsds.net/nearbot",
            thumbnail="fakeinfo_fake",
        )

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

        # works as intended, but gives this error: "This interaction failed" after some time
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

    @app_commands.command(name="fake", description="Generate fake information")
    @app_commands.describe(category="What exactly to generate. Refer to help for additional information")
    async def fake(self, interaction: discord.Interaction, category: str = "help"):
        try:
        
            fake = Faker()
            
            fake_methods = {
                "name": ("Name", lambda: fake.name()),
                "dob": ("Date Of Birth", lambda: fake.date_of_birth()),
                "addr": ("Address", lambda: fake.address()),
                "job": ("Job", lambda: fake.job()),
                "color": ("Color", lambda: fake.color_name()),
                "zipcode": ("Zip Code", lambda: fake.zipcode()),
                "city": ("City", lambda: fake.city()),
                "licenseplate": ("License Plate", lambda: fake.license_plate()),
                "bban": ("Basic Bank Account", lambda: fake.bban()),
                "iban": ("International Bank Account", lambda: fake.iban()),
                "bs": ("BS", lambda: fake.bs()),
                "cc": ("Credit Card", lambda: fake.credit_card_full()),
                "cemail": ("Email", lambda: fake.company_email()),
                "pno": ("Phone Number", lambda: fake.phone_number()),
                "cp": ("Catch Phrase", lambda: fake.catch_phrase()),
                "ssn": ("SSN", lambda: fake.ssn()),
                "country": ("Country", lambda: fake.country()),
                "postcode": ("Postcode", lambda: fake.postcode()),
                "street addr": ("Street Address", lambda: fake.street_address()),
                "street name": ("Street Name", lambda: fake.street_name()),
                "aba": ("ABA", lambda: fake.aba()),
                "bank country": ("Bank Country", lambda: fake.bank_country()),
                "company suffix": ("Company Suffix", lambda: fake.company_suffix()),
                "cc ex": ("Credit Card Expire Date", lambda: fake.credit_card_expire()),
                "cc no": ("Credit Card Number", lambda: fake.credit_card_number()),
                "cc pr": ("Credit Card Provider", lambda: fake.credit_card_provider()),
                "cc cvv": ("Credit Card CVV", lambda: fake.credit_card_security_code()),
                "crypto": ("Cryptocurrency", lambda: fake.cryptocurrency()),
                "crypto code": ("Cryptocurrency Code", lambda: fake.cryptocurrency_code()),
                "crypto name": ("Cryptocurrency Name", lambda: fake.cryptocurrency_name()),
                "curr": ("Currency", lambda: fake.currency()),
                "curr code": ("Currency Code", lambda: fake.currency_code()),
                "curr name": ("Currency Name", lambda: fake.currency_name()),
                "pricetag": ("Pricetag", lambda: fake.pricetag()),
                "date": ("Date", lambda: fake.date()),
                "century": ("Century", lambda: fake.century()),
                "file name": ("File Name", lambda: fake.file_name()),
                "file ex": ("File Extension", lambda: fake.file_extension()),
                "file path": ("File Path", lambda: fake.file_path()),
                "unix device": ("Unix Device", lambda: fake.unix_device()),
                "unix partition": ("Unix Partition", lambda: fake.unix_partition()),
                "email": ("Email Address", lambda: fake.ascii_email()),
                "email free": ("Free Email Address", lambda: fake.ascii_free_email()),
                "domain": ("Domain Name", lambda: fake.domain_name()),
                "hostname": ("Hostname", lambda: fake.hostname()),
                "http method": ("HTTP Method", lambda: fake.http_method()),
                "iana": ("IANA Registrar ID", lambda: fake.iana_id()),
                "img url": ("Image URL", lambda: fake.image_url()),
                "slug": ("Slug", lambda: fake.slug()),
                "tld": ("TLD", lambda: fake.tld()),
                "uri": ("URI", lambda: fake.uri()),
                "uri ex": ("URI Extension", lambda: fake.uri_extension()),
                "url": ("URL", lambda: fake.url()),
                "username": ("Username", lambda: fake.user_name()),
                "isbn10": ("ISBN 10", lambda: fake.isbn10()),
                "isbn13": ("ISBN 13", lambda: fake.isbn13()),
                "paragraph": ("Paragraph", lambda: "".join(fake.paragraphs())),
                "sentence": ("Sentence", lambda: fake.sentence()),
                "text": ("Text", lambda: fake.texts()),
                "word": ("Word", lambda: fake.word()),
                "fname": ("First Name", lambda: fake.first_name()),
                "fname male": ("First Name - Male", lambda: fake.first_name_male()),
                "fname female": ("First Name - Female", lambda: fake.first_name_female()),
                "fname nb": ("First Name - Non Binary", lambda: fake.first_name_nonbinary()),
                "lang": ("Language Name", lambda: fake.language_name()),
                "lname": ("Last Name", lambda: fake.last_name()),
                "lname male": ("Last Name - Male", lambda: fake.last_name_male()),
                "lname female": ("Last Name - Female", lambda: fake.last_name_female()),
                "lname nb": ("Last Name - Non Binary", lambda: fake.last_name_nonbinary()),
                "name female": ("Name - Female", lambda: fake.name_female()),
                "name male": ("Name - Male", lambda: fake.name_male()),
                "name nb": ("Name - Non Binary", lambda: fake.name_nonbinary()),
                "prefix": ("Prefix", lambda: fake.prefix()),
                "suffix": ("Suffix", lambda: fake.suffix()),
                "callingcode": ("Calling Code", lambda: fake.country_calling_code()),
                "msisdn": ("MSISDN", lambda: fake.msisdn()),
                "apt": ("Android Platform Token", lambda: fake.android_platform_token()),
                "chrome": ("User Agent - Chrome", lambda: fake.chrome()),
                "firefox": ("User Agent - FireFox", lambda: fake.firefox()),
                "ie": ("User Agent - Internet Explorer", lambda: fake.internet_explorer()),
                "iospt": ("IOS Platform Token", lambda: fake.ios_platform_token()),
                "linuxpt": ("Linux Platform Token", lambda: fake.linux_platform_token()),
                "linuxproc": ("Linux Processor", lambda: fake.linux_processor()),
                "macpt": ("MAC - Platform Token", lambda: fake.mac_platform_token()),
                "macprocessor": ("MAC Processor", lambda: fake.mac_processor()),
                "opera": ("User Agent - Opera", lambda: fake.opera()),
                "safari": ("User Agent - Safari", lambda: fake.safari()),
                "winpt": ("Windows - Platform Token", lambda: fake.windows_platform_token()),
                "ua": ("User Agent", lambda: fake.user_agent()),
                "ipv4": ("IPv4", lambda: fake.ipv4()),
                "ipv4 class": ("IPv4 Network Class", lambda: fake.ipv4_network_class()),
                "ipv4 private": ("Private IPv4 Address", lambda: fake.ipv4_private()),
                "ipv4 public": ("Public IPv4 Address", lambda: fake.ipv4_public()),
                "macaddr": ("MAC Address", lambda: fake.mac_address()),
                "nic handle": ("NIC Handle", lambda: fake.mac_address()),
                "port": ("Port Number", lambda: fake.port_number()),
                "ripeid": ("RIPE ID", lambda: fake.ripe_id()),
            }
            
            em = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Fake Information",
                thumbnail="fakeinfo_fake",
            )
            
            if category in fake_methods:
                label, value_func = fake_methods[category]
                value = value_func() # generate the value on-demand
                if category in ["crypto", "curr"]:
                    em.add_field(name=label, value=f"Short Name: {value[0]} \nFull Name: {value[1]}")
                else:
                    if isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set):
                        em.add_field(name=label, value=" ".join(value).replace("\\n", "\n"))
                    else:
                        em.add_field(name=label, value=str(value).replace("\\n", "\n"))
                    
            else:
            
                if category == "high":
                    simple_dict = fake.profile()
                    for key, value in simple_dict.items():
                        em.add_field(name=key.replace("_", " ").title(), value=str(value))
                
                elif category == "low":
                    shitthing_simple = fake.simple_profile()
                    for key, value in shitthing_simple.items():
                        em.add_field(name=key.replace("_", " ").title(), value=str(value))

                elif category == "ean":
                    # The usage is like 'fake ean 10' - 10 is the length
                    try:
                        nu_of_time = int(category.split(" ")[-1])
                    except:
                        nu_of_time = 10
                    em.add_field(name="EAN Barcode", value=f"{str(fake.ean(length=int(nu_of_time)))}")
                
                elif category.lower().startswith("curr symbol"):
                    try:
                        currcode = category.split(' ')[-1]
                        USssa = fake.currency_symbol(code=str(currcode))
                    except:
                        USssa = fake.currency_symbol()
                    em.add_field(name="Currency Code", value=f"{USssa}")
                    
                elif category.lower().startswith("mime"):
                    subcall = category.split(" ")
                    try:
                        subc = fake.mime_type(subcall[-1])
                        USssa = fake.mime_type(category=subc)
                    except:
                        USssa = fake.mime_type(category=subc)
                    em.add_field(name="File Extension", value=f"{USssa}")
                    
                elif category.lower().startswith('vcl'):
                    fake.add_provider(VehicleProvider)
                    try:
                        fmlast = category.split(" ")[-1]
                    except:
                        fmlast = "all"
                        
                    if fmlast == "ymm":
                        em.add_field(name="Vehicle Infromation", value=f"**Year, Make, Model:** \n{fake.vehicle_year_make_model()}")
                    elif fmlast == "ymmc":
                        em.add_field(name="Vehicle Infromation", value=f"**Year, Make, Model, Cat:** \n{fake.vehicle_year_make_model_cat()}")
                    elif fmlast == "mm":
                        em.add_field(name="Vehicle Infromation", value=f"**Make, Model:** \n{fake.vehicle_make_model()}")
                    elif fmlast == "make":
                        em.add_field(name="Vehicle Infromation", value=f"**Make:** {fake.vehicle_make()}")
                    elif fmlast == "model":
                        em.add_field(name="Vehicle Infromation", value=f"**Model:** {fake.vehicle_model()}")
                    elif fmlast == "year":
                        em.add_field(name="Vehicle Infromation", value=f"**Year:** {fake.vehicle_model()}")
                    elif fmlast == "category":
                        em.add_field(name="Vehicle Infromation", value=f"**Category:** {fake.vehicle_category()}")
                    else:
                        vinfo = fake.vehicle_object()
                        em.add_field(name="Vehicle Infromation", value=f"**Year:** {vinfo['Year']} \n**Make:** {vinfo['Make']} \n**Model:** {vinfo['Model']} \n**Category:** {vinfo['Category']}")

                    # TODO: minified version, test it out
                    # ---
                    # vehicle_info_map = {
                    #     "ymm": f"**Year, Make, Model:** \n{fake.vehicle_year_make_model()}",
                    #     "ymmc": f"**Year, Make, Model, Cat:** \n{fake.vehicle_year_make_model_cat()}",
                    #     "mm": f"**Make, Model:** \n{fake.vehicle_make_model()}",
                    #     "make": f"**Make:** {fake.vehicle_make()}",
                    #     "model": f"**Model:** {fake.vehicle_model()}",
                    #     "year": f"**Year:** {fake.vehicle_model()}",
                    #     "category": f"**Category:** {fake.vehicle_category()}",
                    #     "all": lambda: f"**Year:** {vinfo['Year']} \n**Make:** {vinfo['Make']} \n**Model:** {vinfo['Model']} \n**Category:** {vinfo['Category']}"
                    # }
                    # vinfo = fake.vehicle_object() if fmlast == "all" else None
                    # value = vehicle_info_map[fmlast]() if callable(vehicle_info_map[fmlast]) else vehicle_info_map[fmlast]
                    # em.add_field(name="Vehicle Information", value=value)
                    # ---
                    
                elif category.lower().startswith('mcn'):
                    fake.add_provider(VehicleProvider)
                    try:
                        fmlast = category.split(" ")[-1]
                    except:
                        fmlast = "all"
                        
                    if fmlast == "ymm":
                        em.add_field(name="Machine Infromation", value=f"**Year, Make, Model:** \n{fake.machine_year_make_model()}")
                    elif fmlast == "ymmc":
                        em.add_field(name="Machine Infromation", value=f"**Year, Make, Model, Cat:** \n{fake.machine_year_make_model_cat()}")
                    elif fmlast == "mm":
                        em.add_field(name="Machine Infromation", value=f"**Make, Model:** \n{fake.machine_make_model()}")
                    elif fmlast == "make":
                        em.add_field(name="Machine Infromation", value=f"**Make:** {fake.machine_make()}")
                    elif fmlast == "model":
                        em.add_field(name="Machine Infromation", value=f"**Model:** {fake.machine_model()}")
                    elif fmlast == "year":
                        em.add_field(name="Machine Infromation", value=f"**Year:** {fake.machine_year()}")
                    elif fmlast == "category":
                        em.add_field(name="Machine Infromation", value=f"**Category:** {fake.machine_category()}")
                    else:
                        vinfo = fake.machine_object()
                        em.add_field(name="Machine Infromation", value=f"**Year:** {vinfo['Year']} \n**Make:** {vinfo['Make']} \n**Model:** {vinfo['Model']} \n**Category:** {vinfo['Category']}")

                    # TODO: minified version, test it out
                    # ---
                    # machine_info_map = {
                    #     "ymm": f"**Year, Make, Model:** \n{fake.machine_year_make_model()}",
                    #     "ymmc": f"**Year, Make, Model, Cat:** \n{fake.machine_year_make_model_cat()}",
                    #     "mm": f"**Make, Model:** \n{fake.machine_make_model()}",
                    #     "make": f"**Make:** {fake.machine_make()}",
                    #     "model": f"**Model:** {fake.machine_model()}",
                    #     "year": f"**Year:** {fake.machine_year()}",
                    #     "category": f"**Category:** {fake.machine_category()}",
                    #     "all": lambda: f"**Year:** {vinfo['Year']} \n**Make:** {vinfo['Make']} \n**Model:** {vinfo['Model']} \n**Category:** {vinfo['Category']}"
                    # }
                    # vinfo = fake.machine_object() if fmlast == "all" else None
                    # value = machine_info_map[fmlast]() if callable(machine_info_map[fmlast]) else machine_info_map[fmlast]
                    # em.add_field(name="Machine Information", value=value)
                    # ---

                else:
                    em = await embeds.Common(
                        client=self.client,
                        interaction=interaction,
                        title="Fake Information",
                        description="Please choose a category from the options below to access a comprehensive list of all the commands available within that category.",
                        thumbnail="fakeinfo_fake"
                    )
                    return await interaction.response.send_message(embed=em, view=SelectViewFakeHelp(), ephemeral=False)

            return await interaction.response.send_message(embed=em)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)
    
    @app_commands.command(name="fakeprofiles", description="Generate a given number of fake profiles")
    @app_commands.describe(amount="Amount of fake profiles to generate")
    async def fakeprofiles(self, interaction: discord.Interaction, amount: int = 3):
        try:
            fake_how_many = int(amount)

            if fake_how_many <= 3: # to prevent spam
                em1 = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="Mass Fake Profiles", 
                    description="You can only request 3 profiles at a time!",
                    thumbnail="fakeinfo_fake"
                )
                em1.add_field(name=f"{interaction.user.name} requested {amount} fake profiles!", value=f"Starting to send {amount} fake profiles!", inline=True)
                await interaction.response.send_message(embed=em1)

                for _ in range(fake_how_many):
                    fake = Faker()
                    simple_dict = fake.profile()
                    em2 = await embeds.Common(
                        client=self.client,
                        interaction=interaction,
                        title="Fake Information", 
                        thumbnail="fakeinfo_fake"
                    )
                    em2.set_footer(text=f"Requested by {interaction.user.name}")
                    em2.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                    em2.add_field(name="Name", value=f"{str(simple_dict['name'])}")
                    em2.add_field(name="Job", value=f"{str(simple_dict['job'])}")
                    em2.add_field(name="Birthdate", value=f"{str(simple_dict['birthdate'])}")
                    em2.add_field(name="Company", value=f"{str(simple_dict['company'])}")
                    em2.add_field(name="SSN", value=f"{str(simple_dict['ssn'])}")
                    em2.add_field(name="Recidence", value=f"{str(simple_dict['residence'])}")
                    em2.add_field(name="Current Location", value=f"{str(simple_dict['current_location'])}")
                    em2.add_field(name="Blood Group", value=f"{str(simple_dict['blood_group'])}")
                    em2.add_field(name="Username", value=f"{str(simple_dict['username'])}")
                    em2.add_field(name="Address", value=f"{str(simple_dict['address'])}")
                    em2.add_field(name="Mail", value=f"{str(simple_dict['mail'])}")
                    await interaction.response.send_message(embed=em2)

            else:
                raise errors.IllegalInput("You can only request 3 profiles at a time. This is to prevent spam. Please try again!")

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(FakeInformation(client))
