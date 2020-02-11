import discord
from redbot.core import commands
from redbot.core.data_manager import cog_data_path as datapath
import random
import yaml


class Social(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def embed_maker(self, ctx, action, user, sender, ):
        d = datapath(self)
        with open(d / 'social.yaml') as f:
            data = yaml.safe_load(f)
        if user == sender:
            msg = data[action]['selfmsg']
        else:
            msg = data[action]['msg']
        num = random.randint(1, int(data[action]['num']))
        if action == "fever":
            filetype = ".jpg"
        else:
            filetype = ".gif"
        baseurl = "http://cdn.hardinserver.com/social/"
        url = f'{baseurl}{action}/{action}{num}{filetype}'
        embed = discord.Embed(title=msg.format(sender.name, user.name))
        embed.set_image(url=url)
        return embed

    @commands.command(pass_context=True, invoke_without_command=True)
    async def kiss(self, ctx, *, user: discord.Member, action="kiss"):
        """Kiss people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def bite(self, ctx, *, user: discord.Member, action="bite"):
        """Bite people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def slap(self, ctx, *, user: discord.Member, action="slap"):
        """Slap people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def taunt(self, ctx, *, user: discord.Member, action="taunt"):
        """Taunt people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def cuddle(self, ctx, *, user: discord.Member, action="cuddle"):
        """Cuddle people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def hugs(self, ctx, *, user: discord.Member, action="hug"):
        """Hug people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def feed(self, ctx, *, user: discord.Member, action="feed"):
        """Feed people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def spank(self, ctx, *, user: discord.Member, action="spank"):
        """Spank people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def tease(self, ctx, *, user: discord.Member, action="tease"):
        """Tease people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def hi5(self, ctx, *, user: discord.Member, action="hi5"):
        """HighFive people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def shoot(self, ctx, *, user: discord.Member, action="shoot"):
        """Shoot people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def lick(self, ctx, *, user: discord.Member, action="lick"):
        """Lick people!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def shake(self, ctx, *, user: discord.Member, action="shake"):
        """Handshake!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def twerk(self, ctx, *, user: discord.Member, action="twerk"):
        """TWERK!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def strip(self, ctx, *, user: discord.Member, action="strip"):
        """STRIP!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def thirsty(self, ctx, *, user: discord.Member, action="thirsty"):
        """The Thirst is Real!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def moist(self, ctx, *, user: discord.Member, action="moist"):
        """Moist lol!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def whip(self, ctx, *, user: discord.Member, action="whip"):
        """Whip someone!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def facepalm(self, ctx, *, user: discord.Member, action="facepalm"):
        """Facepalm images!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def ohno(self, ctx, *, user: discord.Member, action="ono"):
        """Oh no they didnt images!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def hungry(self, ctx, *, user: discord.Member, action="hungry"):
        """Hungry images!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def nuts(self, ctx, *, user: discord.Member, action="nuts"):
        """NutCracker images!"""
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def fever(self, ctx, action="fever"):
        """Do you have the Fever?"""
        user = ctx.message.author
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def socialcmds(self, ctx):
        """List all Social Commands"""
        embed = discord.Embed(title="Social Commands!")
        list = ["kiss", "bite", "slap", "taunt", "cuddle", "hugs", "feed", "spank", "tease", "hi5", "shoot", "lick",
                "shake", "shoot", "twerk", "strip", "thirsty", "moist", "whip", "facepalm", "ohno", "hungry", "nuts",
                "fever", "socialcmds"]
        for x in list:
            embed.add_field(name=x, value=f"{x} someone! [p]{x} @username")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Social(bot))
