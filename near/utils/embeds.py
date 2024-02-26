import discord
from near.database.db import Embeds


def Error(interaction: discord.Interaction, error_message: str) -> discord.Embed:
    db_error = Embeds.ErrorEmbed()
    db_common = Embeds.CommonEmbed()
    embed = discord.Embed(
        title=db_error["error_title"],
        description=db_error["error_description"],
        color=0x0000FF,
    )
    embed.set_author(
        name=db_common["common_author_name"], icon_url=db_common["common_author_url"]
    )
    embed.set_thumbnail(url=db_error["error_thumbnail"])
    embed.add_field(
        name=db_error["error_feild_name"], value=f"{error_message}", inline=False
    )
    embed.set_footer(text=f"Requested by {interaction.user.name}")
