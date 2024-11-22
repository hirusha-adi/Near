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

        embed = embeds.Common(
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
            em = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Fake Information",
                thumbnail="fakeinfo_fake",
            )
            
            if category == "high":
                    simple_dict = fake.profile()
                    em.add_field(name="Name", value=f"{str(simple_dict['name'])}")
                    em.add_field(name="Job", value=f"{str(simple_dict['job'])}")
                    em.add_field(name="Birthdate", value=f"{str(simple_dict['birthdate'])}")
                    em.add_field(name="Company", value=f"{str(simple_dict['company'])}")
                    em.add_field(name="SSN", value=f"{str(simple_dict['ssn'])}")
                    em.add_field(name="Recidence", value=f"{str(simple_dict['residence'])}")
                    em.add_field(name="Current Location", value=f"{str(simple_dict['current_location'])}")
                    em.add_field(name="Blood Group", value=f"{str(simple_dict['blood_group'])}")
                    em.add_field(name="Username", value=f"{str(simple_dict['username'])}")
                    em.add_field(name="Address", value=f"{str(simple_dict['address'])}")
                    em.add_field(name="Mail", value=f"{str(simple_dict['mail'])}")

            elif category == "name":
                USname = fake.name()
                em.add_field(name="Name", value=f"{USname}")

            elif category == "dob":
                USdob = fake.date_of_birth()
                em.add_field(name="Date Of Birth", value=f"{str(USdob)}")

            elif category == "addr":
                USaddress = fake.address()
                em.add_field(name="Address", value=f"{str(USaddress)}")

            elif category == "job":
                USjob = fake.job()
                em.add_field(name="Job", value=f"{str(USjob)}")

            elif category == "color":
                USfavColor = fake.color_name()
                em.add_field(name="Color", value=f"{str(USfavColor)}")

            elif category == "zipcode":
                USzip = fake.zipcode()
                em.add_field(name="Zip Code", value=f"{str(USzip)}")
                
            elif category == "city":
                UScity = fake.city()
                em.add_field(name="City", value=f"{str(UScity)}")

            elif category == "licenseplate":
                USnumberPlate = fake.license_plate()
                em.add_field(name="License Plate", value=f"{str(USnumberPlate)}")

            elif category == "bban":
                USbasicBankAccountNumber = fake.bban()
                em.add_field(name="Basic Bank Account", value=f"{str(USbasicBankAccountNumber)}")

            elif category == "iban":
                USinternationalBankAccountNumber = fake.iban()
                em.add_field(name="International Bank Account", value=f"{str(USinternationalBankAccountNumber)}")

            elif category == "bs":
                USbs = fake.bs()
                em.add_field(name="BS", value=f"{str(USbs)}")

            elif category == "cc":
                UScreditcard = fake.credit_card_full()
                em.add_field(name="Credit Card", value=f"{str(UScreditcard)}")

            elif category == "cemail":
                UScompanyemail = fake.company_email()
                em.add_field(name="Email", value=f"{str(UScompanyemail)}")

            elif category == "pno":
                USphoneNumber = fake.phone_number()
                em.add_field(name="Phone Number", value=f"{str(USphoneNumber)}")

            elif category == "cp":
                UScatchPhrase = fake.catch_phrase()
                em.add_field(name="Catch Phrase", value=f"{str(UScatchPhrase)}")
                
            elif category == "ssn":
                USssa = fake.ssn()
                em.add_field(name="SSN", value=f"{str(USssa)}")

            elif category == "low":
                shitthing_simple = fake.simple_profile()
                em.add_field(name="Name", value=f"{str(shitthing_simple['name'])}")
                em.add_field(name="Sex", value=f"{str(shitthing_simple['sex'])}")
                em.add_field(name="Address", value=f"{str(shitthing_simple['address'])}")
                em.add_field(name="Mail", value=f"{str(shitthing_simple['mail'])}")
                em.add_field(name="Birthday", value=f"{str(shitthing_simple['birthdate'])}")

            elif category == "country":
                USssa = fake.country()
                em.add_field(name="Country", value=f"{str(USssa)}")

            elif category == "postcode":
                USssa = fake.postcode()
                em.add_field(name="Postcode", value=f"{str(USssa)}")

            elif category == "street addr":
                USssa = fake.street_address()
                em.add_field(name="Street Address", value=f"{str(USssa)}")
                
            elif category == "street addr":
                USssa = fake.street_name()
                em.add_field(name="Street Name", value=f"{str(USssa)}")
                
            elif category == "aba":
                USssa = fake.aba()
                em.add_field(name="ABA", value=f"{str(USssa)}")
                
            elif category == "bank country":
                USssa = fake.bank_country()
                em.add_field(name="Bank Cuntry", value=f"{str(USssa)}")
                
            elif category == "ean":
                # The usage is like 'fake ean 10' - 10 is the length
                try:
                    nu_of_time = int(category.split(" ")[-1])
                except:
                    nu_of_time = 10
                USssa = fake.ean(length=int(nu_of_time))
                em.add_field(name="EAN Barcode", value=f"{str(USssa)}")

            elif category == "company suffix":
                USssa = fake.company_suffix()
                em.add_field(name="Company Suffix", value=f"{str(USssa)}")
                
            elif category == "cc ex":
                USssa = fake.credit_card_expire()
                em.add_field(name="Credit Card Expire Date", value=f"{str(USssa)}")
                
            elif category == "cc no":
                USssa = fake.credit_card_number()
                em.add_field(name="Credit Card Number", value=f"{str(USssa)}")
                
            elif category == "cc pr":
                USssa = fake.credit_card_provider()
                em.add_field(name="Credit Card Provider", value=f"{str(USssa)}")
                
            elif category == "cc cvv":
                USssa = fake.credit_card_security_code()
                em.add_field(name="Credit Card CVV", value=f"{str(USssa)}")
                
            elif category == "crypto":
                USssa = fake.cryptocurrency()
                em.add_field(name="Cryptocurrency", value=f"Short Name: {USssa[0]} \nFull Name: {USssa[1]}")
                
            elif category == "crypto code":
                USssa = fake.cryptocurrency_code()
                em.add_field(name="Cryptocurrency Code", value=f"{USssa}")
                
            elif category == "crypto name":
                USssa = fake.cryptocurrency_name()
                em.add_field(name="Cryptocurrency Name", value=f"{USssa}")

            elif category == "curr":
                USssa = fake.currency()
                em.add_field(name="Currency", value=f"Short Name: {USssa[0]} \nFull Name: {USssa[1]}")

            elif category == "curr code":
                USssa = fake.currency_code()
                em.add_field(name="Currency Code", value=f"{USssa}")
                

            elif category == "curr name":
                USssa = fake.currency_name()
                em.add_field(name="Currency Code", value=f"{USssa}")
                

            elif category.lower().startswith("curr symbol"):
                try:
                    currcode = category.split(' ')[-1]
                    USssa = fake.currency_symbol(code=str(currcode))
                except:
                    USssa = fake.currency_symbol()
                em.add_field(name="Currency Code", value=f"{USssa}")
                
            elif category == "pricetag":
                USssa = fake.pricetag()
                em.add_field(name="Pricetag", value=f"{USssa}")
                
            elif category == "date":
                USssa = fake.date()
                em.add_field(name="Date", value=f"{USssa}")

            elif category == "century":
                USssa = fake.century()
                em.add_field(name="Century", value=f"{USssa}")
                
            elif category == "file name":
                USssa = fake.file_name()
                em.add_field(name="File Name", value=f"{USssa}")
                

            elif category == "file ex":
                USssa = fake.file_extension()
                em.add_field(name="File Extension", value=f"{USssa}")
                

            elif category == "file path":
                USssa = fake.file_path()
                em.add_field(name="File Extension", value=f"{USssa}")
                
            elif category.lower().startswith("mime"):
                subcall = category.split(" ")
                try:
                    subc = fake.mime_type(subcall[-1])
                    USssa = fake.mime_type(category=subc)
                except:
                    USssa = fake.mime_type(category=subc)
                em.add_field(name="File Extension", value=f"{USssa}")
                

            elif category == "unix device":
                USssa = fake.unix_device()
                em.add_field(name="Unix Device", value=f"{USssa}")
                

            elif category == "unix partition":
                USssa = fake.unix_partition()
                em.add_field(name="Unix Partition", value=f"{USssa}")
                

            elif category == "email":
                USssa = fake.ascii_email()
                em.add_field(name="Email Address", value=f"{USssa}")
                

            elif category == "email free":
                USssa = fake.ascii_free_email()
                em.add_field(name="Email Address", value=f"{USssa}")
                

            elif category == "domain":
                USssa = fake.domain_name()
                em.add_field(name="Email Address", value=f"{USssa}")
                

            elif category == "hostname":
                USssa = fake.hostname()
                em.add_field(name="Hostname", value=f"{USssa}")
                

            elif category == "http method":
                USssa = fake.http_method()
                em.add_field(name="HTTP METHOD", value=f"{USssa}")
                

            elif category == "iana":
                USssa = fake.iana_id()
                em.add_field(name="IANA Registrar ID", value=f"{USssa}")
                

            elif category == "img url":
                USssa = fake.image_url()
                em.add_field(name="Image URL", value=f"{USssa}")
                

            elif category == "ipv4":
                USssa = fake.ipv4()
                em.add_field(name="IPv4", value=f"{USssa}")
                
            elif category == "ipv4 class":
                USssa = fake.ipv4_network_class()
                em.add_field(name="IPv4 Netwrok Class", value=f"{USssa}")
                
            elif category == "ipv4 private":
                USssa = fake.ipv4_private()
                em.add_field(name="a Private IPv4 Address", value=f"{USssa}")
            

            elif category == "ipv4 public":
                USssa = fake.ipv4_public()
                em.add_field(name="a Public IPv4 Address", value=f"{USssa}")
                

            elif category == "ipv6":
                USssa = fake.ipv6()
                em.add_field(name="IPv6", value=f"{USssa}")
                

            elif category == "macaddr":
                USssa = fake.mac_address()
                em.add_field(name="Mac Address", value=f"{USssa}")
                

            elif category == "nic handle":
                USssa = fake.nic_handle()
                em.add_field(name="NIC Handle", value=f"{USssa}")
                

            elif category == "port":
                USssa = fake.port_number()
                em.add_field(name="Port Number", value=f"{USssa}")
                
            elif category == "ripeid":
                USssa = fake.ripe_id()
                em.add_field(name="RIPE ID", value=f"{USssa}")
                
            elif category == "slug":
                USssa = fake.slug()
                em.add_field(name="Slug", value=f"{USssa}")
                
            elif category == "tld":
                USssa = fake.tld()
                em.add_field(name="TLD", value=f"{USssa}")
                
            elif category == "uri":
                USssa = fake.uri()
                em.add_field(name="URI", value=f"{USssa}")
                
            elif category == "uri ex":
                USssa = fake.uri_extension()
                em.add_field(name="URI Extension", value=f"{USssa}")
                
            elif category == "url":
                USssa = fake.url()
                em.add_field(name="URL", value=f"{USssa}")
                
            elif category == "username":
                USssa = fake.user_name()
                em.add_field(name="Username", value=f"{USssa}")
                
            elif category == "isbn10":
                USssa = fake.isbn10()
                em.add_field(name="ISBN 10", value=f"{USssa}")
                
            elif category == "isbn13":
                USssa = fake.isbn13()
                em.add_field(name="ISBN 13", value=f"{USssa}")

            elif category == "paragraph":
                USssa = fake.paragraphs()
                em.add_field(name="Paragraph", value=f"{''.join(USssa)}")
                
            elif category == "sentence":
                USssa = fake.sentence()
                em.add_field(name="Sentence", value=f"{USssa}")
                
            elif category == "text":
                USssa = fake.texts()
                em.add_field(name="Text", value=f"{USssa}")
                
            elif category == "word":
                USssa = fake.word()
                em.add_field(name="Word", value=f"{USssa}")
                
            elif category == "fname":
                USssa = fake.first_name()
                em.add_field(name="First Name", value=f"{USssa}")
                
            elif category == "fname male":
                USssa = fake.first_name_male()
                em.add_field(name="First Name - Male", value=f"{USssa}")
                
            elif category == "fname female":
                USssa = fake.first_name_male()
                em.add_field(name="First Name - Female", value=f"{USssa}")

            elif category == "fname nb":
                USssa = fake.first_name_nonbinary()
                em.add_field(name="First Name - Non Binary", value=f"{USssa}")
                

            elif category == "lang":
                USssa = fake.language_name()
                em.add_field(name="Language Name", value=f"{USssa}")
                
            elif category == "lname":
                USssa = fake.last_name()
                em.add_field(name="Last Name", value=f"{USssa}")
                
            elif category == "lname male":
                USssa = fake.last_name_male()
                em.add_field(name="Last Name - Male", value=f"{USssa}")
                
            elif category == "lname female":
                USssa = fake.last_name_female()
                em.add_field(name="Last Name - Female", value=f"{USssa}")
                
            elif category == "lname nb":
                USssa = fake.last_name_nonbinary()
                em.add_field(name="Last Name - Non Binary", value=f"{USssa}")
                
            elif category == "name female":
                USssa = fake.name_female()
                em.add_field(name="Name - Female", value=f"{USssa}")
                
            elif category == "name male":
                USssa = fake.name_male()
                em.add_field(name="Name - Male", value=f"{USssa}")
                
            elif category == "name nb":
                USssa = fake.name_nonbinary()
                em.add_field(name="Name - Non Binary", value=f"{USssa}")
                
            elif category == "prefix":
                USssa = fake.prefix()
                em.add_field(name="Prefix", value=f"{USssa}")
                
            elif category == "suffix":
                USssa = fake.prefix()
                em.add_field(name="Prefix", value=f"{USssa}")
                
            elif category == "callingcode":
                USssa = fake.country_calling_code()
                em.add_field(name="Calling Code", value=f"{USssa}")

            elif category == "msisdn":
                USssa = fake.msisdn()
                em.add_field(name="MSISDN", value=f"{USssa}")

            elif category == "apt":
                USssa = fake.android_platform_token()
                em.add_field(name="Android Platform Token", value=f"{USssa}")

            elif category == "chrome":
                USssa = fake.chrome()
                em.add_field(name="User Agent - Chrome", value=f"{USssa}")

            elif category == "firefox":
                USssa = fake.firefox()
                em.add_field(name="User Agent - FireFox", value=f"{USssa}")
                
            elif category == "ie":
                USssa = fake.internet_explorer()
                em.add_field(name="User Agent - Internet Explorer", value=f"{USssa}")
                
            elif category == "iospt":
                USssa = fake.ios_platform_token()
                em.add_field(name="IOS Platform Token", value=f"{USssa}")

            elif category == "linuxpt":
                USssa = fake.linux_platform_token()
                em.add_field(name="Linux Platform Token", value=f"{USssa}")
                
            elif category == "linuxproc":
                USssa = fake.linux_processor()
                em.add_field(name="Linux Processor", value=f"{USssa}")
        
            elif category == "macpt":
                USssa = fake.mac_platform_token()
                em.add_field(name="MAC - Platform Token", value=f"{USssa}")
                
            elif category == "macprocessor":
                USssa = fake.mac_processor()
                em.add_field(name="MAC Processor", value=f"{USssa}")
                
            elif category == "opera":
                USssa = fake.opera()
                em.add_field(name="User Agent - Opera", value=f"{USssa}")
                
            elif category == "safari":
                USssa = fake.opera()
                em.add_field(name="User Agent - Safari", value=f"{USssa}")
                
            elif category == "winpt":
                USssa = fake.windows_platform_token()
                em.add_field(name="Windows - Platform Token", value=f"{USssa}")
                
            elif category == "ua":
                USssa = fake.user_agent()
                em.add_field(name="User Agent", value=f"{USssa}")
                
            elif category.lower().startswith('vcl'):
                fake.add_provider(VehicleProvider)
                try:
                    fmall = category.split(" ")
                    fmlast = fmall[-1]
                except:
                    fmlast = "all"
                    
                if fmlast == "ymm":
                    vinfo = fake.vehicle_year_make_model()
                    em.add_field(name="Vehicle Infromation", value=f"**Year, Make, Model:** \n{vinfo}")
                elif fmlast == "ymmc":
                    vinfo = fake.vehicle_year_make_model_cat()
                    em.add_field(
                        name="Vehicle Infromation", value=f"**Year, Make, Model, Cat:** \n{vinfo}")
                elif fmlast == "mm":
                    vinfo = fake.vehicle_make_model()
                    em.add_field(name="Vehicle Infromation", value=f"**Make, Model:** \n{vinfo}")
                elif fmlast == "make":
                    vinfo = fake.vehicle_make()
                    em.add_field(name="Vehicle Infromation", value=f"**Make:** {vinfo}")
                elif fmlast == "model":
                    vinfo = fake.vehicle_model()
                    em.add_field(name="Vehicle Infromation", value=f"**Model:** {vinfo}")
                elif fmlast == "year":
                    vinfo = fake.vehicle_model()
                    em.add_field(name="Vehicle Infromation", value=f"**Year:** {vinfo}")
                elif fmlast == "category":
                    vinfo = fake.vehicle_category()
                    em.add_field(name="Vehicle Infromation", value=f"**Category:** {vinfo}")
                else:
                    vinfo = fake.vehicle_object()
                    em.add_field(name="Vehicle Infromation", value=f"**Year:** {vinfo['Year']} \n**Make:** {vinfo['Make']} \n**Model:** {vinfo['Model']} \n**Category:** {vinfo['Category']}")

            elif category.lower().startswith('mcn'):
                fake.add_provider(VehicleProvider)
                try:
                    fmlast = category.split(" ")[-1]
                except:
                    fmlast = "all"
                    
                if fmlast == "ymm":
                    vinfo = fake.machine_year_make_model()
                    em.add_field(name="Machine Infromation", value=f"**Year, Make, Model:** \n{vinfo}")
                elif fmlast == "ymmc":
                    vinfo = fake.machine_year_make_model_cat()
                    em.add_field(name="Machine Infromation", value=f"**Year, Make, Model, Cat:** \n{vinfo}")
                elif fmlast == "mm":
                    vinfo = fake.machine_make_model()
                    em.add_field(name="Machine Infromation", value=f"**Make, Model:** \n{vinfo}")
                elif fmlast == "make":
                    vinfo = fake.machine_make()
                    em.add_field(name="Machine Infromation", value=f"**Make:** {vinfo}")
                elif fmlast == "model":
                    vinfo = fake.machine_model()
                    em.add_field(name="Machine Infromation", value=f"**Model:** {vinfo}")
                elif fmlast == "year":
                    vinfo = fake.machine_year()
                    em.add_field(name="Machine Infromation", value=f"**Year:** {vinfo}")
                elif fmlast == "category":
                    vinfo = fake.machine_category()
                    em.add_field(name="Machine Infromation", value=f"**Category:** {vinfo}")
                else:
                    vinfo = fake.machine_object()
                    em.add_field(name="Machine Infromation", value=f"**Year:** {vinfo['Year']} \n**Make:** {vinfo['Make']} \n**Model:** {vinfo['Model']} \n**Category:** {vinfo['Category']}")

            else:
                em = embeds.Common(
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
                em1 = embeds.Common(
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
                    em2 = embeds.Common(
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
