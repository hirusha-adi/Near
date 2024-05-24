import os
import secrets
import string
import shutil
import glob

import discord
import instaloader
import privatebinapi
from discord import app_commands
from discord.ext import commands
from zxcvbn import zxcvbn

from near.utils import embeds
from near.utils import input_sanitization, errors


class Tools(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        with open(os.path.join('near', 'assets', 'tenmilpwds.txt'), 'r') as _file:
            self.lines = _file.readlines()

    @app_commands.command(name='passwordgen', description="Generate a very secure and unique password")
    @app_commands.describe(length="Length of the Password to generate.")
    async def passwordgen(self, interaction: discord.Interaction, length: int):
        try:

            if int(length) < 101:
                c = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(int(length))))

                embed = embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="Password Generator",
                    thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png"
                )
                embed.add_field(name="Password Length", value=f"{length}", inline=False)
                embed.add_field(name="Password", value=f"```{c}```", inline=False)
                await interaction.response.send_message(embed=embed)

            else:
                await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"The value of the number is high.\nPlease Enter a value below 40,"), ephemeral=False)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="insta", description="Grab the Instagram Profile Picture of a Profile")
    @app_commands.describe(username="Instagram Profile's Username")
    async def insta(self, interaction: discord.Interaction, username: str):
        try:
            igpfp = instaloader.Instaloader()
            igpfp.download_profile(username, profile_pic_only=True)
                
            os.chdir(f'{username}')
            jpg_files = glob.glob("*.jpg")
            for jpg_file in jpg_files:
                shutil.move(jpg_file, os.path.join("..", jpg_file))
            os.chdir("..")
            jpg_files = glob.glob("*.jpg")
            for jpg_file in jpg_files:
                shutil.move(jpg_file, "igtemp.jpg")
                break
                
            file = discord.File(f'igtemp.jpg', filename="image.jpg")
            
            # Use this if you want to send the image as an embed
            # ---
            
            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Instagram Profile Picture",
                description=f"of {username}",
                thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png"
            )
            embed.add_field(name="Link", value=f"https://instagram.com/{username}", inline=False)
            embed.set_image(url="attachment://image.jpg")
            await interaction.response.send_message(file=file, embed=embed)
            
            # Use this if you only want to send the file without an embed
            # ---
            # await interaction.response.send_message(file=file)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)
            
        finally:
            try:
                shutil.rmtree(username)
                os.remove(f'igtemp.jpg')
            except Exception as e:
                print(f"Error removing directory {username}: {e}")
            

    @app_commands.command(name="bin", description="Create a PrivateBin from a Text")
    @app_commands.describe(text="Text to be included in the PrivateBin")
    async def bin(self, interaction: discord.Interaction, text: str):
        try:
            if input_sanitization.check_input(text):
                privbin = privatebinapi.send("https://bin.teamsds.net/", text=text)
                
                embed = embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="TeamSDS's PrivateBin",
                    thumbnail="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png"
                )
                embed.add_field(name="ID", value=f"{privbin['id']}", inline=False)
                embed.add_field(name="URL", value=f"{privbin['full_url']}", inline=False)
                embed.add_field(name="Passcode", value=f"{privbin['passcode']}", inline=False)
                embed.add_field(name=f"Text by {interaction.user.name}", value=f"{text}", inline=False)
                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)

    @app_commands.command(name="passwordcheck", description="Password Strength Check and Profiler")
    @app_commands.describe(password="Password to analyze")
    async def passwordchk(self, interaction: discord.Interaction, password: str):
        try:
            if input_sanitization.password_check(password):
                results = zxcvbn(f"{password}")
                
                embed = embeds.Common(
                    client=self.client,
                    interaction=interaction,
                    title="Password Check",
                    description="using Low Budget Password Strength Estimation (zxcvbn)",
                    thumbnail="https://iconape.com/wp-content/png_logo_vector/password.png"
                )

                embed.add_field(name="Password", value=f"{results.get('password', '')}", inline=False)
                embed.add_field(name="Score", value=f"{results['score']}", inline=False)
                embed.add_field(name="Guesses", value=f"Decimal - {results['guesses']}\nLog10 - {results['guesses_log10']}", inline=False)
                
                sequence_info = "\n".join(f"{k} - {v}" for dic in results["sequence"] for k, v in dic.items())
                embed.add_field(name="Sequence Info", value=sequence_info, inline=False)

                embed.add_field(name="Calculation Time", value=f"{results.get('calc_time', '')}", inline=False)
                crack_times = results.get('crack_times_display', {})
                embed.add_field(name="Crack Time", value=(
                    f"Online throttling 100 per hour - {crack_times.get('online_throttling_100_per_hour', '')}\n"
                    f"Online throttling 10 per second - {crack_times.get('online_no_throttling_10_per_second', '')}\n"
                    f"Offline slow hashing 1e4 per second - {crack_times.get('offline_slow_hashing_1e4_per_second', '')}\n"
                    f"Offline fast hashing 1e10 per second - {crack_times.get('offline_fast_hashing_1e10_per_second', '')}"
                ), inline=False)

                feedback = results.get('feedback', {})
                warning = feedback.get('warning', '')
                if warning:
                    embed.add_field(name="Warning", value=warning, inline=False)
                
                suggestions = "\n".join(feedback.get('suggestions', []))
                if suggestions:
                    embed.add_field(name="Suggestions", value=suggestions, inline=False)
                
                if f'{password}\n' in self.lines:
                    embed.add_field(name="Common Password", value="This password is among the worlds top 1 million most common passwords", inline=False)

                await interaction.response.send_message(embed=embed)
            else:
                raise errors.IllegalInput

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"), ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(Tools(client))
