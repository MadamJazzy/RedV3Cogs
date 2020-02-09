"""Package for ReverseImage cog."""
from .revimg import ReverseImage


async def setup(bot):
    """Load ReverseImage cog."""
    cog = ReverseImage(bot)
    await cog.initialize()
    bot.add_cog(cog)
