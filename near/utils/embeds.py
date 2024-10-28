from datetime import datetime
import typing as t

import discord
from discord.ext import commands
from loguru import logger

from near.database import get_embeds
from near.database import dbfetch
from near.utils import input_sanitization

async def Error(client: commands.Bot, interaction: discord.Interaction, error_message: str) -> discord.Embed:
    """
    Generate an error embed given an error message.
    
    Parameters:
    -----------
    client: commands.Bot
        The bot instance.
    interaction: discord.Interaction
        The interaction which invoked the error.
    error_message: str
        The error message to be embedded and sent.
    
    Returns:
    --------
    discord.Embed
        An embed containing the error message and the interaction user.
    """
    
    logger.error(error_message)
    embed_info = await dbfetch.DataEmbedsFetcher.allError()
    embed = discord.Embed(title=embed_info['ERROR_TITLE'], description=f"```\n{error_message}```", color=input_sanitization.color(embed_info['ERROR_COLOR']), timestamp=datetime.utcnow())
    embed.set_author(name=f"{client.user.name}", icon_url=f"{client.user.avatar.url}")
    embed.set_thumbnail(url=embed_info['ERROR_THUMBNAIL'])
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    return embed

async def Common(client: commands.Bot, interaction: discord.Interaction, title: str, description: t.Optional[str | list | bool] = False, thumbnail: t.Optional[str] = "",) -> discord.Embed:
    """
    Create a common embed with a title and optional description and thumbnail.
    
    Parameters
    ----------
    client : commands.Bot
        The bot instance.
    interaction : discord.Interaction
        The interaction for which the embed is being created.
    title : str
        The title of the embed.
    description : str | list | bool, optional
        The description of the embed. If it's a list, the elements are joined.
        If False, no description is added. Defaults to False.
    thumbnail : str, optional
        URL of the thumbnail image to be added to the embed. Defaults to an empty string.
    
    Returns
    -------
    discord.Embed
        An embed with the specified title, optional description, and thumbnail.
    """
    
    if description == False:            # dont add description
        embed = discord.Embed(
            title=title,
            color=get_embeds.Common.COLOR,
            timestamp=datetime.utcnow()
        )
    else:                               # add description
        embed = discord.Embed(
            title=title,
            description=(
                "".join(description) if isinstance(description, list) else description
            ),
            color=get_embeds.Common.COLOR,
            timestamp=datetime.utcnow()
        )
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    return embed
