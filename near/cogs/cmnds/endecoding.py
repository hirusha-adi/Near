import base64
import hashlib

import discord

from near.utils import embeds
from near.utils import errors
from near.utils import input_sanitization


class Cmnds_EncodeDecode:

    @errors.handle_error
    async def b64encode(interaction: discord.Interaction, text: str):
        if input_sanitization.check_input(text):
            msg = base64.b64encode("{}".format(text).encode("ascii"))
            result = str(msg)
            result = result[2 : len(result) - 1]

            embed = embeds.Common(
                interaction=interaction,
                title="Encode to Base64",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg",
            )
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{result}", inline=True)
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput

    @errors.handle_error
    async def b64decode(interaction: discord.Interaction, text: str):
        if input_sanitization.is_base64(text):
            msg = base64.b64decode("{}".format(text).encode("ascii"))
            result = str(msg)
            result = result[2 : len(result) - 1]

            embed = embeds.Common(
                interaction=interaction,
                title="Decode from Base64",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg",
            )
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{result}", inline=True)
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput

    @errors.handle_error
    async def md5(interaction: discord.Interaction, text: str):
        if input_sanitization.check_input(text):
            msg = hashlib.md5(text.encode())
            slpake = msg.hexdigest()

            embed = embeds.Common(
                interaction=interaction,
                title="MDS Hash",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879956672771137546/MD5.png",
            )
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{slpake}", inline=True)
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput

    @errors.handle_error
    async def sha1(interaction: discord.Interaction, text: str):
        if input_sanitization.check_input(text):
            msg = hashlib.sha1(text.encode())
            slpake = msg.hexdigest()

            embed = embeds.Common(
                interaction=interaction,
                title="SHA1 Hash",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879957622546108436/SHA1.png",
            )
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{slpake}", inline=True)
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput

    @errors.handle_error
    async def sha224(interaction: discord.Interaction, text: str):
        if input_sanitization.check_input(text):
            msg = hashlib.sha224(text.encode())
            slpake = msg.hexdigest()

            embed = embeds.Common(
                interaction=interaction,
                title="SHA224 Hash",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879958751640191046/download.png",
            )
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{slpake}", inline=True)
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput

    @errors.handle_error
    async def sha512(interaction: discord.Interaction, text: str):
        if input_sanitization.check_input(text):
            msg = hashlib.sha512(text.encode())
            slpake = msg.hexdigest()

            embed = embeds.Common(
                interaction=interaction,
                title="SHA512 Hash",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879960296863698944/download_1.png",
            )
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{slpake}", inline=True)
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput

    @errors.handle_error
    async def leet(interaction: discord.Interaction, text: str):
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

            embed = embeds.Common(
                interaction=interaction,
                title="L33T",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879961162895212574/download_2.png",
            )
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{encoded}", inline=True)
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput
