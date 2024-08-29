import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
from loguru import logger

from near.utils import embeds
from near.utils import errors


class Administration(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(
        name="move", description="Move everyone from one voice channel to another"
    )
    @commands.guild_only()
    @has_permissions(move_members=True)
    @app_commands.describe(channel_to="Voice channel to move the members to")
    @app_commands.describe(channel_from="Voice channel to move the members from")
    async def move(self,interaction: discord.Interaction,channel_to: discord.VoiceChannel,channel_from: discord.VoiceChannel = None):
        logger.info(f"Command invoked by {interaction.user.name} ({interaction.user.id}) in {interaction.guild} ({interaction.guild_id})")
        try:
            
            if channel_from is None: # vc not given
                if not interaction.user.voice: # user not in vc
                    raise errors.CommandError("No value set to `channel_from`. Please pass it in manually or join a voice channel.")
                    return
                else: # user in vc
                    channel_from = interaction.user.voice.channel
            # else: 
                # vc is given

            if channel_to == channel_from:
                raise errors.CommandError(
                    "You can't move to the channel you are already in."
                )
                return

            if not isinstance(channel_from, discord.VoiceChannel) or not isinstance(channel_to, discord.VoiceChannel):
                raise errors.CommandError("Both channels must be voice channels.")
                return

            if not interaction.user.guild_permissions.move_members:
                raise errors.CommandError("Sorry, you don't have permission to do that.")

            members_to_move = channel_from.members
            for member in members_to_move:
                await member.move_to(channel_to)

            embed = embeds.Common(
                client=self.client,
                interaction=interaction,
                title="Moved members!",
                description=f"Moved members from {channel_from.mention} to {channel_to.mention}.",
            )
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            await interaction.response.send_message(embed=embeds.Error(interaction=interaction, client=self.client, error_message=f"{e}"),ephemeral=False)


async def setup(client: commands.Bot):
    await client.add_cog(Administration(client))
