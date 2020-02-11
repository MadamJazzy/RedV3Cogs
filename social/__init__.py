"""Package for Social cog."""
from .social import Social


def setup(bot):
    bot.add_cog(Social(bot))
