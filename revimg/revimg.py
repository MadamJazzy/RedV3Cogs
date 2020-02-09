import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import error, info

__author__ = "MadamJazzy"
__version__ = "1.0.0"

class ReverseImage(commands.Cog):
    """Lookup an image on several common reverse search services!"""
    @commands.command()
    async def revimg(self, ctx, url=None):
        """
        Reverse image search!
        usage:  [p]revimg <image-link>
        """

        sauce = f'https://saucenao.com/search.php?url={url}'
        google = f'https://www.google.com/searchbyimage?&image_url={url}'
        tineye = f'https://www.tineye.com/search?url={url}'
        iqbd = f'https://iqdb.org/?url={url}'
        yandex = f'https://yandex.com/images/search?url={url}&rpt=imageview'
        embed = discord.Embed(title='Reverse Image Details', color=16776960)
        if url is None:
            return await ctx.send(info("I need a image URL to search for!"))
        await ctx.message.delete()
        embed.add_field(name="Sauce", value=f'[Sauce Image Results]({sauce})', inline=False)
        embed.add_field(name="Google", value=f'[Google Image Results]({google})', inline=False)
        embed.add_field(name="TinEye", value=f'[Tineye Image Results]({tineye})', inline=False)
        embed.add_field(name="IQBD", value=f'[IQBD Image Results]({iqbd})', inline=False)
        embed.add_field(name="Yandex", value=f'[Yandex Image Results]({yandex})', inline=False)
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
