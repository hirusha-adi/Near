
@client.command()
async def face(ctx, gender="any"):

  try:
    # any_wl = ("any", "everything", "both", "all", "whole")
    male_wl = ("male", "man", "dick","testes", "boy", "m")
    female_wl = ("female", "girl", "egirl", "vagina", "puss", "pussy", "gurl", "g", "f", "lady", "woman", "wife")
    fake = Faker()

    # Loading Message
    loading_message = await ctx.send(embed=please_wait_emb)


    if gender.lower() in male_wl:
      r = requests.get("https://fakeface.rest/face/json?gender=male").json()
      embed=discord.Embed(title="Here is your generated face", color=0xff0000)
      embed.add_field(name="Name", value=f"{fake.first_name_male()} {fake.last_name_male()}", inline=False)
      embed.add_field(name="Gender", value="Male", inline=False)
      embed.add_field(name="Age", value=f"{r['age']}", inline=True)
      embed.set_image(url=f'{r["image_url"]}')
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed)
    elif gender.lower() in female_wl:
      r = requests.get("https://fakeface.rest/face/json?gender=female").json()
      embed2=discord.Embed(title="Here is your generated face", color=0xff0000)
      embed2.add_field(name="Name", value=f"{fake.first_name_female()} {fake.last_name_female()}", inline=False)
      embed2.add_field(name="Gender", value="Female", inline=False)
      embed2.add_field(name="Age", value=f"{r['age']}", inline=True)
      embed2.set_image(url=f'{r["image_url"]}')
      embed2.set_footer(text=f"Requested by {ctx.author.name}")
      await loading_message.delete()
      await ctx.send(embed=embed2)
    else:
      r = requests.get("https://fakeface.rest/face/json").json()
      embed3=discord.Embed(title="Here is your generated face", color=0xff0000)
      if r['gender'] == "male":
        embed3.add_field(name="Name", value=f"{fake.first_name_male()} {fake.last_name_male()}", inline=False)
      elif r['gender'] == "female":
        embed3.add_field(name="Name", value=f"{fake.first_name_female()} {fake.last_name_female()}", inline=False)
      else:
        pass
      embed3.add_field(name="Gender", value=f"{r['gender']}", inline=False)
      embed3.add_field(name="Age", value=f"{r['age']}", inline=True)
      embed3.set_image(url=f'{r["image_url"]}')
      embed3.set_footer(text=f"Requested by {ctx.author.name}")

    #   Deleting the loading message
      await loading_message.delete()
      await ctx.send(embed=embed3)

  except Exception as e:
    embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
    embed3.set_author(name="YourBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/879295069834850324/Avatar.png")
    embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    embed3.add_field(name="Error:", value=f"{e}", inline=False)
    embed3.set_footer(text=f"Requested by {ctx.author.name}")

    #   Deleting the loading message
    await loading_message.delete()
    await ctx.send(embed=embed3)
