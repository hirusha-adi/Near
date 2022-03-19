from datetime import timedelta as dttimedelta
from platform import python_version as cur_python_version
from time import time as nowtime

import discord
from discord.ext import commands
from flask import message_flashed
from near.database import get_embeds, get_main


class General(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.delete_messages_log_servers = [953475156309856256]
        self.msg_log_channel = 954566295171502120

        self.client = client

        # For custom help
        self.client.remove_command('help')

        # Bot uptime
        self.start_time = None

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=get_embeds.PleaseWait.AUTHOR_NAME, icon_url=get_embeds.PleaseWait.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.client.user.name}')
        print(f'Discord.py API version: {discord.__version__}')
        print(f'Python version: {cur_python_version()}')
        self.start_time = nowtime()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"teamsds.net/discord"))
        print('Bot is ready!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="ERROR", description="`You don't have the permissions required to use this command!`", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await ctx.send(embed=embed)
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Something is wrong!", description="An error has been occured!", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.add_field(
                name="Error", value="You haven't passed the needed arguments for this command to run properly", inline=True)
            embed.add_field(
                # name="Possible Fix", value=f"use `{get_main.BotMainDB.MESSAGE_PREFIX}help all` to list out all the command and check the proper usage of the command you used", inline=True)
                name="Possible Fix", value=f"use `{self.client.get_prefix}help all` to list out all the command and check the proper usage of the command you used", inline=True)
            await ctx.send(embed=embed)
            return

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild.id in self.delete_messages_log_servers:
            channel = self.client.get_channel(self.msg_log_channel)
            embed = discord.Embed(title=f"Message deleted in <#{message.channel.id}>",
                                  color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.add_field(name=f"Sent by",
                            value=f"{message.author}", inline=False)
            embed.add_field(name=f"Content",
                            value=f"{message}", inline=False)
            await channel.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            embed = discord.Embed(title="Response Time",
                                  color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
            embed.add_field(
                name=f"Ping :timer:", value=f"{round(self.client.latency * 1000)} ms", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command()
    async def uptime(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            current_time = nowtime()
            difference = int(round(current_time - self.start_time))
            text = str(dttimedelta(seconds=difference))
            embed = discord.Embed(color=get_embeds.Common.COLOR)
            embed.add_field(name="The bot was online for: ",
                            value=f":alarm_clock: {text}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clean(self, ctx, amount=5):
        """
        Delete messages sent by the bot itself to the message channel
        You need have the "manage_messages" permission to use this command
        """
        try:
            if amount <= 100:
                amttdel = amount + 1
                await ctx.channel.purge(limit=amttdel, check=lambda m: m.author == self.client.user)

                if amount == "1":
                    msgtxt = "message"
                else:
                    msgtxt = "messages"

                embed = discord.Embed(
                    title="Success!", color=get_embeds.Common.COLOR)
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar_url}")
                embed.add_field(
                    name="Action", value=f"Deleted {amount} {msgtxt} sent by {self.client.user.name}!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed, delete_after=4)

            else:
                embed2 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                       description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed2.set_author(name=f"{self.client.user.name}",
                                  icon_url=f"{self.client.user.avatar_url}")
                embed2.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(
                    name="Error:", value=f"Please enter a value below 100!", inline=False)
                embed2.set_footer(text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed2)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed3)

    @commands.command()
    async def help(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        bp = get_main.BotMainDB.MESSAGE_PREFIX

        try:
            embed3 = discord.Embed(
                title=":gear: Help", description="The list of all the commands! the might be some eastereggs!?! ", color=get_embeds.Common.COLOR)
            embed3.set_author(
                name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar_url}")
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
                if ctx.message.author.guild_permissions.manage_messages:
                    embed3.add_field(
                        name="Manage", value=f"`{bp}clean [number_of_messages]` - Delete the given number of messages sent by the bot", inline=False)
            except:
                pass

            try:
                if ctx.author.id in get_main.BotMainDB.DEV_AND_OWNERS:
                    embed3.add_field(
                        name="Server Related", value=f"`{bp}av [@user or id]` - Get the profile picture of any user \n`{bp}serverinfo` - Show all publicly available information about the server \n`{bp}userinfo` - Show all the publicly available information about a user", inline=False)
            except:
                pass

            embed3.add_field(name="Others", value=f"`{bp}countryinfo [country_code]` - Search for Country Information \n`{bp}hastebin [text]` - Create a hatebin link for the given text \n`{bp}insta [ig_username]` - Download the Instgram profile picture \n`{bp}ip [ip_addr]` - Find Information of an IP Address \n`{bp}lyrics [song_name]` - Find lyrics of any song \n`{bp}mfp [number]` - Mass fake profile \n`{bp}pwdcheck [password]` - Check for the status of a password \n`{bp}uptime` - Show bot uptime \n ", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed3)


def setup(client: commands.Bot):
    client.add_cog(General(client))
