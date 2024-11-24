import base64
import hashlib

import discord
from discord import app_commands
from discord.ext import commands
from loguru import logger

from near.utils import embeds
from near.utils import errors
from near.utils import log
from near.utils import input_sanitization


class EncodeDecode(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="b64encode", description="Encode to Base64")
    @app_commands.describe(text="Text to process")
    async def b64encode(self, interaction: discord.Interaction, text: str):
        await log.log_command_history(command="/b64encode", command_args=f"text: {text}", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            if input_sanitization.check_input(text):
                msg = base64.b64encode('{}'.format(text).encode('ascii'))
                result = str(msg)
                result = result[2:len(result)-1]

                embed = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="Encode to Base64",
                    thumbnail="endecoding_b64",
                )
                embed.add_field(name="Query", value=f"{text}", inline=False)
                embed.add_field(name="Result", value=f"{result}", inline=True)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="b64decode", description="Decode from Base64")
    @app_commands.describe(text="Text to process")
    async def b64decode(self, interaction: discord.Interaction, text: str):
        await log.log_command_history(command="/b64decode", command_args=f"text: {text}", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            if input_sanitization.is_base64(text):
                msg = base64.b64decode('{}'.format(text).encode('ascii'))
                result = str(msg)
                result = result[2:len(result)-1]

                embed = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="Decode from Base64",
                    thumbnail="endecoding_b64",
                )
                embed.add_field(name="Query", value=f"{text}", inline=False)
                embed.add_field(name="Result", value=f"{result}", inline=True)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="md5", description="Get MD5 Hash")
    @app_commands.describe(text="Text to process")
    async def md5(self, interaction: discord.Interaction, text: str):
        await log.log_command_history(command="/md5", command_args=f"text: {text}", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            if input_sanitization.check_input(text):
                msg = hashlib.md5(text.encode())
                result = msg.hexdigest()

                embed = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="MDS Hash",
                    thumbnail="endecoding_md5",
                )
                embed.add_field(name="Query", value=f"{text}", inline=False)
                embed.add_field(name="Result", value=f"{result}", inline=True)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="sha1", description="Get SHA1 Hash")
    @app_commands.describe(text="Text to process")
    async def sha1(self, interaction: discord.Interaction, text: str):
        await log.log_command_history(command="/sha1", command_args=f"text: {text}", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            if input_sanitization.check_input(text):
                msg = hashlib.sha1(text.encode())
                slpake = msg.hexdigest()

                embed = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="SHA1 Hash",
                    thumbnail="endecoding_hash",
                )
                embed.add_field(name="Query", value=f"{text}", inline=False)
                embed.add_field(name="Result", value=f"{slpake}", inline=True)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="sha224", description="Get SHA224 Hash")
    @app_commands.describe(text="Text to process")
    async def sha224(self, interaction: discord.Interaction, text: str):
        await log.log_command_history(command="/sha224", command_args=f"text: {text}", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            if input_sanitization.check_input(text):
                msg = hashlib.sha224(text.encode())
                slpake = msg.hexdigest()

                embed = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="SHA224 Hash",
                    thumbnail="endecoding_hash",
                )
                embed.add_field(name="Query", value=f"{text}", inline=False)
                embed.add_field(name="Result", value=f"{slpake}", inline=True)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="sha512", description="Get SHA512 Hash")
    @app_commands.describe(text="Text to process")
    async def sha512(self, interaction: discord.Interaction, text: str):
        await log.log_command_history(command="/sha512", command_args=f"text: {text}", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            if input_sanitization.check_input(text):
                msg = hashlib.sha512(text.encode())
                slpake = msg.hexdigest()

                embed = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="SHA512 Hash",
                    thumbnail="endecoding_hash",
                )
                embed.add_field(name="Query", value=f"{text}", inline=False)
                embed.add_field(name="Result", value=f"{slpake}", inline=True)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="leet", description="Convert text to L33T format")
    @app_commands.describe(text="Text to process")
    async def leet(self, interaction: discord.Interaction, text: str):
        await log.log_command_history(command="/leet", command_args=f"text: {text}", author_id=interaction.user.id, author_name=interaction.user.name, server_id=interaction.guild.id, server_name=interaction.guild.name)
        try:
            if input_sanitization.check_input(text):
                encoded = (
                    text.replace("e", "3")
                    .replace("a", "4")
                    .replace("i", "!")
                    .replace("u", "|_|")
                    .replace("U", "|_|")
                    .replace("E", "3")
                    .replace("I", "!")
                    .replace("A", "4")
                    .replace("o", "0")
                    .replace("O", "0")
                    .replace("t", "7")
                    .replace("T", "7")
                    .replace("l", "1")
                    .replace("L", "1")
                    .replace("k", "|<")
                    .replace("K", "|<")
                    .replace("CK", "X")
                    .replace("ck", "x")
                    .replace("Ck", "X")
                    .replace("cK", "x")
                )

                embed = await embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="L33T",
                    thumbnail="endecoding_leet",
                )
                embed.add_field(name="Query", value=f"{text}", inline=False)
                embed.add_field(name="Result", value=f"{encoded}", inline=True)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=await embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(EncodeDecode(client))
