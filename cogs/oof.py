import discord
from discord.ext import commands


class OofCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='oof')
    async def oof(self, ctx):
        await ctx.send('o0f')


def setup(bot):
    bot.add_cog(OofCog(bot))
