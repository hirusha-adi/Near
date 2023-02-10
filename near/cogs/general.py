from datetime import timedelta as dttimedelta
from platform import python_version as cur_python_version
from time import time as nowtime

import discord
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds, get_main


class General(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Bot uptime
        self.start_time = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.client.user.name}')
        print(f'Discord.py API version: {discord.__version__}')
        print(f'Python version: {cur_python_version()}')
        self.start_time = nowtime()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"teamsds.net/discord"))
        synced = await self.client.tree.sync()
        print(synced)
        print(f'Synced {len(synced)} Slash Commands')
        print('Bot is ready!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="ERROR", description="`You don't have the permissions required to use this command!`", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.default_avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await ctx.send(embed=embed)
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Something is wrong!", description="An error has been occured!", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.default_avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.add_field(
                name="Error", value="You haven't passed the needed arguments for this command to run properly", inline=True)
            embed.add_field(
                # name="Possible Fix", value=f"use `{get_main.BotMainDB.MESSAGE_PREFIX}help all` to list out all the command and check the proper usage of the command you used", inline=True)
                name="Possible Fix", value=f"use `{self.client.get_prefix}help all` to list out all the command and check the proper usage of the command you used", inline=True)
            await ctx.send(embed=embed)
            return

    @app_commands.command(name="ping", description="Check the response time of the Discord Bot")
    async def ping(self, interaction: discord.Interaction):
        try:
            embed = discord.Embed(title="Response Time",
                                  color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.default_avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
            embed.add_field(
                name=f"Ping :timer:", value=f"{round(self.client.latency * 1000)} ms", inline=False)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

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

    @app_commands.command(name="uptime", description="How long has the bot been up for?")
    async def uptime(self, interaction: discord.Interaction):
        try:
            current_time = nowtime()
            difference = int(round(current_time - self.start_time))
            text = str(dttimedelta(seconds=difference))
            embed = discord.Embed(color=get_embeds.Common.COLOR)
            embed.add_field(name="The bot was online for: ",
                            value=f":alarm_clock: {text}", inline=False)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

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

    @app_commands.command(name="clean", description="Delete messages sent by the Bot")
    @app_commands.describe(amount="Amount of messages to Delete")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clean(self, interaction: discord.Interaction, amount: int):
        # interaction.user.guild_permissions.manage_channels
        try:
            if amount <= 100:

                amttdel = amount + 1
                await interaction.channel.purge(limit=amttdel, check=lambda m: m.author == self.client.user)

                msgtxt = "message" if amount == "1" else "messages"

                embed = discord.Embed(
                    title="Success!", color=get_embeds.Common.COLOR)
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.default_avatar.url}")
                embed.add_field(
                    name="Action", value=f"Deleted {amount} {msgtxt} sent by {self.client.user.name}!", inline=False)
                embed.set_footer(
                    text=f"Requested by {interaction.user.name}")
                await interaction.response.send_message(embed=embed, ephemeral=True)

            else:
                embed2 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                       description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed2.set_author(name=f"{self.client.user.name}",
                                  icon_url=f"{self.client.user.default_avatar.url}")
                embed2.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed2.add_field(
                    name="Error:", value=f"Please enter a value below 100!", inline=False)
                embed2.set_footer(
                    text=f"Requested by {interaction.user.name}")
                await interaction.response.send_message(embed=embed2, ephemeral=True)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.default_avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(client: commands.Bot):
    await client.add_cog(General(client))
