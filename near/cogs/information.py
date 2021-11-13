import discord
import requests
from discord.ext import commands
from near.database import get_embeds
from zxcvbn import zxcvbn


class Information(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(
            title=get_embeds.PleaseWait.TITLE, description=get_embeds.PleaseWait.DESCRIPTION, color=get_embeds.PleaseWait.COLOR)
        self.please_wait_emb.set_author(
            name=get_embeds.Common.AUTHOR_NAME, icon_url=get_embeds.Common.AUTHOR_URL)
        self.please_wait_emb.set_thumbnail(url=get_embeds.PleaseWait.THUMBNAIL)
        self.please_wait_emb.set_footer(text=get_embeds.PleaseWait.FOOTER)

        self.filepwdlist1 = open("near/assets/tenmilpwds.txt", "r")
        self.lines = self.filepwdlist1.readlines()

    @commands.command(aliases=["ipinfo", "infoip", "ip-info", "info-ip"])
    async def ip(self, ctx, *, ip_from_user):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            r = requests.get(f"https://ipapi.co/{ip_from_user}/json").json()
            rc = requests.get(
                f"https://api.worldbank.org/v2/country/{r['country_code']}?format=json").json()

            embed = discord.Embed(title="IP Information",
                                  color=get_embeds.Common.COLOR)
            embed.set_thumbnail(
                url="https://user-images.githubusercontent.com/36286877/127773181-c98b63be-b18b-4d8b-a8b6-9426bd031b7c.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME,
                             icon_url=get_embeds.Common.AUTHOR_URL)
            embed.add_field(name="IP Info", value="IP Address: " + str(r["ip"]) + "\nCity: " + str(r["city"]) + "\nRegion: " + str(r["region"]) + "\nCountry Name: " + str(r["country_name"]) + "\nLatitude: " + str(r["latitude"]) + "\nLongitude: " + str(r["longitude"]) + "\nTime Zone: " + str(r["timezone"]) + "\nUTC Offset: " + str(r["utc_offset"]) + "\nPostal Code: " + str(r["postal"]) + str("\nISP: " + r["org"]) + "\nASN: " + str(r["asn"]) + "\nCountry Code: " + str(
                r["country_code"]) + "\nCountry TLD: " + str(r["country_tld"]) + "\nPopulation: " + str(r["country_population"]) + "\nCurrency: " + str(r["currency"]) + "\n Curreny Name: " + str(r["currency_name"]) + "\nCountry Area: " + str(r["country_area"]) + "\nLanguages: " + str(r["languages"]) + "\nCalling Code: " + str(r["country_calling_code"]) + "\nGOOGLE MAPS Link: " + f"https://maps.google.com/?q={r['latitude']},{r['longitude']}", inline=False)
            embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(
                rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME,
                              icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(alises=["country-info", "country", "infocountry", "country-information"])
    async def countryinfo(self, ctx, *, countrycodeig):
        # MAKE SURE TO ENTER THE COUNTRY CODE AND NOT THE COUNTRY NAME
        # eg- sg ( for Singapore ), us for ( United States )
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            rc = requests.get(
                f"https://api.worldbank.org/v2/country/{countrycodeig}?format=json").json()

            embed = discord.Embed(
                title="Country Information", color=get_embeds.Common.COLOR)
            embed.set_thumbnail(
                url="https://user-images.githubusercontent.com/36286877/129850352-33345963-273b-42bf-b2bc-5523c8158229.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_author(name=get_embeds.Common.AUTHOR_NAME,
                             icon_url=get_embeds.Common.AUTHOR_URL)
            embed.add_field(name="Country Info", value="ID: " + str(rc[1][0]["id"]) + "\niso2Code: " + str(rc[1][0]["iso2Code"]) + "\nName" + str(rc[1][0]["name"]) + "\n\nRegion: " + "\n   ID: " + str(rc[1][0]["region"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["region"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["region"]["value"]) + "\n\nAdmin Region: " + "\n   ID: " + str(rc[1][0]["adminregion"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["adminregion"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["adminregion"]["value"]) + "\n\nIncome Level: " + "\n   ID: " + str(
                rc[1][0]["incomeLevel"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["incomeLevel"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["incomeLevel"]["value"]) + "\n\nLending Type: " + "\n   ID: " + str(rc[1][0]["lendingType"]["id"]) + "\n   iso2Code: " + str(rc[1][0]["lendingType"]["iso2code"]) + "\n   Value: " + str(rc[1][0]["lendingType"]["value"]) + "\n\nCapital City: " + str(rc[1][0]["capitalCity"]) + "\nLongitude: " + str(rc[1][0]["longitude"]) + "\nLatitude: " + str(rc[1][0]["latitude"]), inline=False)
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME,
                              icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(aliases=["covidall"])
    async def covid(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            # This uses the official API provided by the Sri Lankan Government to gather the needed data
            r = requests.get(
                "https://www.hpb.health.gov.lk/api/get-current-statistical")
            c = r.json()
            data = c['data']

            update_date_time = data['update_date_time']
            global_new_cases = data['global_new_cases']
            global_total_cases = data['global_total_cases']
            global_deaths = data['global_deaths']
            global_new_deaths = data['global_new_deaths']
            global_recovered = data['global_recovered']
            total_pcr_testing_count = data['total_pcr_testing_count']
            total_antigen_testing_count = data['total_antigen_testing_count']

            em = discord.Embed(
                title="COVID-19 Stats Global - All Info", color=get_embeds.Common.COLOR)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            em.set_author(name=get_embeds.Common.AUTHOR_NAME,
                          icon_url=get_embeds.Common.AUTHOR_URL)
            em.set_thumbnail(
                url="https://www.apsf.org/wp-content/uploads/newsletters/2020/3502/coronavirus-covid-19.png")
            em.add_field(name="Last Updated", value=update_date_time)
            em.add_field(name="New Cases", value=global_new_cases)
            em.add_field(name="Total Cases", value=global_total_cases)
            em.add_field(name="Total Deaths", value=global_deaths)
            em.add_field(name="New Deaths", value=global_new_deaths)
            em.add_field(name="Total Recovered", value=global_recovered)
            em.add_field(name="Total PCR Testing Count",
                         value=total_pcr_testing_count)
            em.add_field(name="Total Antigen Testing Count",
                         value=total_antigen_testing_count)
            await loading_message.delete()
            await ctx.send(embed=em)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME,
                              icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(
                name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

    @commands.command(breif="Password Checker",
                      description="This command will send you very useful information about your password",
                      help="This command will send you very useful information about your password",
                      aliases=['pwdcheck']
                      )
    async def passwordchk(self, ctx, *, password):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            results = zxcvbn('hirusha')
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME,
                              icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)

            embed3.add_field(
                name="Password", value=f"{password}", inline=False)
            embed3.add_field(
                name="Guesses", value=f"Decimal: {results['guesses']}\nLog 10: {results['guesses_log10']}", inline=False)

            pat = ""
            for seq in results['sequence']:
                pat += f"\n-------\nPattern: {seq['pattern']}\ni: {seq['i']}\nj: {seq['j']}\nToken: {seq['token']}\nMatched Word: {seq['matched_word']}\nRank: {seq['rank']}\nDictionary Name: {seq['dictionary_name']}\nReversed: {seq['reversed']}\nl33t: {seq['l33t']}\nBase Guesses: {seq['base_guesses']}\nUppercase Variations: {seq['uppercase_variations']}\nl33t Variations: {seq['l33t_variations']}\nGuesses: {seq['guesses']}\nGuesses Log10: {seq['guesses_log10']}"

            embed3.add_field(name="Pattern: ", value=f"{pat}", inline=False)
            embed3.add_field(name="Calculate Time: ",
                             value=f"{results['calc_time']}", inline=False)
            embed3.add_field(name="Crack Time Seconds: ",
                             value=f"Online Throttling 100 Per Hour: {results['crack_times_seconds']['online_throttling_100_per_hour']}\nOnline no Throttling 10 Per Second: {results['crack_times_seconds']['online_no_throttling_10_per_second']}\nOffline Slow Hashing 1e4 Per Second: {results['crack_times_seconds']['offline_slow_hashing_1e4_per_second']}\nOffline Fast Hashing 1e10 Per Second: {results['crack_times_seconds']['offline_fast_hashing_1e10_per_second']}", inline=False)
            embed3.add_field(name="Crack Times Display: ",
                             value=f"Online Throttling 100 Per Hour: {results['crack_times_display']['online_throttling_100_per_hour']}\nOnline No Throttling 10 Per Second: {results['crack_times_display']['online_no_throttling_10_per_second']}\nOffline Slow Hashing 1e4 Per Second: {results['crack_times_display']['offline_slow_hashing_1e4_per_second']}\nOffline Fast Hashing 1e10 Per Second: {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}", inline=False)
            embed3.add_field(
                name="Score: ", value=f"{results['score']}", inline=False)

            fdb = ""
            for feedbsug in results['feedback']['suggestions']:
                fdb += f"{feedbsug}\n"

            embed3.add_field(
                name="Feedback: ", value=f"{results['feedback']['warning']}\n{fdb}", inline=False)

            if password + "\n" in self.lines:
                embed3.add_field(
                    name="Password Found!", value=f"This password can be found in the list of most common 10 Million passwords", inline=False
                )
            else:
                embed3.add_field(
                    name="Password Not Found!", value=f"This password cannot be found in the list of most common 10 Million passwords", inline=False
                )
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)

        except Exception as e:
            embed3 = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE,
                                   description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
            embed3.set_author(name=get_embeds.Common.AUTHOR_NAME,
                              icon_url=get_embeds.Common.AUTHOR_URL)
            embed3.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)


def setup(client: commands.Bot):
    client.add_cog(Information(client))
