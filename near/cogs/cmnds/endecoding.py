import base64
import hashlib

import discord

from near.database import get_embeds
from near.utils import errors
from near.utils import input_sanitization


class Cmnds_EncodeDecode:
    
    @errors.handle_error
    async def b64encode(interaction: discord.Interaction, text: str):
        if input_sanitization.check_input(text):
            msg = base64.b64encode('{}'.format(text).encode('ascii'))
            result = str(msg)
            result = result[2:len(result)-1]

            embed = discord.Embed(title="Encode to Base64", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg")
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{result}", inline=True)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)
        else:
                raise errors.IllegalInput

    @errors.handle_error
    async def b64decode(interaction: discord.Interaction, text: str):
        if input_sanitization.is_base64(text):
            msg = base64.b64decode('{}'.format(text).encode('ascii'))
            result = str(msg)
            result = result[2:len(result)-1]
            
            embed = discord.Embed(title="Decode from Base64", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879955815602200586/base64-logo-352x200.jpg")
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{result}", inline=True)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput
        
    @errors.handle_error
    async def md5(interaction: discord.Interaction, text: str):
        if input_sanitization.check_input(text):
            msg = hashlib.md5(text.encode())
            slpake = msg.hexdigest()

            embed = discord.Embed(title="to MD5", color=get_embeds.Common.COLOR)
            embed.set_author(name=f"{self.client.user.name}", icon_url=f"{self.client.user.avatar.url}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879956672771137546/MD5.png")
            embed.add_field(name="Query", value=f"{text}", inline=False)
            embed.add_field(name="Result", value=f"{slpake}", inline=True)
            embed.set_footer(text=f"Requested by {interaction.user.name}")
            await interaction.response.send_message(embed=embed)
        else:
            raise errors.IllegalInput

    @errors.handle_error
    async def doge(interaction: discord.Interaction):
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
        dat = r.json()
        eur = dat['EUR']
        usd = dat['USD']
        embed = discord.Embed(title="Doge Coin", color=get_embeds.Common.COLOR)
        embed.set_author(name=f"Near", icon_url=f"https://user-images.githubusercontent.com/36286877/208341567-6706e40f-03b5-4e29-836c-760708f2e619.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073564685061861388/Dogecoin_Logo.png")
        embed.add_field(name="USD", value=f"{usd}", inline=False)
        embed.add_field(name="EUR", value=f"{eur}", inline=True)
        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)

    @errors.handle_error
    async def xrp(interaction: discord.Interaction):
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
        dat = r.json()
        eur = dat['EUR']
        usd = dat['USD']
        embed = discord.Embed(title="Ripple", color=get_embeds.Common.COLOR)
        embed.set_author(name=f"Near", icon_url=f"https://user-images.githubusercontent.com/36286877/208341567-6706e40f-03b5-4e29-836c-760708f2e619.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073565079410319430/free-ripple-coin-icon-2208-thumb.png")
        embed.add_field(name="USD", value=f"{usd}", inline=False)
        embed.add_field(name="EUR", value=f"{eur}", inline=True)
        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)

    @errors.handle_error
    async def rvn(interaction: discord.Interaction):
        c = requests.get('https://www.coindesk.com/price/ravencoin/')
        soup = BeautifulSoup(c.content, "html.parser")
        raven_coin_value = soup.find_all("span", {"class": "currency-pricestyles__Price-sc-1rux8hj-0 jxzQXk"})[0].text
        change_percentage = soup.find_all("h6", {"class": "typography__StyledTypography-owin6q-0 hZxwDe"})[0].text
        embed = discord.Embed(title="Ravencoin", color=get_embeds.Common.COLOR)
        embed.set_author(name=f"Near", icon_url=f"https://user-images.githubusercontent.com/36286877/208341567-6706e40f-03b5-4e29-836c-760708f2e619.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/940889393974104084/1073566855593197600/ravencoin-rvn-logo.png")
        embed.add_field(name="USD", value=f"{raven_coin_value}", inline=False)
        embed.add_field(name="24 Hour Change %", value=f"{change_percentage}", inline=False)
        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)
 