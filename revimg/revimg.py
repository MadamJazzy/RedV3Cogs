import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import error, info

__author__ = "MadamJazzy"
__version__ = "1.0.0"

class ReverseImage(commands.Cog):
    """Lookup an image on several common reverse search services!"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def revimg(self, ctx, url=None):
        """
        Reverse image search!
        usage:  [p]revimg <image-link> or file upload
        """
        if url is not None:
            await ctx.message.delete()
        if url is None:
            url = ctx.message.attachments[0].url
        embed = discord.Embed(title='Reverse Image Details', color=16776960)
        embed.add_field(name="Sauce", value=f'[Sauce Image Results](https://saucenao.com/search.php?url={url})', inline=True)
        embed.add_field(name="Google", value=f'[Google Image Results](https://www.google.com/searchbyimage?&image_url={url})', inline=True)
        embed.add_field(name="TinEye", value=f'[Tineye Image Results](https://www.tineye.com/search?url={url})', inline=True)
        embed.add_field(name="IQBD", value=f'[IQBD Image Results](https://iqdb.org/?url={url})', inline=True)
        embed.add_field(name="Yandex", value=f'[Yandex Image Results](https://yandex.com/images/search?url={url}&rpt=imageview)', inline=True)
        await ctx.send(embed=embed)

    @staticmethod
    async def send_embed(ctx, embed):
        """Send an embed. If the bot can't send it, complains about permissions."""
        try:
            await ctx.send(embed=embed)
            return True
        except discord.HTTPException:
            await ctx.send(
                error("I need the `Embed links` permission to function properly")
            )
            return False
