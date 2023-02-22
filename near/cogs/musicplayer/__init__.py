from .music import Music
from .events import MusicEvents


async def setup(bot):
    await bot.add_cog(Music(bot))
    await bot.add_cog(MusicEvents(bot))


__version__ = "1.0.1"
