import discord
from discord.ext import commands


class RoleRemoveeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roleremovee')
    async def roleremovee(self, ctx, role=None, member: discord.Member = None):
        if ctx.author.id == 291585359345876993 or ctx.author.id == 464366551194402817:
            if role is None and member is None:
                await ctx.send("You must specify a role.")
            elif member is None:
                await ctx.send("You must specify a member.")
            elif member is not None:
                roleremove = discord.utils.get(member.guild.roles, name=role)
                await member.remove_roles(roleremove, reason=None)
                await ctx.send(f"Role successfully removed.")
        else:
            pass


def setup(bot):
    bot.add_cog(RoleRemoveeCog(bot))
