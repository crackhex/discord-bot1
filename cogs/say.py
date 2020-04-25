import discord
from discord.ext import commands


class SayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='say')
    async def say(self, ctx, *args):
        if args == ():
            await ctx.send('Please put something to say')
        else:
            await ctx.message.delete()
            await ctx.send((" ".join(args[0:])))


def setup(bot):
    bot.add_cog(SayCog(bot))
