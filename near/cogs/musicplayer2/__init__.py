from ._version import __version__, version_info
from .events import MusicEvents
from .music import Music


def setup(bot):
    bot.add_cog(Music(bot))
    bot.add_cog(MusicEvents(bot))
