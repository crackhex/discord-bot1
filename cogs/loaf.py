import discord
from discord.ext import commands
import random


class LoafCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='loaf')
    async def loaf(self, ctx):
        rand = random.randint(1, 2)
        if rand == 1:
            await ctx.send(':bread:')
        else:
            await ctx.send(':french_bread:')


def setup(bot):
    bot.add_cog(LoafCog(bot))
