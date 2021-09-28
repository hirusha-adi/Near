import discord
import base64
import hashlib
from discord.ext import commands
from near.database import get_embeds


class EncodeDecode(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    
        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.TITLE, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.DESCRIPTION)

    
    @commands.command(aliases=["e_base64"])
    async def e_b64(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = base64.b64encode('{}'.format(args).encode('ascii'))
            enc = str(msg)
            enc = enc[2:len(enc)-1]

            embed=discord.Embed(title="to Base64", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{enc}", inline=True)
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
    async def e_md5(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.md5(args.encode())
            slpake =  msg.hexdigest()

            embed=discord.Embed(title="to MD5", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879956672771137546/MD5.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{slpake}", inline=True)
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
    async def e_sha1(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.sha1(args.encode())
            slpuka =  msg.hexdigest()

            embed=discord.Embed(title="to SHA1", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879957622546108436/SHA1.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{slpuka}", inline=True)
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
    async def e_sha224(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.sha3_224(args.encode())
            crnja =  msg.hexdigest()

            embed=discord.Embed(title="to SHA224", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879958751640191046/download.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{crnja}", inline=True)
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
    async def e_sha512(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            msg = hashlib.sha3_512(args.encode())
            crnja =  msg.hexdigest()

            embed=discord.Embed(title="to SHA512", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879960296863698944/download_1.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{crnja}", inline=True)
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


    @commands.command(aliases=["leet"])
    async def e_leet(self, ctx, *, args):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            encoded = args.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')

            embed=discord.Embed(title="to LEET", color=get_embeds.Common.COLOR)
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879961162895212574/download_2.png")
            embed.add_field(name="Query", value=f"{args}", inline=False)
            embed.add_field(name="Result", value=f"{encoded}", inline=True)
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
    client.add_cog(EncodeDecode(client))
