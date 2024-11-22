import discord
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
        
        commands = {
            "Main": [
                ("/fake high", "Generate a high amount of information"),
                ("/fake low", "Generate a low amount of information"),
                ("/fake help", "Show this / List all commands"),
                ("/fakeprofiles [number=3]", "Create several fake profiles with high information"),
            ],
            "Personal": [
                "Fake Personal Information Related Commands",
                "`/fake job`, `/fake licenseplate`, `/fake bs`, `/fake ssn`",
            ],
            "Location": [
                "Fake Location Related Commands",
                "`/fake country`, `/fake postcode`, `/fake street addr`, `/fake addr`, `/fake zipcode`, `/fake city`",
            ],
            "Bank Cards": [
                "Fake Bank Cards Related Commands",
                "`/fake cc`, `/fake cc ex`, `/fake cc no`, `/fake cc pr`, `/fake cc cvv`",
            ],
            "Crypto": [
                "Fake Crypto Related Commands",
                "`/fake crypto`, `/fake crypto code`, `/fake crypto name`",
            ],
            "Money": [
                "Fake Money Related Commands",
                "`/fake curr`, `/fake curr code`, `/fake curr name`, `/fake curr symbol`, `/fake pricetag`",
            ],
            "Date": [
                "Fake Date Related Commands",
                "`/fake date`, `/fake century`, `/fake dob`",
            ],
            "File": [
                "Fake File Related Commands",
                "`/fake file name`, `/fake file ex`, `/fake file path`",
            ],
            "Unix": [
                "Fake Unix Related Commands",
                "`/fake unix device`, `/fake unix partition`",
            ],
            "Banking": [
                "Fake Banking Related Commands",
                "`/fake aba`, `/fake bank country`, `/fake bban`, `/fake iban`",
            ],
            "Technical": [
                "Fake Technical Information Related Commands",
                "`/fake email`, `/fake cemail`, `/fake email free`, `/fake domain`, `/fake hostname`, `/fake http method`, "
                "`/fake img url`, `/fake ipv4`, `/fake ipv4 class`, `/fake ipv4 private`, `/fake ipv4 public`, `/fake ipv6`, "
                "`/fake macaddr`, `/fake nic handle`, `/fake port`, `/fake ripeid`, `/fake slug`, `/fake tld`, `/fake uri`, "
                "`/fake uri ex`, `/fake url`, `/fake username`",
            ],
            "ISBN": ["Fake ISBN Related Commands", "`/fake isbn10`, `/fake isbn13`"],
            "Name": [
                "Fake Name Related Commands",
                "`/fake name`, `/fake fname`, `/fake lname`, `/fake prefix`, `/fake suffix`",
            ],
            "Texts": [
                "Fake Texts Related Commands",
                "`/fake paragraph`, `/fake sentence`, `/fake text`",
            ],
            "Phone Number": [
                "Fake Phone Number Related Commands",
                "`/fake callingcode`, `/fake msisdn`, `/fake pno`",
            ],
            "User Agents": [
                "Fake User Agents Related Commands",
                "`/fake chrome`, `/fake firefox`, `/fake ie`, `/fake opera`, `/fake safari`, `/fake ua`",
            ],
            "Platform Tokens": [
                "Fake Platform Tokens Related Commands",
                "`/fake apt`,`/fake iosptn`",
            ],
            "Machine": ["Technically Generated Factory"],
        }


        embed = await embeds.Common(
            interaction=interaction,
            title=":gear: A Guide to All Available Commands :gear:",
            description="To access the complete list of commands and their respective descriptions, kindly select a category from the drop-down menu. For additional information and a comprehensive list of commands, please visit our website at https://teamsds.net/nearbot",
            thumbnail="fakeinfo_fake",
        )
        
        if option in commands:
            if isinstance(commands[option][0], tuple):  
                # Check if it's a list of command-value pairs
                for name, value in commands[option]:
                    embed.add_field(name=name, value=value, inline=False)
            else:  
                # It's a single description and commands
                embed.add_field(name=commands[option][0], value=commands[option][1], inline=False)
        
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

                    options = {
                        "ymm": lambda: f"**Year, Make, Model:** \n{fake.vehicle_year_make_model()}",
                        "ymmc": lambda: f"**Year, Make, Model, Cat:** \n{fake.vehicle_year_make_model_cat()}",
                        "mm": lambda: f"**Make, Model:** \n{fake.vehicle_make_model()}",
                        "make": lambda: f"**Make:** {fake.vehicle_make()}",
                        "model": lambda: f"**Model:** {fake.vehicle_model()}",
                        "year": lambda: f"**Year:** {fake.vehicle_year()}",
                        "category": lambda: f"**Category:** {fake.vehicle_category()}",
                    }
                    
                    em.add_field(
                        name="Vehicle Information",
                        value=options.get(
                            fmlast, 
                            lambda: (
                                lambda vinfo: f"**Year:** {vinfo['Year']} \n**Make:** {vinfo['Make']} \n**Model:** {vinfo['Model']} \n**Category:** {vinfo['Category']}"
                            )(fake.vehicle_object())
                        )()
                    )
                    
                elif category.lower().startswith('mcn'):
                    fake.add_provider(VehicleProvider)
                    try:
                        fmlast = category.split(" ")[-1]
                    except:
                        fmlast = "all"
                        
                    options = {
                        "ymm": lambda: f"**Year, Make, Model:** \n{fake.machine_year_make_model()}",
                        "ymmc": lambda: f"**Year, Make, Model, Cat:** \n{fake.machine_year_make_model_cat()}",
                        "mm": lambda: f"**Make, Model:** \n{fake.machine_make_model()}",
                        "make": lambda: f"**Make:** {fake.machine_make()}",
                        "model": lambda: f"**Model:** {fake.machine_model()}",
                        "year": lambda: f"**Year:** {fake.machine_year()}",
                        "category": lambda: f"**Category:** {fake.machine_category()}",
                    }
                    
                    em.add_field(
                        name="Machine Information",
                        value=options.get(
                            fmlast, 
                            lambda: (
                                lambda minfo: f"**Year:** {minfo['Year']} \n**Make:** {minfo['Make']} \n**Model:** {minfo['Model']} \n**Category:** {minfo['Category']}"
                            )(fake.machine_object())
                        )()
                    )

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
