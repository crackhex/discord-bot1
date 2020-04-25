import discord
from discord.ext import commands


class CookieCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cookie')
    async def cookie(self, ctx):
        await ctx.send(":cookie:")


def setup(bot):
    bot.add_cog(CookieCog(bot))
