import discord
from discord.ext import commands


class ModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mod')
    async def mod(self, ctx):
        if 418160786297323521 in [role.id for role in ctx.author.roles]:
            member = ctx.author
            role = discord.utils.get(ctx.guild.roles, name='Mod')
            await member.add_roles(role)
            await ctx.send('You now have the role Mod')
        else:
            await ctx.send('You do not have permission to use that command')


def setup(bot):
    bot.add_cog(ModCog(bot))
