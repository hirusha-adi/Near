# load .env before everything
# ---
from dotenv import load_dotenv
load_dotenv()

# imports
# ---
import os
import asyncio
from datetime import datetime

import discord
from discord.ext import commands
from loguru import logger

from near.utils import embeds
from near.utils import errors
from near.database import dbfetch

# Setup Logging
# ---
log_dir = './logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S.log')
log_path = os.path.join(log_dir, log_filename)
logger.add(log_path, level="DEBUG", format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}", rotation="2 MB")


# Project Files Imports
# ---
from near.utils import texts
texts.welcome_message()

# main config
# ---
bot_prefix = dbfetch.SettingsMain.MESSAGE_PREFIX
bot_creator_name = dbfetch.SettingsMain.BOT_CREATOR_NAME
bot_current_version = dbfetch.SettingsMain.BOT_VERSION
bot_owner_id_or_dev_id = dbfetch.SettingsMain.DEV_ID

client = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all())

@client.tree.command(name="loadex", description="Load a Cog by its Extension")
async def loadex(interaction: discord.Interaction, extension: str):
    """
    Load a Cog by its Extension.

    Parameters
    ----------
    interaction: discord.Interaction
        Passed in automatically when the command is run.
    extension: str
        Extension of the Cog to be loaded.
    """

    logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
    try:
        if interaction.user.id == bot_owner_id_or_dev_id:
            await client.load_extension(f'near.cogs.{extension}')
            logger.info(f"Loaded near.cogs.{extension}")

            embed = await embeds.Common(
                client=client,
                interaction=interaction,
                title="Success :white_check_mark:",
                description=f"Loaded `near.cogs.{extension}`"
            )
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.PermissionError()
    except Exception as e:
        await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=client, error_message=f"{e}"), ephemeral=False)

@client.tree.command(name="unloadex", description="Unload a Cog by its Extension")
async def unloadex(interaction: discord.Interaction, extension: str):
    """
    Unload a Cog by its Extension.

    Parameters
    ----------
    interaction: discord.Interaction
        Passed in automatically when the command is run.
    extension: str
        Extension of the Cog to be unloaded.
    """

    logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
    try:
        if interaction.user.id == bot_owner_id_or_dev_id:
            await client.unload_extension(f'near.cogs.{extension}')
            logger.info(f"Unloaded near.cogs.{extension}")
            embed = await embeds.Common(
                client=client,
                interaction=interaction,
                title="Success :white_check_mark:",
                description=f"Unloaded `near.cogs.{extension}`",
            )
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.PermissionError()
    except Exception as e:
        await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=client, error_message=f"{e}"), ephemeral=False)


@client.tree.command(name="sync", description="Sync Commands Globally")
async def sync(interaction: discord.Interaction):
    """
    This command will sync all commands globally. It might take a while to sync all commands.

    Parameters
    ----------
    interaction: discord.Interaction
        Passed in automatically when the command is run.

    Raises:
        By client.tree.sync() ->
            HTTPException, CommandSyncFailure, Forbidden, MissingApplicationID, TranslationError
    """

    synced = await client.tree.sync()
    logger.debug(f"Synced: {synced}")
    logger.success(f'Synced {len(synced)} Slash Commands')
    logger.debug('Command tree synced.')


async def load_extensions():
    """
    Loads all cogs at startup.

    This function iterates through all the `.py` files in the `./near/cogs` directory and loads them as cogs.
    It prints a log message of the format "Loaded: near.cogs.<filename>" for each cog that is loaded.

    This function is called during the `on_ready` event of the bot.
    """
    
    for filename in os.listdir('./near/cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'near.cogs.{filename[:-3]}')
            logger.info(f"Loaded: near.cogs.{filename[:-3]}")


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
    """
    Called when a message is received by the bot.
    """
    # checks if the message was sent by the bot itself
    # if so, it does not process it
    if client.user == message.author:
        return

    msg = message.content

    # if the message mentions the bot
    # it replies the message and asks to use the `/help` command for more info.
    if message.mentions:
        for mentn in message.mentions:
            if mentn == client.user:
                await message.reply("Hey there! Use `/help` to get see a list of available commands.")

    # if the message starts with the bot prefix
    # checks if the command contains any blacklisted characters
    # sends an error message to the channel suggesting a possible fix
    if msg.startswith(f'{bot_prefix}'):

        msgaftercmnd = msg.split(" ")[1:-1]

        messagesubcont = ""
        for messagesubcontlp in msgaftercmnd:
            messagesubcont += messagesubcontlp

        if messagesubcont in blacklisted_letters_n_words:
            embed = discord.Embed(title="Something is wrong!", description="Please enter the command with valid characters", color=0xff0000)
            embed.set_author(name=f"{client.user.name}", icon_url=f"{client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.add_field(name="Possible Fix", value=f"Dont have {blacklisted_letters_n_words} in your command!", inline=True)
            await message.reply(embed=embed)
            return

    # finally, processes the command as normal
    await client.process_commands(message)


# Load stuff from the .env file
# ---
host = os.getenv("LAVA_HOST")
if not host:
    host = "lavalink" # or 127.0.0.1. Default to 'lavalink'
client.lavalink_host = host


# TODO: Fix this later
token = os.getenv("BOT_TOKEN")
# token = os.getenv("BOT_TOKEN") or "token.txt"
# if token == "token.txt":
# with open("token.txt", "r", encoding="utf-8") as tokenfile:
# token = tokenfile.read()


# Start the bot
# ---
async def start_bot():
    """
    Main entry point of the bot. Loads all extensions, then starts the bot with the given token.
    """
    async with client:
        await load_extensions()
        await client.start(token=token, reconnect=True)


if __name__ == "__main__":
    asyncio.run(start_bot())
