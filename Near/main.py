from keep_alive import keep_alive
import os
from password_strength import PasswordStats
import discord
from discord.ext import commands
import json
from near.database import get_main

bot_prefix = get_main.BotMainDB.MESSAGE_PREFIX
bot_creator_name = get_main.BotMainDB.BOT_CREATOR_NAME
bot_current_version = get_main.BotMainDB.BOT_VERSION
bot_owner_id_or_dev_id = get_main.BotMainDB.DEV_ID

token = get_main.BotMainDB.BOT_TOKEN
client = commands.Bot(command_prefix = bot_prefix)


@client.command()
async def loadex(ctx, extension):
  if ctx.author.id == bot_owner_id_or_dev_id:
    client.load_extension(f'cogs.{extension}')
    embed=discord.Embed(title="SUCCESS", description=f"`ADDED cogs.{extension} from NearBot`", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    await ctx.send(embed=embed)
    return
  else:
    embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
    embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    await ctx.send(embed=embed)
    return


@client.command()
async def unloadex(ctx, extension):
  if ctx.author.id == bot_owner_id_or_dev_id:
    try:
      client.unload_extension(f'cogs.{extension}')
      embed=discord.Embed(title="SUCCESS", description=f"`REMOVED cogs.{extension} from NearBot`", color=0xff0000)
      embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      await ctx.send(embed=embed)
      return
    except:
      embed=discord.Embed(title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
      embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      await ctx.send(embed=embed)
      return


# Loading all the cogs at startup
for filename in os.listdir('./near/cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'near.cogs.{filename[:-3]}')
    print(f"[+] Loaded: near.cogs.{filename[:-3]}")


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
client.load_extension('near.cogs.musicplayer')
print("[+] Loaded: near.cogs.musicplayer")


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
      embed.set_author(name="NearBot", icon_url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
      embed.add_field(name="Possible Fix", value=f"Dont have {blacklisted_letters_n_words} in your command!", inline=True)
      await message.send(embed=embed)
      return

  await client.process_commands(message)

keep_alive()
client.run(token)
