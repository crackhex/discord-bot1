import discord
from discord.ext import commands


class RoleRemoveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_roles=True)
    @commands.command(name='roleremove')
    async def roleremove(self, ctx, role: discord.Role, member: discord.Member = None):
        if not role >= ctx.author.top_role or ctx.author == ctx.guild.owner:
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(f"Role successfully removed.")
            else:
                await ctx.send("Member doesn't have that role.")

def setup(bot):
    bot.add_cog(RoleRemoveCog(bot))
