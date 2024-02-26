import typing as t

import discord
from near.database.db import Embeds
from near.utils.input_sanitization import color


def Error(interaction: discord.Interaction, error_message: str) -> discord.Embed:
    db_error = Embeds.ErrorEmbed()
    db_common = Embeds.CommonEmbed()
    embed = discord.Embed(
        title=db_error["error_title"],
        description=db_error["error_description"],
        color=color(db_error["error_color"]),
    )
    embed.set_author(
        name=db_common["common_author_name"], icon_url=db_common["common_author_url"]
    )
    embed.set_thumbnail(url=db_error["error_thumbnail"])
    embed.add_field(
        name=db_error["error_feild_name"], value=f"{error_message}", inline=False
    )
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    return embed


def Common(
    interaction: discord.Interaction,
    title: str,
    description: t.Optional[str | list | bool] = False,
    thumbnail: t.Optional[str] = "",
) -> discord.Embed:

    db_common = Embeds.CommonEmbed()

    if description == False:  # dont add description
        embed = discord.Embed(
            title=title,
            color=color(db_common["common_color"]),
        )
    else:  # add description
        embed = discord.Embed(
            title=title,
            description=(
                "".join(description) if isinstance(description, list) else description
            ),
            color=color(db_common["common_color"]),
        )
    embed.set_author(
        name=db_common["common_author_name"], icon_url=db_common["common_author_url"]
    )
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    return embed


def Fake(
    interaction: discord.Interaction,
    description: str | list,
) -> discord.Embed:

    db_fake = Embeds.FakeEmbed()
    db_common = Embeds.CommonEmbed()

    embed = discord.Embed(
        title=db_fake["fakeinfo_title"],
        description=(
            "".join(description) if isinstance(description, list) else description
        ),
        color=color(db_fake["fakeinfo_color"]),
    )
    embed.set_author(
        name=db_common["common_author_name"], icon_url=db_common["common_author_url"]
    )
    embed.set_thumbnail(url=db_fake["fakeinfo_thumbnail"])
    embed.set_footer(text=f"Requested by {interaction.user.name}")
    return embed


def PleaseWait(
    interaction: discord.Interaction,
) -> discord.Embed:

    db_please_wait = Embeds.PleaseWaitEmbed()
    db_common = Embeds.CommonEmbed()

    embed = discord.Embed(
        title=db_please_wait["pleasewait_title"],
        description=db_please_wait["pleasewait_description"],
        color=color(db_please_wait["pleasewait_color"]),
    )
    embed.set_author(
        name=db_common["common_author_name"], icon_url=db_common["common_author_url"]
    )
    embed.set_thumbnail(url=db_please_wait["pleasewait_thumbnail"])
    embed.set_footer(
        text=str(db_please_wait["pleasewait_footer"]).format(
            username=interaction.user.name
        )
    )
    return embed
