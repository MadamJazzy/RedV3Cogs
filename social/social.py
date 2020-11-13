import discord
from redbot.core import commands
from redbot.core.data_manager import cog_data_path as datapath
import random
import yaml


class Social(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def embed_maker(self, ctx, action, user, sender):
        d = datapath(self)
        embed = discord.Embed()
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
        baseurl = "http://hardinserver.com/social/"
        url = f'{baseurl}{action}/{action}{num}{filetype}'
        embed.title = msg.format(sender, user)
        if user != sender:
            embed.set_image(url=url)
        return embed

    @commands.command(pass_context=True, invoke_without_command=True)
    async def kiss(self, ctx, *, user: discord.Member):
        """Kiss people!"""
        action = "kiss"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def bite(self, ctx, *, user: discord.Member):
        """Bite people!"""
        action = "bite"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def slap(self, ctx, *, user: discord.Member):
        """Slap people!"""
        action = "slap"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def taunt(self, ctx, *, user: discord.Member):
        """Taunt people!"""
        action = "taunt"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def cuddle(self, ctx, *, user: discord.Member):
        """Cuddle people!"""
        action = "cuddle"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def hugs(self, ctx, *, user: discord.Member):
        """Hug people!"""
        action = "hug"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def feed(self, ctx, *, user: discord.Member):
        """Feed people!"""
        action = "feeds"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def spank(self, ctx, *, user: discord.Member):
        """Spank people!"""
        action = "spank"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def tease(self, ctx, *, user: discord.Member):
        """Tease people!"""
        action = "tease"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def hi5(self, ctx, *, user: discord.Member):
        """HighFive people!"""
        action = "hi5"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def shoot(self, ctx, *, user: discord.Member):
        """Shoot people!"""
        action = "shoot"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def lick(self, ctx, *, user: discord.Member):
        """Lick people!"""
        action = "lick"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def shake(self, ctx, *, user: discord.Member):
        """Handshake!"""
        action = "handshake"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def twerk(self, ctx, *, user: discord.Member):
        """TWERK!"""
        action = "twerk"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def strip(self, ctx, *, user: discord.Member):
        """STRIP!"""
        action = "strip"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def thirsty(self, ctx, *, user: discord.Member):
        """The Thirst is Real!"""
        action = "thirsty"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def moist(self, ctx, *, user: discord.Member):
        """Moist lol!"""
        action = "moist"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def whip(self, ctx, *, user: discord.Member):
        """Whip someone!"""
        action = "whip"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def facepalm(self, ctx, *, user: discord.Member):
        """Facepalm images!"""
        action = "facepalm"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def ohno(self, ctx, *, user: discord.Member):
        """Oh no they didnt images!"""
        action = "ono"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def hungry(self, ctx, *, user: discord.Member):
        """Hungry images!"""
        action = "hungry"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def nuts(self, ctx, *, user: discord.Member):
        """NutCracker images!"""
        action = "nuts"
        await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))

    @commands.command(pass_context=True, invoke_without_command=True)
    async def fever(self, ctx):
        """Do you have the Fever?"""
        action = "fever"
        user = ctx.message.author
        try:
            await ctx.send(embed=self.embed_maker(ctx, action, user, sender=ctx.message.author))
        except KeyError:
            await ctx.send("Looks like you included a user! This command doesn't need that. Just use `fever` by itself.")

    @commands.command(pass_context=True, invoke_without_command=True)
    async def socialcmds(self, ctx):
        """List all Social Commands"""
        embed = discord.Embed(title="Social Commands!")
        list = ["kiss", "bite", "slap", "taunt", "cuddle", "hugs", "feed", "spank", "tease", "hi5", "shoot", "lick",
                "shake", "shoot", "twerk", "strip", "thirsty", "moist", "whip", "facepalm", "ohno", "hungry", "nuts",
                "fever", "socialcmds"]
        for x in list:
            embed.add_field(name=x, value=f"[p]{x} @username", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Social(bot))
