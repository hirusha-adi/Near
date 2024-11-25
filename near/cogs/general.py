import os
from datetime import timedelta as dttimedelta
from platform import python_version as cur_python_version
from time import time as nowtime

import discord
from discord import app_commands
from discord.ext import commands
from loguru import logger

from near.database.defaults import set_defaults
from near.utils import embeds
from near.utils import log


class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Administration", emoji="💥", description="Administration commands"),
            discord.SelectOption(label="Crypto", emoji="🪙", description="Cryptocurrencies Related Commands"),
            discord.SelectOption(label="Encoding", emoji="🧾", description="Encoding and Hashing Related Commands"),
            discord.SelectOption(label="Fake Information", emoji="👨‍🦰", description="Fake Information Generating Commands"),
            discord.SelectOption(label="Fun", emoji="😆", description="Fun Commands"),
            discord.SelectOption(label="General", emoji="🧸", description="General commands"),
            discord.SelectOption(label="Information Gathering", emoji="🔍", description="Information Gathering Related Commands"),
            discord.SelectOption(label="Music", emoji="🎵", description="Music Commands"),
            discord.SelectOption(label="Tools", emoji="🛠️", description="Important tools to get stuff done"),
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
            description="To access the complete list of commands and their respective descriptions, kindly select a category from the drop-down menu. For additional information and a comprehensive list of commands, please visit our website at https://teamsds.net/nearbot"
        )

        thumbnails = {
            "Administration": "https://cdn.discordapp.com/attachments/1278527700482527273/1278527720132968458/admin-3d-illustration-icon-png.png",
            "Crypto": "https://cdn.discordapp.com/attachments/940889393974104084/1073538553335783454/7047060.png",
            "Encoding": "https://cdn.discordapp.com/attachments/940889393974104084/1073538746806444103/2362335.png",
            "Fake Information": "https://cdn.discordapp.com/attachments/940889393974104084/1073538885986033704/4410174.png",
            "Fun": "https://cdn.discordapp.com/attachments/940889393974104084/1073539343597174794/funny-icon-7.png",
            "General": "https://cdn.discordapp.com/attachments/940889393974104084/1073539659596058685/stuff-icon-2.png",
            "Information Gathering": "https://cdn.discordapp.com/attachments/940889393974104084/1073539896892981279/search-flat.png",
            "Music": "https://cdn.discordapp.com/attachments/940889393974104084/1073540069186600960/3844724.png",
            "Tools": "https://cdn.discordapp.com/attachments/940889393974104084/1073540361240186883/768px-Circle-icons-tools.png"
        }
        
        commands = {
            "Administration": [
                ("/move", "Move users from one voice channel to another"),
            ],
            "Crypto": [
                ("/btc", "Get the current Bitcoin Rates"),
                ("/eth", "Get the current Etherium Rates"),
                ("/xmr", "Get the current XMR Rates"),
                ("/doge", "Get the current Doge Coin Rates"),
                ("/xrp", "Get the current XRP Rates"),
                ("/rvn", "Get the current Raven Coin Rates")
            ],
            "Encoding": [
                ("/b64encode", "Encode to Base64"),
                ("/b64decode", "Decode from Base64"),
                ("/md5", "Get MD5 Hash"),
                ("/sha1", "Get SHA1 Hash"),
                ("/sha224", "Get SHA224 Hash"),
                ("/sha512", "Get SHA512 Hash"),
                ("/leet", "Convert text to L33T format")
            ],
            "Fake Information": [
                ("/fake", "List out all the fake information commands - Theres a LOT!"),
                ("/fakeprofiles", "Generate a given number of fake profiles"),
            ],
            "Fun": [
                ("/inspire", "List out all the fake information commands - Theres a LOT!"),
                ("/meme", "Get a random meme"),
                ("/dadjoke", "Get a random dad joke"),
                ("/joke", "Get a random joke"),
                ("/wyr", "Would You Rather...?"),
                ("/advice", "Get advice for your life")
            ],
            "General": [
                ("/ping", "Check the response time of the Discord Bot"),
                ("/uptime", "How long has the bot been up for?"),
                ("/clean", "Amount of messages to Delete")
            ],
            "Information Gathering": [
                ("/ipinfo", "IP Address Lookup"),
                ("/avatar", "Get the User Avatar"),
                ("/serverinfo", "Get Information about the Server"),
                ("/userinfo", "User to get the Information of. Defaults to the Author")
            ],
            "Music": [
                ("/lyrics", "Search the Lyrics of any Song"),
                ("--join", "Join a Voice Channel"),
                ("--leave", "Leave the Voice Channel"),
                ("--play", "Play the song"),
                ("--skip", "Skip the currently playing song"),
                ("--pause", "Pause the music"),
                ("--resume", "Resume the music"),
                ("--shuffle", "Shuffle the pending music list"),
                ("--volume <vol>", "Change the volume of the song")
            ],
            "Tools": [
                ("/passwordgen", "Generate a very secure and unique password"),
                ("/passwordchk", "Password Strength Check and Profiler"),
                ("/insta", "Grab the Instagram Profile Picture of a Profile"),
                ("/bin", "Create a PrivateBin from a Text")
            ]
        }
        
        if option in commands:
            embed.set_thumbnail(url=thumbnails[option])
            for name, value in commands[option]:
                embed.add_field(name=name, value=value, inline=False)

        # works as intended, but gives this error: "This interaction failed" after some time
        await interaction.message.edit(embed=embed)

        # Sends message everytime an option is selected. Bad idea, but no bugged Error
        # await interaction.response.send_message(embed=embed, ephemeral=True)


