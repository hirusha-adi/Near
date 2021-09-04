from keep_alive import keep_alive
import platform
import os
from password_strength import PasswordStats
import discord
from discord.ext import commands
import requests
import json
from faker import *
import time
import datetime
import aiohttp
from bs4 import BeautifulSoup
import urllib
import base64
import hashlib
import instaloader
import textwrap
import youtube_dl

# FOR MUSIC COMMAND
import asyncio
import functools
import itertools
import math
import random
from async_timeout import timeout

botconfigdata = json.load(open("config.json", "r"))
bot_prefix = botconfigdata["msg-prefix"]
bot_creator_name = botconfigdata["bot-creator-name"]
bot_current_version = botconfigdata["bot-version"]

client = commands.Bot(command_prefix = bot_prefix)
client.remove_command('help')
token = botconfigdata["bottoken"]


start_time = None

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print(f'Discord.py API version: {discord.__version__}')
    print(f'Python version: {platform.python_version()}')

    global start_time
    start_time = time.time()

    client.load_extension('dismusic')

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"teamsds.net/discord"))
    print('Bot is ready!')


# THIS IS THE PLASE WAIT TEMPLATE!
# Almost all the commands use this, you can change it here!
please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
please_wait_emb.set_author(name="NearBot")
please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")
please_wait_wt_bfd = 2



filepwdlist1 = open("pwds2.txt", "r")
lines = filepwdlist1.readlines()

@client.command()
async def pwdcheck(ctx, *, password):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
        if password + "\n" in lines:
            embed=discord.Embed(title="Password Checker!", color=0xff0000)
            embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
            embed.add_field(name=f"Your Passoword", value=f"{password}", inline=False)
            embed.add_field(name=f"Safety", value=f"Not Safe. This password is in the list of most common 10 million passwords!", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Password Checker!", color=0xff0000)
            embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
            embed.add_field(name=f"Your Passoword", value=f"{password}", inline=False)
            embed.add_field(name=f"Safety", value=f"Safe. This password is not in the list of most common 10 million passwords!", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

    except Exception as e:
        embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed2.add_field(name="Error:", value=f"{e}", inline=False)
        embed2.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed2)

@client.command() 
async def ping(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)
    try:
        embed=discord.Embed(title="Response Time", color=0xff0000)
        embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
        embed.add_field(name=f"Ping :timer:", value=f"{round(client.latency * 1000)} ms", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed)

    except Exception as e:
        embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed2.add_field(name="Error:", value=f"{e}", inline=False)
        embed2.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed2)

