# load .env before everything
# ---
from dotenv import load_dotenv
load_dotenv()

# imports
# ---
import os
import asyncio

import discord
from discord.ext import commands

from database.settings import dbget_mainSettings

# main config
# ---
main_config = dbget_mainSettings()
bot_prefix = main_config['bot_prefix']
bot_creator_name = main_config['bot_creator_name']
bot_current_version = main_config['bot_current_version']
bot_owner_id_or_dev_id = main_config['bot_owner_id_or_dev_id']

client = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all())

@client.tree.command(name="loadex", description="Load a Cog by its Extension")
async def loadex(interaction: discord.Interaction, extension: str):
    if interaction.user.id == bot_owner_id_or_dev_id:
        try:
            await client.load_extension(f'cogs.{extension}')
            embed = discord.Embed(
                title="SUCCESS", description=f"`ADDED cogs.{extension} from NearBot`", color=0xff0000)
            embed.set_author(name=f"{client.user.name}",
                             icon_url=f"{client.user.avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="ERROR", description=f"```{e}```", color=0xff0000)
            embed.set_author(name=f"{client.user.name}",
                             icon_url=f"{client.user.avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(
            title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
        embed.set_author(name=f"{client.user.name}",
                         icon_url=f"{client.user.avatar.url}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        await interaction.response.send_message(embed=embed, ephemeral=True)


@client.tree.command(name="unloadex", description="Unload a Cog by its Extension")
async def unloadex(interaction: discord.Interaction, extension: str):
    if interaction.user.id == bot_owner_id_or_dev_id:
        try:
            await client.unload_extension(f'cogs.{extension}')
            embed = discord.Embed(
                title="SUCCESS", description=f"`REMOVED cogs.{extension} from NearBot`", color=0xff0000)
            embed.set_author(name=f"{client.user.name}",
                             icon_url=f"{client.user.avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="ERROR", description=f"```{e}```", color=0xff0000)
            embed.set_author(name=f"{client.user.name}",
                             icon_url=f"{client.user.avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(
            title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
        embed.set_author(name=f"{client.user.name}",
                         icon_url=f"{client.user.avatar.url}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        await interaction.response.send_message(embed=embed, ephemeral=True)


@client.tree.command(name="sync", description="Sync Commands Globally")
async def sync(interaction: discord.Interaction):
    synced = await client.tree.sync()
    print(synced)
    print(f'Synced {len(synced)} Slash Commands')
    print('Command tree synced.')


# Loading all the cogs at startup
async def load_extensions():
    for filename in os.listdir('./near/cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'near.cogs.{filename[:-3]}')
            print(f"[+] Loaded: near.cogs.{filename[:-3]}")


host = os.getenv("LAVA_HOST")
if not host:
    host = "0.0.0.0"
client.lavalink_host = host

# This is for user input sanitization
# Add more stuff here to make it better
blacklisted_letters_n_words = (
    # Full grabify link detection
    "grabify.link", "partpicker.shop", "websafe.online", "sportshub.bar", "herald.sbs", "locations.quest", "leancoding.co"
    "lovebird.guru", "trulove.guru", "dateing.club", "shrekis.life", "headshot.monster", "gaming-at-my.best", "stopify.co",
    "progaming.monster", "yourmy.monster", "imageshare.best", "screenshot.best", "gamingfun.me", "catsnthing.com",
    "catsnthings.fun", "curiouscat.club", "joinmy.site", "fortnitechat.site", "fortnight.space", "freegiftcards.co",

    # Others
    "nc", "netcat", "ncat", "apt", "snap", "remove", "uninstall", "{", "}", "<", ">", "/silent", "/verysilent", "python -c", "python3 -c"
)


@client.event
async def on_message(message: discord.message.Message):
    if client.user == message.author:
        return

    msg = message.content

    if message.mentions:
        for mentn in message.mentions:
            if mentn == client.user:
                await message.reply("Hey there! The bot now supports slash commands. Enter `/help` to get started")

    if msg.startswith(f'{bot_prefix}'):

        msgaftercmnd = msg.split(" ")[1:-1]

        messagesubcont = ""
        for messagesubcontlp in msgaftercmnd:
            messagesubcont += messagesubcontlp

        if messagesubcont in blacklisted_letters_n_words:
            embed = discord.Embed(
                title="Something is wrong!", description="Please enter the command with valid characters", color=0xff0000)
            embed.set_author(
                name=f"{client.user.name}", icon_url=f"{client.user.avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.add_field(
                name="Possible Fix", value=f"Dont have {blacklisted_letters_n_words} in your command!", inline=True)
            await message.reply(embed=embed)
            return

    await client.process_commands(message)

token = os.getenv("BOT_TOKEN")
if not token:
    with open("token.txt", "r", encoding="utf-8") as tokenfile:
        token = tokenfile.read()


async def main():
    async with client:
        await load_extensions()
        await client.start(token=token, reconnect=True)


asyncio.run(main())
