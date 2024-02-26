import functools
import discord
from near.utils import embeds


def handle_error(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            return result
        except Exception as e:
            interaction = None
            if "interaction" in kwargs:
                interaction = kwargs["interaction"]
            elif len(args) > 0 and hasattr(args[0], "interaction"):
                interaction = args[0].interaction
            if interaction:
                embed = embeds.Error(interaction=interaction, error_message=f"{e}")
                await interaction.response.send_message(embed=embed)
            else:
                print("Error: {}".format(str(e)))

    return wrapper


class IllegalInput(Exception):
    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return f"Illegal Input Passed to the bot as an argument{': ' + str(self.message) if not(self.message is None) else '.'}"