@client.command()
async def fake(ctx, *, fake_mode="help"):
    loading_message = await ctx.send(embed=please_wait_emb)
    
    # All the information generated is in sync with each other
    if fake_mode == "high":
      try:
        fake = Faker()
        simple_dict = fake.profile()
        # fake_info_simple = "Name: " + str(simple_dict['name']) + "\nJob: " + str(simple_dict['job']) + "\nBirthdate: " + str(simple_dict['birthdate']) + "\nCompany: " + str(simple_dict['company']) + "\SSN: " + str(simple_dict['ssn']) + "\nRecidence: " + simple_dict['residence'] + "\nCurrent Location:" + str(simple_dict['current_location']) + "\nBlood Group: " + str(simple_dict['blood_group']) + "\nUsername: " + str(simple_dict['username']) + "\nAddress: " + str(simple_dict['address']) + "\nMail: " + str(simple_dict['mail'])
        emf = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf.set_footer(text=f"Requested by {ctx.author.name}")
        emf.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
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
        await loading_message.delete()
        await ctx.send(embed=emf)
      except Exception as e:
        embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed2.add_field(name="Error:", value=f"{e}", inline=False)
        embed2.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed2)
    
    # Only a name
    elif fake_mode == "name":
      faker = Faker()
      try:
        USname = faker.name()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Name", value=f"{str(USname)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the Date of Birth
    elif fake_mode == "dob":
      faker = Faker()
      try:
        USdob = faker.date_of_birth()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Date Of Birth", value=f"{str(USdob)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the Address
    elif fake_mode == "addr":
      faker = Faker()
      try:
        USaddress = faker.address()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Address", value=f"{str(USaddress)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the JOB
    elif fake_mode == "job":
      faker = Faker()
      try:
        USjob = faker.job()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Job", value=f"{str(USjob)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the color
    elif fake_mode == "color":
      faker = Faker()
      try:
        USfavColor = faker.color_name()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Color", value=f"{str(USfavColor)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the ZipCode
    elif fake_mode == "zipcode":
      faker = Faker()
      try:
        USzip = faker.zipcode()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Zip Code", value=f"{str(USzip)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only the city
    elif fake_mode == "city":
      faker = Faker()
      try:
        UScity = faker.city()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="City", value=f"{str(UScity)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a lisence plate number
    elif fake_mode == "licenseplate":
      faker = Faker()
      try:
        USnumberPlate = faker.license_plate()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="License Plate", value=f"{str(USnumberPlate)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a Basic Bank Account Number
    elif fake_mode == "bban":
      faker = Faker()
      try:
        USbasicBankAccountNumber = faker.bban()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Basic Bank Account", value=f"{str(USbasicBankAccountNumber)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a International Bank Account Number
    elif fake_mode == "iban":
      faker = Faker()
      try:
        USinternationalBankAccountNumber = faker.iban()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="International Bank Account", value=f"{str(USinternationalBankAccountNumber)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a BSc
    elif fake_mode == "bs":
      faker = Faker()
      try:
        USbs = faker.bs()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="BS", value=f"{str(USbs)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only credit card information, provides everything
    elif fake_mode == "cc":
      faker = Faker()
      try:
        UScreditcard = faker.credit_card_full()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Credit Card", value=f"{str(UScreditcard)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # only a Company Email
    elif fake_mode == "cemail":
      faker = Faker()
      try:
        UScompanyemail = faker.company_email()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Email", value=f"{str(UScompanyemail)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a Phone Number
    elif fake_mode == "pno":
      faker = Faker()
      try:
        USphoneNumber = faker.phone_number()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Phone Number", value=f"{str(USphoneNumber)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a Catch Phrase
    elif fake_mode == "cp":
      faker = Faker()
      try:
        UScatchPhrase = faker.catch_phrase()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Catch Phrase", value=f"{str(UScatchPhrase)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Only a SSN
    elif fake_mode == "ssn":
      faker = Faker()
      try:
        USssa = faker.ssn()
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="SSN", value=f"{str(USssa)}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Generate the basic information
    elif fake_mode == "low":
      fake_low = Faker()
      try:
        shitthing_simple = fake_low.simple_profile()
        # fake_info_low_info = "Name: " + str(shitthing_simple['name']) + "\nSex: " + str(shitthing_simple['sex']) + "\nAddress: " + str(shitthing_simple['address']) + "\nMail: " + str(shitthing_simple['mail']) + "\nBirthday: " + str(shitthing_simple['birthdate'])
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name="Name", value=f"{str(shitthing_simple['name'])}")
        emf2.add_field(name="Sex", value=f"{str(shitthing_simple['sex'])}")
        emf2.add_field(name="Address", value=f"{str(shitthing_simple['address'])}")
        emf2.add_field(name="Mail", value=f"{str(shitthing_simple['mail'])}")
        emf2.add_field(name="Birthday", value=f"{str(shitthing_simple['birthdate'])}")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
    # Show help
    elif fake_mode == "help":
      bp = bot_prefix
      try:
        emf2 = discord.Embed(title="Fake Information Generator", color=0xF00000)
        emf2.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        emf2.set_footer(text=f"Requested by {ctx.author.name}")
        emf2.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        emf2.add_field(name=f"{bp}fake high", value=f"Generate a high amount of information")
        emf2.add_field(name=f"{bp}fake low", value=f"Generate a low amount of information")
        emf2.add_field(name=f"{bp}fake help", value=f"Show this / list all commands")
        emf2.add_field(name=f"{bp}fake name", value=f"Generate a fake name")
        emf2.add_field(name=f"{bp}fake dob", value=f"Generate a fake Date of Birth")
        emf2.add_field(name=f"{bp}fake addr", value=f"Generate a fake Address")
        emf2.add_field(name=f"{bp}fake job", value=f"Generate a fake Job")
        emf2.add_field(name=f"{bp}fake color", value=f"Generate a random color")
        emf2.add_field(name=f"{bp}fake zipcode", value=f"Generate a random zipcode")
        emf2.add_field(name=f"{bp}fake city", value=f"Generate a random City name")
        emf2.add_field(name=f"{bp}fake licenseplate", value=f"Generate a fake licenseplate number")
        emf2.add_field(name=f"{bp}fake bban", value=f"Generate a fake Basic Bank Account")
        emf2.add_field(name=f"{bp}fake bban", value=f"Generate a fake International Bank Account")
        emf2.add_field(name=f"{bp}fake bs", value=f"Generate a random BS degree")
        emf2.add_field(name=f"{bp}fake cc", value=f"Generate fake Credit Card Information")
        emf2.add_field(name=f"{bp}fake cemail", value=f"Generate a fake company email")
        emf2.add_field(name=f"{bp}fake pno", value=f"Generate a fake Phone Number")
        emf2.add_field(name=f"{bp}fake cp", value=f"Generate a fake Catch Phrase")
        emf2.add_field(name=f"{bp}fake ssn", value=f"Generate a fake SSN")
        await loading_message.delete()
        await ctx.send(embed=emf2)
      except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)

@client.command(aliases=["ipinfo", "infoip", "ip-info", "info-ip"])
async def ip(ctx, *, ip_from_user):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      r = requests.get(f"https://ipapi.co/{ip_from_user}/json").json()
      rc = requests.get(f"https://api.worldbank.org/v2/country/{r['country_code']}?format=json").json()

      embed=discord.Embed(title="IP Information", color=0xff0000)
      embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png")
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed.add_field(name="IP Info", value="IP Address: " + str(r["ip"]) + "\nCity: " + str(r["city"]) + "\nRegion: " + str(r["region"]) + "\nCountry Name: " + str(r["country_name"]) + "\nLatitude: " + str(r["latitude"]) + "\nLongitude: " + str(r["longitude"]) + "\nTime Zone: " + str(r["timezone"]) + "\nUTC Offset: " + str(r["utc_offset"]) + "\nPostal Code: " + str(r["postal"]) + str("\nISP: " + r["org"]) + "\nASN: " + str(r["asn"]) + "\nCountry Code: " + str(r["country_code"]) + "\nCountry TLD: " + str(r["country_tld"]) + "\nPopulation: " + str(r["country_population"]) + "\nCurrency: " + str(r["currency"]) + "\n Curreny Name: " + str(r["currency_name"]) + "\nCountry Area: " + str(r["country_area"]) + "\nLanguages: " + str(r["languages"]) + "\nCalling Code: " + str(r["country_calling_code"]) + "\nGOOGLE MAPS Link: " + f"https://maps.google.com/?q={r['latitude']},{r['longitude']}", inline=False)
      embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
      await loading_message.delete()
      await ctx.send(embed=embed)

    except Exception as e:
      embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
      embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed3.add_field(name="Error:", value=f"{e}", inline=False)
      embed3.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed3)

@client.command(alises=["country-info", "country", "infocountry", "country-information"])
async def countryinfo(ctx, *, countrycodeig):
  # MAKE SURE TO ENTER THE COUNTRY CODE AND NOT THE COUNTRY NAME
  # eg- sg ( for Singapore ), us for ( United States )
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    rc = requests.get(f"https://api.worldbank.org/v2/country/{countrycodeig}?format=json").json()

    embed=discord.Embed(title="Country Information", color=0xff0000)
    embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/129850352-33345963-273b-42bf-b2bc-5523c8158229.png")
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
    await loading_message.delete()
    await ctx.send(embed=embed)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command(aliases=["mass-fake-profile", "massfakeprofile", "mass-fake-profiles", "massfakeprofiles"])
async def mfp(ctx, *, how_many):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
      fake_how_many = int(how_many)
      
      # This is the limit for this command to stop spamming!
      if fake_how_many <= 3:

        embed=discord.Embed(title="Mass Fake Profiles", color=0xff0000)
        embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        embed.add_field(name=f"{ctx.author.name} requested {how_many} fake profiles!", value=f"Starting to send {how_many} fake profiles!", inline=True)
        # embed.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed)

        for i in range(fake_how_many):
            fake = Faker()
            simple_dict = fake.profile()
            emf = discord.Embed(title="Fake Information Generator", color=0xF00000)
            emf.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
            emf.set_footer(text=f"Requested by {ctx.author.name}")
            emf.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
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
            await ctx.send(embed=emf)

      else:
        embed=discord.Embed(title="Mass Fake Profiles", color=0xff0000)
        embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed.set_thumbnail(url="https://www.nicepng.com/png/detail/214-2146883_4-fake-stamp-vector-fake-news-logo-png.png")
        embed.add_field(name="Error", value="Please enter a value below 30; This is done to prevent spam!", inline=True)
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    except Exception as e:
      embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
      embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed3.add_field(name="Error:", value=f"{e}", inline=False)
      embed3.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed3)

@client.command(aliases=["covidall"])
async def covid(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
  # This uses the official API provided by the Sri Lankan Government to gather the needed data
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
    
    em = discord.Embed(title="COVID-19 Stats Global - All Info", color=0xff0000)
    em.set_footer(text=f"Requested by {ctx.author.name}")
    em.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    em.set_thumbnail(url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
    em.add_field(name="Last Updated", value=update_date_time)
    em.add_field(name="New Cases", value=global_new_cases)
    em.add_field(name="Total Cases", value=global_total_cases)
    em.add_field(name="Total Deaths", value=global_deaths)
    em.add_field(name="New Deaths", value=global_new_deaths)
    em.add_field(name="Total Recovered", value=global_recovered)
    em.add_field(name="Total PCR Testing Count", value=total_pcr_testing_count)
    em.add_field(name="Total Antigen Testing Count", value=total_antigen_testing_count)
    await loading_message.delete()
    await ctx.send(embed=em)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def bitcoin(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)
  
  try:
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()

    usd = r['USD']
    eur = r['EUR']

    embed=discord.Embed(title="Bitcoin", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
    embed.add_field(name="USD", value=f"{usd}$", inline=False)
    embed.add_field(name="EUR", value=f"{eur}€", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)
    
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def eth(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()

    usd = r['USD']
    eur = r['EUR']

    embed=discord.Embed(title="Ethereum", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png")
    embed.add_field(name="USD", value=f"{usd}$", inline=False)
    embed.add_field(name="EUR", value=f"{eur}€", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx, *, questionhere):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text

    soup = BeautifulSoup(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text

    embed=discord.Embed(title="Would You Rather", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg")
    embed.add_field(name="Question", value=f"{questionhere}", inline=False)
    embed.add_field(name="Answer", value=f"{qa}\n{qor}\n{qb}", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def hastebin(ctx, *, message):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.post("https://hastebin.com/documents", data=message).json()

    try:
      embed=discord.Embed(title="Hastebin", color=0xff0000)
      embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png")
      embed.add_field(name="Link", value=f"https://hastebin.com/{r['key']}", inline=False)
      embed.add_field(name=f"Text by {ctx.author.name}", value=f"{message}", inline=False)
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed)
    
    except:
      embed=discord.Embed(title="Hastebin", color=0xff0000)
      embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png")
      embed.add_field(name="Link", value=f"https://hastebin.com/{r['key']}", inline=False)
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def xmr(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
    NegroPuket = r.json()

    eur = NegroPuket['EUR']
    usd = NegroPuket['USD']

    embed=discord.Embed(title="XMR", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879739662837633074/monero-logo-png-transparent.png")
    embed.add_field(name="USD", value=f"{usd}", inline=False)
    embed.add_field(name="EUR", value=f"{eur}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def doge(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
    NegroPuketDOGE = r.json()

    eur = NegroPuketDOGE['EUR']
    usd = NegroPuketDOGE['USD']

    embed=discord.Embed(title="Doge Coin", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879741979183968286/Dogecoin_Logo.png")
    embed.add_field(name="USD", value=f"{usd}", inline=False)
    embed.add_field(name="EUR", value=f"{eur}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def xrp(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
    kekistan = r.json()

    eur = kekistan['EUR']
    usd = kekistan['USD']

    embed=discord.Embed(title="Ripple", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879741815237017680/52.png")
    embed.add_field(name="USD", value=f"{usd}", inline=False)
    embed.add_field(name="EUR", value=f"{eur}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def goodnight(ctx):
  await ctx.message.delete()
  night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
  await ctx.send(night)

@client.command()
async def smile(ctx):
  await ctx.message.delete()
  smile = '˙ ͜ʟ˙'
  await ctx.send(smile)

@client.command()
async def iloveu(ctx):
  await ctx.message.delete()
  love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
  await ctx.send(love)

@client.command()
async def sword(ctx):
  await ctx.message.delete()
  sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
  await ctx.send(sword)

@client.command()
async def what(ctx):
  await ctx.message.delete()
  what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
  await ctx.send(what)

@client.command()
async def fuckyou(ctx):
  await ctx.message.delete()
  middlef = '╭∩╮(･◡･)╭∩╮'
  await ctx.send(middlef)

@client.command(aliases=["e_base64"])
async def e_b64(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    msg = base64.b64encode('{}'.format(args).encode('ascii'))
    enc = str(msg)
    enc = enc[2:len(enc)-1]

    embed=discord.Embed(title="to Base64", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg")
    embed.add_field(name="Query", value=f"{args}", inline=False)
    embed.add_field(name="Result", value=f"{enc}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def e_md5(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    msg = hashlib.md5(args.encode())
    slpake =  msg.hexdigest()

    embed=discord.Embed(title="to MD5", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879956672771137546/MD5.png")
    embed.add_field(name="Query", value=f"{args}", inline=False)
    embed.add_field(name="Result", value=f"{slpake}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def e_sha1(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    msg = hashlib.sha1(args.encode())
    slpuka =  msg.hexdigest()

    embed=discord.Embed(title="to SHA1", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879957622546108436/SHA1.png")
    embed.add_field(name="Query", value=f"{args}", inline=False)
    embed.add_field(name="Result", value=f"{slpuka}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def e_sha224(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    msg = hashlib.sha3_224(args.encode())
    crnja =  msg.hexdigest()

    embed=discord.Embed(title="to SHA224", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879958751640191046/download.png")
    embed.add_field(name="Query", value=f"{args}", inline=False)
    embed.add_field(name="Result", value=f"{crnja}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def e_sha512(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    msg = hashlib.sha3_512(args.encode())
    crnja =  msg.hexdigest()

    embed=discord.Embed(title="to SHA512", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879960296863698944/download_1.png")
    embed.add_field(name="Query", value=f"{args}", inline=False)
    embed.add_field(name="Result", value=f"{crnja}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command(aliases=["leet"])
async def e_leet(ctx, *, args):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    encoded = args.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')

    embed=discord.Embed(title="to LEET", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879961162895212574/download_2.png")
    embed.add_field(name="Query", value=f"{args}", inline=False)
    embed.add_field(name="Result", value=f"{encoded}", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command(aliases=["lyricsof"])
async def lyrics(ctx, *, search = None):
    loading_message = await ctx.send(embed=please_wait_emb)

    try:
        if not search:
            embed = discord.Embed(
                title = "No search argument!",
                description = "You havent entered anything, so i couldnt find lyrics!",
                color=0xff0000
            )
            embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            try:
                await loading_message.delete()
            except:
                pass
            return await ctx.send(embed = embed)
        
        song = urllib.parse.quote(search)
        
        async with aiohttp.ClientSession() as lyricsSession:
            async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: 
                if not 300 > jsondata.status >= 200: 
                    try:
                        await loading_message.delete()
                    except:
                        pass
                    return await ctx.send(f'Recieved poor status code of {jsondata.status}')
                lyricsData = await jsondata.json() 

        error = lyricsData.get('error')
        if error: 
            try:
                await loading_message.delete()
            except:
                pass
            return await ctx.send(f'Recieved unexpected error: {error}')

        songLyrics = lyricsData['lyrics'] 
        songArtist = lyricsData['author'] 
        songTitle = lyricsData['title'] 
        songThumbnail = lyricsData['thumbnail']['genius']
        
        for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace = False):
            embed = discord.Embed(
                title = f'{songTitle} - {songArtist}',
                description = chunk,
                color = 0xff0000
                # timestamp = datetime.datetime.utcnow()
            )
            embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
            embed.set_thumbnail(url = songThumbnail)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            try:
                await loading_message.delete()
            except:
                pass
            await ctx.send(embed = embed)

    except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)
    
@client.command(aliases=["generate-pwd", "gen-pwd", "generate-password", "gen-password", "newpassword", "password", "newpass", "passwordnew"])
async def genpwd(ctx, *, numberofcharacters=16):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    pwd_lenlis = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40)
    try:
      numberofcharsinint = int(numberofcharacters)

    except Exception as e:
      embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
      embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed3.add_field(name="Error:", value=f"{e}", inline=False)
      embed3.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed3)
      return
      
    if numberofcharsinint in pwd_lenlis:
      url = f"https://passwordinator.herokuapp.com/generate?num=true&char=true&caps=true&len={numberofcharacters}"
      r = requests.get(url)
      c = r.json()

      embed=discord.Embed(title="Password Generator", color=0xff0000)
      embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
      embed.add_field(name="Password Length", value=f"{numberofcharacters}", inline=False)
      embed.add_field(name="Password", value=f"{c['data']}", inline=False)
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed)

    else:
      embed=discord.Embed(title="Password Generator", description="An Error has occured!", color=0xff0000)
      embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
      embed.add_field(name="Error", value="The value of the number is high", inline=False)
      embed.add_field(name="Possible Fix", value="Enter a value below 40", inline=False)
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)

@client.command()
async def ig_pfp(ctx, *, ig_uname):
  loading_message = await ctx.send(embed=please_wait_emb)
  try:
    igpfp = instaloader.Instaloader()
    igpfp.download_profile(ig_uname, profile_pic_only=True)
    os.chdir(f'{ig_uname}')
    try:
      os.system("mv *.jpg ..")
    except:
      os.system("move *.jpg ..")
    os.chdir("..")
    try:
      os.system("mv *.jpg igtemp.jpg")
    except:
      os.system("ren *.jpg igtemp.jpg")
    try:
      os.system(f'rm -r {ig_uname}')
    except:
      os.system(f'DEL {ig_uname} /F/Q/S')


    file = discord.File(f'igtemp.jpg', filename="image.jpg")
    embed=discord.Embed(title="Instagram Profile Picture", description=f"of {ig_uname}", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.add_field(name="Link", value=f"https://instagram.com/{ig_uname}", inline=False)
    embed.set_image(url="attachment://image.jpg")
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(file=file, embed=embed)

    try:
      os.system(f"rm igtemp.jpg")
    except:
      os.remove(f'{ig_uname}')
  except Exception as e:
    await ctx.send(f"Error: {e}")

@client.command()
async def uptime(ctx):
  loading_message = await ctx.send(embed=please_wait_emb)

  try:
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed=discord.Embed(color=0xff0000)
    embed.add_field(name="The bot was online for: ", value=f":alarm_clock: {text}", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed)
  
  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")
    await loading_message.delete()
    await ctx.send(embed=embed3)


@client.command()
async def help(ctx):
    loading_message = await ctx.send(embed=please_wait_emb)
    bp = bot_prefix

    try:
        embed3=discord.Embed(title=":gear: Help", description="The list of all the commands! the might be some eastereggs!?! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.add_field(name="Crypto:", value=f"`{bp}bitcoin` - Get the bitcoin rates \n`{bp}doge` - Get the doge coin rates \n`{bp}xmr` - Get the Monero rates \n`{bp}xrp` - Get the ripple rates \n`{bp}eth` - Get the etherium rates", inline=False)
        embed3.add_field(name="Encoding", value=f"`{bp}e_b64 [value]` - Encode to Base64 \n`{bp}e_leet [value]` - Encode to leet \n`{bp}e_md5` - Encode to MD5 \n`{bp}e_sha1` - Encode to SHA1 \n`{bp}e_sha224` - Encode to SHA224 \n`{bp}e_sha512` - Encode to SHA512", inline=False)
        embed3.add_field(name="Fake Information", value=f"`{bp}fake help` - List out all the fake information commands! \n`{bp}fake high` - High amount fake information  \n`{bp}fake low` - Low amount of fake information \n`{bp}fake name` - Generate a Fake Name \n`{bp}fake dob` - Generate a Fake Date of Birth \n`{bp}fake addr` - Generate a Fake Address \n`{bp}fake job` - Generate a fake job \n`{bp}fake color` - Generate a fake color \n`{bp}fake zipcode` - Generate a fake zipcode \n`{bp}fake city` - Generate a fake city \n`{bp}fake licenseplate` - Generate a fake Lisence Plate \n`{bp}fake bban` - Generate a fake Basic Bank Account Number \n`{bp}fake iban` - Generate a fake International Bank Account \n`{bp}fake bs` - Generate a fake Bachelors \n`{bp}fake cc` - Generate a fake Credit Card \n`{bp}fake cemail` - Generate a fake company email \n`{bp}fake pno` - Generate a fake phone number \n`{bp}fake cp` - Generate a fake phone number \n`{bp}fake cp` - Generate a fake Catch Phrase \n`{bp}fake ssn` - Generate a fake Social Security Number", inline=False)
        # OLD MUSIC, COG
        # embed3.add_field(name="Music (BETA)", value=f"`{bp}play [song-name]` - Join to Voice Channel and play the song\n`{bp}join` - Join Voice Channel \n`{bp}leave` - Leave Voice Channel \n`{bp}skip` - Skip the current playing song and go to the next \n`{bp}summon [vc-name]` - Make the bot join to a VC (Case Sensitive) \n`{bp}now` - Displays the current playing song \n`{bp}queue` - Send the music queue waiting to be played! \n`{bp}shuffle` - Shuffle the queue \n`{bp}remove [index-from-queue]` - Remove a song from the queue \n`{bp}loop` - Loop the same song, use again to unloop", inline=False)
        
        # NEW MUSIC, LAVA LINK
        embed3.add_field(name="Music", value=f"`{bp}connect` - Connect to Voice Channel \n`{bp}disconnect` - Disconnect bot from Voice Channel \n`{bp}play [song-name/link]` - Play the song \n`{bp}skip` - Skip the currently playing song \n`{bp}pause` - Pause the music \n`{bp}resume` - Resume the music \n`{bp}seek [seconds]` - Skip the given seconds of the playing song \n`{bp}volume [number]` - Change the volume of the song \n`{bp}loop [type]` - Play music in a loop \n`{bp}nowplaying` - Show the song which is being played right now \n`{bp}queue` - Diplay the songs waiting to be played \n`{bp}equalizer` - Maybe tune the song to your liking?", inline=False)

        embed3.add_field(name="Others", value=f"`{bp}countryinfo [country_code]` - Search for Country Information \n`{bp}hastebin [text]` - Create a hatebin link for the given text \n`{bp}ig_pfp [ig_username]` - Download the Instgram profile picture \n`{bp}ip [ip_addr]` - Find Information of an IP Address \n`{bp}lyrics [song_name]` - Find lyrics of any song \n`{bp}mfp [number]` - Mass fake profile \n`{bp}pwdcheck [password]` - Check for the status of a password \n`{bp}uptime` - Show bot uptime \n ", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)

    except Exception as e:
        embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed3.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
        embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed3.add_field(name="Error:", value=f"{e}", inline=False)
        embed3.set_footer(text=f"Requested by {ctx.author.name}")
        await loading_message.delete()
        await ctx.send(embed=embed3)


# ERROR HANDLING //////////////////////////////////////////////////////////////////////////////////////////
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    await ctx.send(embed=embed)
    return

  if isinstance(error, commands.MissingRequiredArgument):
    embed=discord.Embed(title="Something is wrong!", description="An error has been occured!", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed.add_field(name="Error", value="You haven't passed the needed arguments for this command to run properly", inline=True)
    embed.add_field(name="Possible Fix", value=f"use `{bot_prefix}help all` to list out all the command and check the proper usage of the command you used", inline=True)
    await ctx.send(embed=embed)
    return


client.lava_nodes = [
  {
    'host':"lava.link",
    'port':80,
    'rest_uri':f'http://lava.link:80',
    'identifier':'MAIN',
    'password':'anything',
    'region':'singapore'
  }
]


# This is for user input sanitization
# Add more stuff here to make it better
blacklisted_letters_n_words = ("nc",
    "netcat", 
    "ncat",
    "apt",
    "snap",
    "remove",
    "uninstall",
    "{",
    "}",
    "<",
    ">",
    "/silent",
    "/verysilent",
    "grabify"
    )

@client.event
async def on_message(message):
  if client.user == message.author:
    return
  
  msg = message.content

  if msg.startswith(f'{bot_prefix}'):

    msgaftercmnd = msg.split(" ")[1:-1]

    messagesubcont = ""
    for messagesubcontlp in msgaftercmnd:
      messagesubcont += messagesubcontlp
    
    if messagesubcont in blacklisted_letters_n_words:
      embed=discord.Embed(title="Something is wrong!", description="Please enter the command with valid characters", color=0xff0000)
      embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed.add_field(name="Possible Fix", value=f"Dont have {blacklisted_letters_n_words} in your command!", inline=True)
      await message.send(embed=embed)
      return

  await client.process_commands(message)


keep_alive()

client.run(token)
