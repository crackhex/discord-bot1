import discord
from discord.ext import commands


class MassOofCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='massoof')
    async def massoof(self, ctx):
        await ctx.send("  o0f o0f o0f o0f o0f \n o0f o0f o0f o0f o0f \n o0f o0f o0f o0f o0f \n o0f o0f o0f o0f o0f \n "
                       "o0f o0f o0f o0f o0f \n o0f o0f o0f o0f o0f \n o0f o0f o0f o0f o0f \n o0f o0f o0f o0f o0f \n o0f"
                       " o0f o0f o0f o0f \n o0f o0f o0f o0f o0f \n o0f o0f o0f o0f o0f \n o0f o0f o0f o0f o0f")


def setup(bot):
    bot.add_cog(MassOofCog(bot))
