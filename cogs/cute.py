import discord
from discord.ext import commands
import random


class CuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cute(self, ctx, *args):
        rando = str(random.randint(1, 100))
        if args == ():
            await ctx.send(f'You are {rando}% cute')
        else:
            await ctx.send(((('%s ' % ' '.join(args[0:])) + 'is ') + rando) + '% cute')


def setup(bot):
    bot.add_cog(CuteCog(bot))
