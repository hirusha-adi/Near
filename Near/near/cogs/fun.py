import discord, requests, aiohttp
from discord.ext import commands
from json import loads as loadjsonstring
from bs4 import BeautifulSoup
from near.database import get_embeds


class OtherCommandsFun(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)


    @commands.command()
    async def inspire(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://zenquotes.io/api/random")
            json_data = loadjsonstring(r.text)
            quote = json_data[0]['q'] + " - " + json_data[0]['a']
            embed=discord.Embed(title="Inspirational isn't it?", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879382016041291828/NicePng_light-streak-png_395357.png")
            embed.add_field(name="Inspirational Quote:", value=f"{quote}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command()
    async def bored(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('http://www.boredapi.com/api/activity/')
            data = r.json()
            what_to_do_when_bored = f'[+] Activity: {data["activity"]} \n[+] Type: {data["type"]} \n[+] Participants: {data["participants"]} \n[+] Key: {data["key"]} \n[+] Accessibility: {data["accessibility"]} '
            embed=discord.Embed(title="Heres an Activity for you", description="If you are bored, consider doing this", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.add_field(name="Activity", value=f"{data['activity']}", inline=False)
            embed.add_field(name="Type", value=f"{data['type']}", inline=False)
            embed.add_field(name="Participants", value=f"{data['participants']}", inline=False)
            embed.add_field(name="Key", value=f"{data['key']}", inline=False)
            embed.add_field(name="Accessibility", value=f"{data['accessibility']}", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/884694742716268554/unnamed.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)
    

    @commands.command(aliases=["lol"])
    async def meme(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/meme").json()

            embed = discord.Embed(color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            
            try:
                caption = str(r["caption"])
                embed.add_field(name="Just a random Meme", value=caption)
            except:
                pass
            
            embed.set_image(url=str(r["image"]))
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command()
    async def dadjoke(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            headers = {
            "Accept": "application/json"
            }
            # Get data from the API with the above mentioned headers
            async with aiohttp.ClientSession()as session:
                async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
                    r = await req.json()

            embed=discord.Embed(title="a Dad Joke", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://user-images.githubusercontent.com/36286877/127767330-d3e68d90-67a0-4672-b3e1-6193b323bc21.png")
            embed.add_field(name="Joke", value=f"{r['joke']}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)
    

    @commands.command()
    async def joke(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://v2.jokeapi.dev/joke/Any")
            c = r.json()
            # print(c)

            try:
                jokeit = c["joke"]
            except:
                try:
                    jokeit = c["setup"]
                except Exception as e:
                    embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=get_embeds.Common.COLOR)
                    embed2.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
                    embed2.set_author(name="NearBot", icon_url="ttps://cdn.discordapp.com/attachments/881007500588089404/881046764206039070/unknown.png")
                    embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                    embed2.add_field(name="Error:", value=f"{e}", inline=False)
                    embed2.set_footer(text=f"Requested by {ctx.author.name}")
                    await loading_message.delete()
                    await ctx.send(embed=embed2)
                    return

            embed=discord.Embed(title=":grin: a Joke", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879303282139463680/480px-Happy_smiley_face.png")
            embed.add_field(name="Joke", value=f"{jokeit}", inline=False)
            embed.add_field(name="Information", value=f"Category: {c['category']} \nType: {c['type']} \nNSFW: {c['flags']['nsfw']} \nReligious: {c['flags']['religious']} \nPolitical: {c['flags']['political']} \nRacist: {c['flags']['racist']} \nSexist: {c['flags']['sexist']} \nExplicit: {c['flags']['explicit']} \nLanguage: {c['lang']}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
    async def wyr(self, ctx, *, questionhere):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text

            soup = BeautifulSoup(r, 'html.parser')
            qa = soup.find(id='qa').text
            qor = soup.find(id='qor').text
            qb = soup.find(id='qb').text

            embed=discord.Embed(title="Would You Rather", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879583873527332904/Would-You-Rather_Questions-680x430.jpg")
            embed.add_field(name="Question", value=f"{questionhere}", inline=False)
            embed.add_field(name="Answer", value=f"{qa}\n{qor}\n{qb}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    
    @commands.command()
    async def advice(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://api.adviceslip.com/advice").json()
            c = r['slip']['advice']

            embed=discord.Embed(title="an Adive", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880034306720956456/download_1.jfif")
            embed.add_field(name="Advice", value=f"{c}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3=discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["chuck-norris-joke", "chuck-joke"])
    async def chuckjoke(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            url = f"https://api.chucknorris.io/jokes/random"
            r = requests.get(url).json()
            joke = r['value']
            created_at = r['created_at']
            urlfj = r['url']

            embed=discord.Embed(title="Chuck Joke", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/880035248820342824/chuck-norris.png")
            embed.add_field(name="Joke", value=f"{joke}", inline=False)
            embed.add_field(name="Created At", value=f"{created_at}", inline=False)
            embed.add_field(name="URL", value=f"{urlfj}", inline=True)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


    @commands.command(aliases=["jokenew", "newjoke"])
    async def joke2(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get("https://some-random-api.ml/joke").json()

            embed=discord.Embed(title="a Joke", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/877796755234783273/880742956552822794/mr-bean-avatar-character-cartoon-rowan-atkinson-png-image-33.png?width=454&height=584")
            embed.add_field(name="Joke", value=f"{r['joke']}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)





def setup(client: commands.Bot):
    client.add_cog(OtherCommandsFun(client))







