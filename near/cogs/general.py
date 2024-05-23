from datetime import timedelta as dttimedelta
from platform import python_version as cur_python_version
from time import time as nowtime
import os
import discord
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds
from near.utils import embeds


class Select(discord.ui.Select):
    def __init__(self):
        options = [
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

        embed = discord.Embed(title=":gear: A Guide to All Available Commands :gear:", description="To access the complete list of commands and their respective descriptions, kindly select a category from the drop-down menu. For additional information and a comprehensive list of commands, please visit our website at https://teamsds.net/nearbot", color=get_embeds.Common.COLOR)
        embed.set_author(name=f"NearBot", icon_url=f"https://cdn.discordapp.com/attachments/953475157605892099/1073516633798225980/Avatar.png")
        embed.set_footer(text=f"Requested by {interaction.user.name}")

        if option == "Crypto":
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073538553335783454/7047060.png")
            embed.add_field(name="/btc", value="Get the current Bitcoin Rates", inline=False)
            embed.add_field(name="/eth", value="Get the current Etherium Rates", inline=False)
            embed.add_field(name="/xmr", value="Get the current XMR Rates", inline=False)
            embed.add_field(name="/doge", value="Get the current Doge Coin Rates", inline=False)
            embed.add_field(name="/xrp", value="Get the current XRP Rates", inline=False)
            embed.add_field(name="/rvn", value="Get the current Raven Coin Rates", inline=False)

        elif option == "Encoding":
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073538746806444103/2362335.png")
            embed.add_field(name="/b64encode", value="Encode to Base64", inline=False)
            embed.add_field(name="/b64decode", value="Decode from Base64", inline=False)
            embed.add_field(name="/md5", value="Get MD5 Hash", inline=False)
            embed.add_field(name="/sha1", value="Get SHA1 Hash", inline=False)
            embed.add_field(name="/sha224", value="Get SHA224 Hash", inline=False)
            embed.add_field(name="/sha512", value="Get SHA512 Hash", inline=False)
            embed.add_field(name="/leet", value="Convert text to L33T format", inline=False)

        elif option == "Fake Information":
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073538885986033704/4410174.png")
            embed.add_field(name="/fake", value="List out all the fake information commands - Theres a LOT!", inline=False)
            embed.add_field(name="/face", value="Generate a fake face with a name", inline=False)
            embed.add_field(name="/fakeprofiles", value="Generate a given number of fake profiles", inline=False)
            embed.add_field(name="/discordtoken", value="Generate a fake discord token", inline=False)

        elif option == "Fun":
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073539343597174794/funny-icon-7.png")
            embed.add_field(name="/inspire", value="List out all the fake information commands - Theres a LOT!", inline=False)
            embed.add_field(name="/bored", value="Bored? What to do now?", inline=False)
            embed.add_field(name="/meme", value="Get a random meme", inline=False)
            embed.add_field(name="/dadjoke", value="Get a random dad joke", inline=False)
            embed.add_field(name="/joke", value="Get a random joke", inline=False)
            embed.add_field(name="/joke2", value="Get a Joke, but from Another API", inline=False)
            embed.add_field(name="/wyr", value="Would You Rather...?", inline=False)
            embed.add_field(name="/advice", value="Get advice for your life", inline=False)

        elif option == "General":
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073539659596058685/stuff-icon-2.png")
            embed.add_field(name="/ping", value="Check the response time of the Discord Bot", inline=False)
            embed.add_field(name="/uptime", value="How long has the bot been up for?", inline=False)
            embed.add_field(name="/clean", value="Amount of messages to Delete", inline=False)

        elif option == "Information Gathering":
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073539896892981279/search-flat.png")
            embed.add_field(name="/ipinfo", value="IP Address Lookup", inline=False)
            embed.add_field(name="/countryinfo", value="Country Information Lookup", inline=False)
            embed.add_field(name="/covid", value="Global Covid-19 Statistics", inline=False)
            embed.add_field(name="/avatar", value="Get the User Avatar", inline=False)
            embed.add_field(name="/serverinfo", value="Get Information about the Server", inline=False)
            embed.add_field(name="/userinfo", value="User to get the Information of. Defaults to the Author", inline=False)

        elif option == "Music":
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073540069186600960/3844724.png")
            embed.add_field(name="--lyrics", value="Search the Lyrics of any Song", inline=False)
            embed.add_field(name="--join", value="Join a Voice Channel", inline=False)
            embed.add_field(name="--leave", value="Leave the Voice Channel", inline=False)
            embed.add_field(name="--play", value="Play the song", inline=False)
            embed.add_field(name="--skip", value="Skip the currently playing song", inline=False)
            embed.add_field(name="--pause", value="Pause the music", inline=False)
            embed.add_field(name="--resume", value="Resume the music", inline=False)
            embed.add_field(name="--shuffle", value="Shuffle the pending music list", inline=False)
            embed.add_field(name="--volume <vol>", value="Change the volume of the song", inline=False)

        elif option == "Tools":
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073540361240186883/768px-Circle-icons-tools.png")
            embed.add_field(name="/passwordgen", value="Generate a very secure and unique password", inline=False)
            embed.add_field(name="/passwordchk", value="Password Strength Check and Profiler", inline=False)
            embed.add_field(name="/insta", value="Grab the Instagram Profile Picture of a Profile", inline=False)
            embed.add_field(name="/bin", value="Create a PrivateBin from a Text", inline=False)

        # works as intended, but gives this error: "This interaction failed"
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
        print(f'Logged in as {self.client.user.name}')
        print(f'Discord.py API version: {discord.__version__}')
        print(f'Python version: {cur_python_version()}')
        self.start_time = nowtime()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"teamsds.net/discord"))

        _tmp_filecheck = ".DO_NOT_DELETE.txt"
        if not os.path.isfile(_tmp_filecheck):
            synced = await self.client.tree.sync()
            print(synced)
            print(f'Synced {len(synced)} Slash Commands')
            with open(_tmp_filecheck, 'w') as _file:
                _file.write("Deleting this file and restarting the bot \nwill make the bot register its command tree\nonce again")

        print('Bot is ready!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=embeds.Error(interaction=ctx, client=self.client, error_message=f"You don't have the permissions required to use this command!"), ephemeral=False)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embeds.Error(interaction=ctx, client=self.client, error_message=f"You haven't passed the needed arguments for this command to run properly.\n\nPlease use `/help` to list out all the command and check the proper usage of the command you used."), ephemeral=False)

    @app_commands.command(name="ping", description="Check the response time of the Discord Bot")
    async def ping(self, interaction: discord.Interaction):
        try:
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title=":timer:  Response Time  :timer:",
                description=f"**{round(self.client.latency * 1000)} ms**",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png"
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="uptime", description="How long has the bot been up for?")
    async def uptime(self, interaction: discord.Interaction):
        try:
            current_time = nowtime()
            difference = int(round(current_time - self.start_time))
            text = str(dttimedelta(seconds=difference))
            embed = discord.Embed(color=get_embeds.Common.COLOR, title=f":clock: Uptime of {self.client.user.name} :clock:", description=f'**{text}**')
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="clean", description="Delete messages sent by the Bot")
    @app_commands.describe(amount="Amount of messages to Delete")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clean(self, interaction: discord.Interaction, amount: int):
        # input sanitization not needed here
        try:
            if amount <= 100:

                amttdel = amount + 1
                await interaction.channel.purge(limit=amttdel, check=lambda m: m.author == self.client.user)

                msgtxt = "message" if amount == "1" else "messages"

                embed = discord.Embed(title="Success!", color=get_embeds.Common.COLOR)
                embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
                embed.add_field(name="Action", value=f"Deleted {amount} {msgtxt} sent by {self.client.user.name}!", inline=False)
                embed.set_footer(text=f"Requested by {interaction.user.name}")
                await interaction.response.send_message(embed=embed, ephemeral=True)

            else:
                await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"Please enter a value below 100!"), ephemeral=False)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="help", description="Command Support")
    async def help(self, interaction: discord.Interaction):

        try:
            embed3 = discord.Embed(
                title=":gear: A Guide to All Available Commands :gear:",
                description="To access the complete list of commands and their respective descriptions, kindly select a category from the drop-down menu. For additional information and a comprehensive list of commands, please visit our website at https://teamsds.net/nearbot",
                color=get_embeds.Common.COLOR
            )
            embed3.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073537396982952016/868681.png")
            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3, view=SelectView(), ephemeral=False)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(General(client))
