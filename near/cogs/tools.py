import os
import random
import secrets
import string
import textwrap
import urllib

import aiohttp
import discord
import instaloader
import privatebinapi
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds
from zxcvbn import zxcvbn


class Tools(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="lyrics", description="Search the Lyrics of any Song")
    @app_commands.describe(query="Name of the Song")
    async def lyrics(self, intercation: discord.Interaction, query: str = None):
        # Another Option: https://github.com/elmoiv/azapi
        try:
            if not query:
                embed = discord.Embed(
                    title="No search argument!",
                    description="You havent entered anything, so i couldnt find lyrics!",
                    color=get_embeds.Common.COLOR
                )
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar.url}")
                embed.set_footer(text=f"Requested by {intercation.user.name}")
                return await intercation.response.send_message(embed=embed)

            song = urllib.parse.quote(query)

            async with aiohttp.ClientSession() as lyricsSession:
                async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata:
                    if not 300 > jsondata.status >= 200:
                        return await intercation.response.send_message(f'Recieved poor status code of {jsondata.status}')
                    lyricsData = await jsondata.json()

            error = lyricsData.get('error')
            if error:
                return await intercation.response.send_message(f'Recieved unexpected error: {error}')

            songLyrics = lyricsData['lyrics']
            songArtist = lyricsData['author']
            songTitle = lyricsData['title']
            songThumbnail = lyricsData['thumbnail']['genius']

            for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace=False):
                embed = discord.Embed(
                    title=f'{songTitle} - {songArtist}',
                    description=chunk,
                    color=get_embeds.Common.COLOR
                    # timestamp=datetime.datetime.utcnow()
                )
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar.url}")
                embed.set_thumbnail(url=songThumbnail)
                embed.set_footer(text=f"Requested by {intercation.user.name}")
                await intercation.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {intercation.user.name}")
            await intercation.response.send_message(embed=embed3)

    @app_commands.command(name='passwordgen', description="Generate a very secure and unique password")
    @app_commands.describe(length="Length of the Password to generate.")
    async def passwordgen(self, interaction: discord.Interaction, length: int):
        try:

            if int(length) < 101:
                c = ''.join((secrets.choice(string.ascii_letters +
                            string.digits + string.punctuation) for i in range(int(length))))

                embed = discord.Embed(
                    title="Password Generator", color=get_embeds.Common.COLOR)
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar.url}")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
                embed.add_field(name="Password Length",
                                value=f"{length}", inline=False)
                embed.add_field(name="Password",
                                value=f"```{c}```", inline=False)
                embed.set_footer(text=f"Requested by {interaction.user.name}")
                await interaction.response.send_message(embed=embed)

            else:
                embed = discord.Embed(
                    title="Password Generator", description="An Error has occured!", color=get_embeds.Common.COLOR)
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar.url}")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
                embed.add_field(
                    name="Error", value="The value of the number is high", inline=False)
                embed.add_field(name="Possible Fix",
                                value="Enter a value below 40", inline=False)
                embed.set_footer(
                    text=f"Requested by {interaction.user.name}")
                await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)

    @app_commands.command(name="insta", description="Grab the Instagram Profile Picture of a Profile")
    @app_commands.describe(username="Instagram Profile's Username")
    async def insta(self, interaction: discord.Interaction, username: str):
        try:
            igpfp = instaloader.Instaloader()
            igpfp.download_profile(username, profile_pic_only=True)
            os.chdir(f'{username}')
            try:
                os.system("mv *.jpg ..")
            except:
                os.system("move *.jpg ..")
            os.chdir("..")
            try:
                os.system("mv *.jpg igtemp.jpg")
            except:
                os.system("ren *.jpg igtemp.jpg")
            try:
                os.system(f'rm -r {username}')
            except:
                os.system(f'DEL {username} /F/Q/S')

            file = discord.File(f'igtemp.jpg', filename="image.jpg")
            embed = discord.Embed(title="Instagram Profile Picture",
                                  description=f"of {username}", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar.url}")
            embed.add_field(
                name="Link", value=f"https://instagram.com/{username}", inline=False)
            embed.set_image(url="attachment://image.jpg")
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(file=file, embed=embed)

            try:
                os.system(f"rm igtemp.jpg")
            except:
                os.remove(f'{username}')
        except Exception as e:
            await interaction.response.send_message(f"Error: {e}")

    @app_commands.command(name="bin", description="Create a PrivateBin from a Text")
    @app_commands.describe(text="Text to be included in the PrivateBin")
    async def bin(self, interaction: discord.Interaction, text: str):
        try:
            privbin = privatebinapi.send(
                "https://bin.teamsds.net/", text=text)

            embed = discord.Embed(
                title="TeamSDS's PrivateBin", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879586340520480768/large.png")
            embed.add_field(
                name="ID", value=f"{privbin['id']}", inline=False)
            embed.add_field(
                name="URL", value=f"{privbin['full_url']}", inline=False)
            embed.add_field(
                name="Passcode", value=f"{privbin['passcode']}", inline=False)
            embed.add_field(
                name=f"Text by {interaction.user.name}", value=f"{text}", inline=False)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(
                name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3, ephemeral=True)

    @app_commands.command(name="passwordcheck", description="Password Strength Check and Profiler")
    @app_commands.describe(password="Password to analyze")
    async def passwordchk(self, interaction: discord.Interaction, password: str):
        try:
            results = zxcvbn(f"{password}")
            embed3 = discord.Embed(title="Password Check",
                                   description="using Low Budget Password Strength Estimation",
                                   color=get_embeds.Common.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(
                url="https://iconape.com/wp-content/png_logo_vector/password.png")

            embed3.add_field(
                name="Password", value=f"{results['password']}", inline=False)

            embed3.add_field(name="Score",
                             value=f"{results['score']}", inline=False)

            embed3.add_field(
                name="Guesses", value=f"Decimal - {results['guesses']}\nLog10 - {results['guesses_log10']}", inline=False)
            try:
                embed3.add_field(
                    name="Password", value=f"{results['password']}", inline=False)
            except:
                pass

            sequence_info = ""
            for dic in results["sequence"]:
                for k, v in dic.items():
                    sequence_info += f"{k} - {v}\n"
                sequence_info += "\n"

            embed3.add_field(name="Sequence Info",
                             value=f"{sequence_info}", inline=False)

            try:
                embed3.add_field(name="Calculation Time",
                                 value=f"{results['calc_time']}")
            except:
                pass

            try:
                embed3.add_field(name="Crack Time",
                                 value=f"Online throttling 100 per hour - {results['crack_times_display']['online_throttling_100_per_hour']}\nOnline throttling 10 per second - {results['crack_times_display']['online_no_throttling_10_per_second']}\nOffline slow hasing 1e4 per second - {results['crack_times_display']['offline_slow_hashing_1e4_per_second']}\nOffline fast hasing 1e10 per second - {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}", inline=False)
            except:
                pass

            try:
                if results['feedback']['warning'] == '':
                    pass
                else:
                    embed3.add_field(
                        name="Warning", value=f"{results['feedback']['warning']}", inline=False)
            except:
                pass

            try:
                if len(results["feedback"]["suggestions"]) == 0:
                    pass
                else:
                    suggestions_info = ""
                    for item in results["feedback"]["suggestions"]:
                        suggestions_info += f"{item}\n"
                    try:
                        embed3.add_field(
                            name="Suggestions", value=f"{suggestions_info}", inline=False)
                    except Exception as e:
                        print(e)
            except:
                pass

            embed3.set_footer(text=f"Requested by {interaction.user.name}")

            await interaction.response.send_message(embed=embed3)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar.url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3)


async def setup(client: commands.Bot):
    await client.add_cog(Tools(client))
