from .music import Music
from .events import MusicEvents
from discord.ext import commands


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
    await bot.add_cog(MusicEvents(bot))


__version__ = "1.0.1"
