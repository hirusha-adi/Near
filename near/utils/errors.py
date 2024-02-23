import functools
import discord
from near.database import get_embeds

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
                embed = discord.Embed(title=get_embeds.ErrorEmbeds.TITLE, description=get_embeds.ErrorEmbeds.DESCRIPTION, color=get_embeds.ErrorEmbeds.COLOR)
                embed.set_author(name=f"Near", icon_url=f"https://user-images.githubusercontent.com/36286877/208341567-6706e40f-03b5-4e29-836c-760708f2e619.png")
                embed.set_thumbnail(url=get_embeds.ErrorEmbeds.THUMBNAIL)
                embed.add_field(name=get_embeds.ErrorEmbeds.FIELD_NAME, value=f"{e}", inline=False)
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