class SelectView(discord.ui.View):
    def __init__(self, *, timeout=60):
        super().__init__(timeout=timeout)
        self.add_item(Select())


class General(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # For custom help
        self.client.remove_command('help')

        # Bot uptime
        self.start_time = None

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f'Logged in as {self.client.user.name}')
        logger.info(f'Discord.py API version: {discord.__version__}')
        logger.info(f'Python version: {cur_python_version()}')
        
        self.start_time = nowtime()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"teamsds.net/discord"))

        # commands tree
        _tmp_filecheck = ".DO_NOT_DELETE.txt"
        if not os.path.isfile(_tmp_filecheck):
            synced = await self.client.tree.sync()
            logger.debug(f"Synced: {[(str(item.name)+'-'+str(item.id)) for item in synced]}")
            logger.success(f'Synced {len(synced)} Slash Commands')
            with open(_tmp_filecheck, 'w') as _file:
                _file.write("Deleting this file and restarting the bot \nwill make the bot register its command tree\nonce again")

        # init orm
        # await connect_db()
        await set_defaults()
        
        logger.success('Bot is ready!')
    
    # @commands.Cog.listener()
    # async def on_disconnect():
    #     await Tortoise.close_connections()
    #     logger.info("Tortoise-ORM connection closed.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error) -> None:
        if isinstance(error, commands.MissingPermissions) or isinstance(error, commands.CheckFailure):
            await ctx.send(embed=await embeds.Error(interaction=ctx, client=self.client, error_message=f"You don't have the necessary permissions required to use this command!"), ephemeral=False)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=await embeds.Error(interaction=ctx, client=self.client, error_message=f"You haven't passed the needed arguments for this command to run properly.\n\nPlease use `/help` to list out all the command and check the proper usage of the command you used."), ephemeral=False)

            
    @app_commands.command(name="ping", description="Check the response time of the Discord Bot")
    async def ping(self, interaction: discord.Interaction):
        await log.log_command_history(command="/ping", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title=f":timer:  Response Time: {round(self.client.latency * 1000)} ms",
                thumbnail="general_ping"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="uptime", description="How long has the bot been up for?")
    async def uptime(self, interaction: discord.Interaction):
        await log.log_command_history(command="/uptime", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            current_time = nowtime()
            difference = int(round(current_time - self.start_time))
            text = str(dttimedelta(seconds=difference))
            
            embed = await embeds.Common(
                client=self.client,
                interaction=interaction,
                title=f":clock: Uptime: {text}",
                thumbnail="general_uptime"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="clean", description="Delete messages sent by the Bot")
    @app_commands.describe(amount="Amount of messages to Delete")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clean(self, interaction: discord.Interaction, amount: int):
        await log.log_command_history(command="/clean", command_args=f"amount: {amount}", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        # input sanitization not needed here
        try:
            if amount <= 100:

                amttdel = amount + 1
                await interaction.channel.purge(limit=amttdel, check=lambda m: m.author == self.client.user)

                msgtxt = "message" if amount == "1" else "messages"

                embed = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title=f"Success!",
                    thumbnail="general_clean"
                )
                embed.add_field(name="Action", value=f"Deleted {amount} {msgtxt} sent by {self.client.user.name}!", inline=False)
                await interaction.response.send_message(embed=embed, ephemeral=True)

            else:
                await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"Please enter a value below 100!"), ephemeral=False)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="help", description="Command Support")
    async def help(self, interaction: discord.Interaction):
        await log.log_command_history(command="/help", command_args="", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title=":gear: A Guide to All Available Commands :gear:",
                description="To access the complete list of commands and their respective descriptions, kindly select a category from the drop-down menu. For additional information and a comprehensive list of commands, please visit our website at https://teamsds.net/nearbot",
                thumbnail="general_help"
            )
            await interaction.response.send_message(embed=embed, view=SelectView(), ephemeral=False)

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(General(client))
