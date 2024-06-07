from datetime import datetime
import typing as t

import discord
from discord.ext import commands
from loguru import logger

from near.database import get_embeds


def Error(client: commands.Bot, interaction: discord.Interaction, error_message: str) -> discord.Embed:
    logger.error(error_message)
    embed = discord.Embed(title=f"🔴 ERROR 🔴", description=f"```\n{error_message}```", color=get_embeds.ErrorEmbeds.COLOR, timestamp=datetime.utcnow())
    embed.set_author(name=f"{client.user.name}", icon_url=f"{client.user.avatar.url}")
    embed.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    return embed

def Common(client: commands.Bot, interaction: discord.Interaction, title: str, description: t.Optional[str | list | bool] = False, thumbnail: t.Optional[str] = "",) -> discord.Embed:
    if description == False:  # dont add description
        embed = discord.Embed(
            title=title,
            color=get_embeds.Common.COLOR,
            timestamp=datetime.utcnow()
        )
    else:                    # add description
        embed = discord.Embed(
            title=title,
            description=(
                "".join(description) if isinstance(description, list) else description
            ),
            color=get_embeds.Common.COLOR,
            timestamp=datetime.utcnow()
        )
    embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    return embed
