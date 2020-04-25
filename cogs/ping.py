import discord
from discord.ext import commands


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f'<@{ctx.author.id}> Pong!')


def setup(bot):
    bot.add_cog(PingCog(bot))
