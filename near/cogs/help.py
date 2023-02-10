from datetime import timedelta as dttimedelta
from platform import python_version as cur_python_version
from time import time as nowtime

import discord
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds, get_main


class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Option 1", emoji="👌",
                                 description="This is option 1!"),
            discord.SelectOption(label="Option 2", emoji="✨",
                                 description="This is option 2!"),
            discord.SelectOption(label="Option 3", emoji="🎭",
                                 description="This is option 3!")
        ]
        super().__init__(placeholder="Select an option",
                         max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"Your choice is {self.values[0]}!", ephemeral=True)


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

    @app_commands.command(name="help", description="Command Support")
    async def help(self, interaction: discord.Interaction):

        bp = "/"

        try:
            embed3 = discord.Embed(
                title=":gear: Help", description="The list of all the commands! there might be some eastereggs!?! ", color=get_embeds.Common.COLOR)
            embed3.set_author(
                name=f"{self.client.user.name}", icon_url=f"{self.client.user.default_avatar.url}")
            embed3.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
            embed3.add_field(
                name="Crypto:", value=f"`{bp}bitcoin` - Get the bitcoin rates \n`{bp}doge` - Get the doge coin rates \n`{bp}xmr` - Get the Monero rates \n`{bp}xrp` - Get the ripple rates \n`{bp}eth` - Get the etherium rates \n`{bp}rvn` - Get raven coin rates and additional information", inline=False)
            embed3.add_field(
                name="Encoding", value=f"`{bp}e_b64 [value]` - Encode to Base64 \n`{bp}e_leet [value]` - Encode to leet \n`{bp}e_md5` - Encode to MD5 \n`{bp}e_sha1` - Encode to SHA1 \n`{bp}e_sha224` - Encode to SHA224 \n`{bp}e_sha512` - Encode to SHA512", inline=False)
            embed3.add_field(name="Fun", value=f"`{bp}inspire` - Send you an inspirational quote! \n`{bp}bored` - Get some activity to do \n`{bp}meme` - Get a meme to laught ats \n`{bp}dadjoke` - just a Dad Joke \n`{bp}joke` - Laughing is the best medicing \n`{bp}joke2` - Jokes are awesome! \n`{bp}wyr`- Would you rather? \n`{bp}advice` - Advice makes our lives better", inline=False)
            embed3.add_field(
                name="Fake Information", value=f"`{bp}fake help` - List out all the fake information commands! \n`{bp}face [gender:optional]` - Generate a fake face with a name", inline=False)

            embed3.add_field(
                name="Music", value=f"`{bp}connect` - Connect to Voice Channel \n`{bp}disconnect` - Disconnect bot from Voice Channel \n`{bp}play [song-name/link]` - Play the song \n`{bp}skip` - Skip the currently playing song \n`{bp}pause` - Pause the music \n`{bp}resume` - Resume the music \n`{bp}seek [seconds]` - Skip the given seconds of the playing song \n`{bp}volume [number]` - Change the volume of the song \n`{bp}loop [type]` - Play music in a loop \n`{bp}nowplaying` - Show the song which is being played right now \n`{bp}queue` - Diplay the songs waiting to be played \n`{bp}equalizer` - Maybe tune the song to your liking?", inline=False)

            try:
                if interaction.user.guild_permissions.manage_messages:
                    embed3.add_field(
                        name="Manage", value=f"`{bp}clean [number_of_messages]` - Delete the given number of messages sent by the bot", inline=False)
            except:
                pass

            try:
                if interaction.user.id in get_main.BotMainDB.DEV_AND_OWNERS:
                    embed3.add_field(
                        name="Server Related", value=f"`{bp}av [@user or id]` - Get the profile picture of any user \n`{bp}serverinfo` - Show all publicly available information about the server \n`{bp}userinfo` - Show all the publicly available information about a user", inline=False)
            except:
                pass

            embed3.add_field(name="Others", value=f"`{bp}countryinfo [country_code]` - Search for Country Information \n`{bp}hastebin [text]` - Create a hatebin link for the given text \n`{bp}insta [ig_username]` - Download the Instgram profile picture \n`{bp}ip [ip_addr]` - Find Information of an IP Address \n`{bp}lyrics [song_name]` - Find lyrics of any song \n`{bp}mfp [number]` - Mass fake profile \n`{bp}pwdcheck [password]` - Check for the status of a password \n`{bp}uptime` - Show bot uptime \n ", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3, view=SelectView())

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.default_avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3, ephemeral=True)


async def setup(client: commands.Bot):
    await client.add_cog(General(client))
