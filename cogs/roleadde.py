import discord
from discord.ext import commands


class RoleAddeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roleadde')
    async def roleadde(self, ctx, role=None, member: discord.Member = None):
        if ctx.author.id == 464366551194402817:
            if role is None and member is None:
                await ctx.send("You must specify a role.")
            elif member is None:
                await ctx.send("You must specify a member.")
            elif member is not None:
                roleadd = discord.utils.get(member.guild.roles, name=role)
                await member.add_roles(roleadd, reason=None)
                await ctx.send(f"Role successfully added.")
        else:
            pass


def setup(bot):
    bot.add_cog(RoleAddeCog(bot))
