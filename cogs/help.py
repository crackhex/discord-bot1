import discord
from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        await ctx.send(
            '```css\n Prefix - ~ \n List of commands: \n help - show list of commands \n cookie - cookie \n loaf - '
            'loaf \n oof - o0f \n say - has the bot say something \n purge - purges the amount of messages '
            'you specify \n speak - has the bot say what you said while mentioning you '
            '\n cute - cuteness meter \n amiadmin - Am I admin? \n mod - gives yourself mod if you are '
            'admin \n That is the end of the help list! \n If you want any more commands, request them in #music. \n '
            'Have a great day! ```')


def setup(bot):
    bot.add_cog(HelpCog(bot))
