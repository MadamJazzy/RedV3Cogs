"""Package for ReverseImage cog."""
from .revimg import ReverseImage


def setup(bot):
    bot.add_cog(ReverseImage(bot))
