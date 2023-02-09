import os
import random
import secrets
import string
import textwrap
import urllib

import aiohttp
import discord
import instaloader
from discord import app_commands
from discord.ext import commands

from near.database import get_embeds


class Tools(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=get_embeds.PleaseWait.AUTHOR_NAME, icon_url=get_embeds.PleaseWait.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)

    @commands.command(aliases=["lyricsof"])
    async def lyrics(self, ctx, *, search=None):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            if not search:
                embed = discord.Embed(
                    title="No search argument!",
                    description="You havent entered anything, so i couldnt find lyrics!",
                    color=get_embeds.Common.COLOR
                )
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar_url}")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                try:
                    await loading_message.delete()
                except:
                    pass
                return await ctx.send(embed=embed)

            song = urllib.parse.quote(search)

            async with aiohttp.ClientSession() as lyricsSession:
                async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata:
                    if not 300 > jsondata.status >= 200:
                        try:
                            await loading_message.delete()
                        except:
                            pass
                        return await ctx.send(f'Recieved poor status code of {jsondata.status}')
                    lyricsData = await jsondata.json()

            error = lyricsData.get('error')
            if error:
                try:
                    await loading_message.delete()
                except:
                    pass
                return await ctx.send(f'Recieved unexpected error: {error}')

            songLyrics = lyricsData['lyrics']
            songArtist = lyricsData['author']
            songTitle = lyricsData['title']
            songThumbnail = lyricsData['thumbnail']['genius']

            for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace=False):
                embed = discord.Embed(
                    title=f'{songTitle} - {songArtist}',
                    description=chunk,
                    color=get_embeds.Common.COLOR
                    # timestamp = datetime.datetime.utcnow()
                )
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar_url}")
                embed.set_thumbnail(url=songThumbnail)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                try:
                    await loading_message.delete()
                except:
                    pass
                await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=f"{self.client.user.name}",
                              icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["generate-pwd", "gen-pwd", "generate-password", "gen-password", "newpassword", "password", "newpass", "passwordnew"])
    async def genpwd(self, ctx, *, numberofcharacters=16):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:

            if int(numberofcharacters) < 101:
                c = ''.join((secrets.choice(string.ascii_letters +
                            string.digits + string.punctuation) for i in range(int(numberofcharacters))))

                embed = discord.Embed(
                    title="Password Generator", color=get_embeds.Common.COLOR)
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar_url}")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
                embed.add_field(name="Password Length",
                                value=f"{numberofcharacters}", inline=False)
                embed.add_field(name="Password",
                                value=f"```{c}```", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await loading_message.delete()
                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(
                    title="Password Generator", description="An Error has occured!", color=get_embeds.Common.COLOR)
                embed.set_author(name=f"{self.client.user.name}",
                                 icon_url=f"{self.client.user.avatar_url}")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/877796755234783273/880031728369016832/704187.png")
                embed.add_field(
                    name="Error", value="The value of the number is high", inline=False)
                embed.add_field(name="Possible Fix",
                                value="Enter a value below 40", inline=False)
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
    async def insta(self, ctx, *, ig_uname):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            igpfp = instaloader.Instaloader()
            igpfp.download_profile(ig_uname, profile_pic_only=True)
            os.chdir(f'{ig_uname}')
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
                os.system(f'rm -r {ig_uname}')
            except:
                os.system(f'DEL {ig_uname} /F/Q/S')

            file = discord.File(f'igtemp.jpg', filename="image.jpg")
            embed = discord.Embed(title="Instagram Profile Picture",
                                  description=f"of {ig_uname}", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
            embed.add_field(
                name="Link", value=f"https://instagram.com/{ig_uname}", inline=False)
            embed.set_image(url="attachment://image.jpg")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(file=file, embed=embed)

            try:
                os.system(f"rm igtemp.jpg")
            except:
                os.remove(f'{ig_uname}')
        except Exception as e:
            await ctx.send(f"Error: {e}")

    @app_commands.command(name="bin", description="Create a PrivateBin from a Text")
    @app_commands.describe(text="Text to be included in the PrivateBin")
    async def bin(self, interaction: discord.Interaction, text: str):
        try:
            privbin = privatebinapi.send(
                "https://bin.teamsds.net/", text=text)

            embed = discord.Embed(
                title="TeamSDS's PrivateBin", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}",
                             icon_url=f"{self.client.user.avatar_url}")
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
                name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar_url}")
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed3, ephemeral=True)


async def setup(client: commands.Bot):
    await client.add_cog(Tools(client))
