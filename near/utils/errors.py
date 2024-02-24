import functools
import discord
from near.database import get_embeds
from near.database.get_embeds import ErrorEmbeds

def handle_error(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            return result
        except Exception as e:
            interaction = None
            if 'interaction' in kwargs:
                interaction = kwargs['interaction']
            elif len(args) > 0 and hasattr(args[0], 'interaction'):
                interaction = args[0].interaction
            if interaction:
                embd = ErrorEmbeds()
                # FIX IT
                embed = discord.Embed(title=embd['error_title'], description=embd['error_description'], color=0x0000ff)
                embed.set_author(name=embd['common_author_name'], icon_url=embd['common_author_url'])
                embed.set_thumbnail(url=embd['error_thumbnail'])
                embed.add_field(name=embd['error_feild_name'], value=f"{e}", inline=False)
                embed.set_footer(text=f"Requested by {interaction.user.name}")
                await interaction.response.send_message(embed=embed)
            else:
                print("Error: {}".format(str(e)))
    return wrapper

class IllegalInput(Exception):
    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return f"Illegal Input Passed to the bot as an argument{': ' + str(self.message) if not(self.message is None) else '.'}"
