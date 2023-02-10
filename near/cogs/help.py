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
            discord.SelectOption(label="Crypto", emoji="🪙",
                                 description="Cryptocurrencies Related Commands"),
            discord.SelectOption(label="Encoding", emoji="🧾",
                                 description="Encoding and Hashing Related Commands"),
            discord.SelectOption(label="Fake Information", emoji="👨‍🦰",
                                 description="Fake Information Generating Commands"),
            discord.SelectOption(label="Texts", emoji="💬",
                                 description="Fun Text Commands"),
            discord.SelectOption(label="Fun", emoji="😆",
                                 description="Fun Commands"),
            discord.SelectOption(label="Music", emoji="🎵",
                                 description="Music Commands"),
            discord.SelectOption(label="Server Related", emoji="🔎",
                                 description="Server & User Information Related Commands"),
            discord.SelectOption(label="Others", emoji="🚨",
                                 description="Other Commands")
        ]
        super().__init__(placeholder="Select an option",
                         max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):

        option = self.values[0]

        embed = discord.Embed(
            title=":gear: Help",
            description="You can use the dropdown menu to navigate among the different categories of commands.",
            color=get_embeds.Common.COLOR
        )
        embed.set_author(
            name=f"NearBot",
            icon_url=f"https://cdn.discordapp.com/attachments/953475157605892099/1073516633798225980/Avatar.png"
        )

        if option == "Crypto":
            embed.add_field(
                name="/btc",
                value="Get the current Bitcoin Rates",
                inline=False
            )
            embed.add_field(
                name="/eth",
                value="Get the current Etherium Rates",
                inline=False
            )
            embed.add_field(
                name="/xmr",
                value="Get the current XMR Rates",
                inline=False
            )
            embed.add_field(
                name="/doge",
                value="Get the current Doge Coin Rates",
                inline=False
            )
            embed.add_field(
                name="/xrp",
                value="Get the current XRP Rates",
                inline=False
            )
            embed.add_field(
                name="/rvn",
                value="Get the current Raven Coin Rates",
                inline=False
            )

        elif option == "Encoding":
            embed.add_field(
                name="/b64",
                value="Encode to Base64",
                inline=False
            )
            embed.add_field(
                name="/md5",
                value="Get MD5 Hash",
                inline=False
            )
            embed.add_field(
                name="/sha1",
                value="Get SHA1 Hash",
                inline=False
            )
            embed.add_field(
                name="/sha224",
                value="Get SHA224 Hash",
                inline=False
            )
            embed.add_field(
                name="/sha512",
                value="Get SHA512 Hash",
                inline=False
            )
            embed.add_field(
                name="/leet",
                value="Convert text to L33T format",
                inline=False
            )

        elif option == "Fake Information":
            embed.add_field(
                name="/fake help",
                value="List out all the fake information commands - Theres a LOT!",
                inline=False
            )
            embed.add_field(
                name="/face [gender:optional='any']",
                value="Generate a fake face with a name",
                inline=False
            )
            embed.add_field(
                name="/fakeprofiles [amount:optional=3]",
                value="Generate a given number of fake profiles",
                inline=False
            )
            embed.add_field(
                name="/discordtoken",
                value="Generate a fake discord token",
                inline=False
            )

        await interaction.response.send_message(embed=embed, ephemeral=True)


class SelectView(discord.ui.View):
    def __init__(self, *, timeout=60):
        super().__init__(timeout=timeout)
        self.add_item(Select())


class Help(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # For custom help
        self.client.remove_command('help')

    @app_commands.command(name="help", description="Command Support")
    async def help(self, interaction: discord.Interaction):

        bp = "/"

        try:
            embed3 = discord.Embed(
                title=":gear: Help", description="The list of all the commands! there might be some eastereggs!?! ", color=get_embeds.Common.COLOR)
            embed3.set_author(
                name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
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

            embed3.add_field(
                name="Server Related", value=f"`{bp}av [@user or id]` - Get the profile picture of any user \n`{bp}serverinfo` - Show all publicly available information about the server \n`{bp}userinfo` - Show all the publicly available information about a user", inline=False)

            embed3.add_field(name="Others", value=f"`{bp}countryinfo [country_code]` - Search for Country Information \n`{bp}hastebin [text]` - Create a hatebin link for the given text \n`{bp}insta [ig_username]` - Download the Instgram profile picture \n`{bp}ip [ip_addr]` - Find Information of an IP Address \n`{bp}lyrics [song_name]` - Find lyrics of any song \n`{bp}mfp [number]` - Mass fake profile \n`{bp}pwdcheck [password]` - Check for the status of a password \n`{bp}uptime` - Show bot uptime \n ", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3, view=SelectView(), ephemeral=True)

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
    await client.add_cog(Help(client))
