import discord
from discord.ext import commands
from near.database import get_embeds

def Error(interaction: discord.Interaction, client: commands.Bot, error_message: str):
    embed = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
    embed.set_author(name=f"{client.user.name}", icon_url=f"{client.user.avatar.url}")
    embed.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
    embed.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{error_message}", inline=False)
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    return embed