import discord
from discord.ext import commands


class PictureCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='picture')
    async def picture(self, ctx):
        await ctx.send(file=discord.File("Tulip.jpg"))


def setup(bot):
    bot.add_cog(PictureCog(bot))
