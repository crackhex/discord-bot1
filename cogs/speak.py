import discord
from discord.ext import commands


class SpeakCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='speak')
    async def speak(self, ctx, *args):
        if args == ():
            await ctx.send('Please put something to say')
        else:
            await ctx.message.delete()
            await ctx.send((f"<@{ctx.author.id}> Said: " + " ".join(args[0:])))


def setup(bot):
    bot.add_cog(SpeakCog(bot))
