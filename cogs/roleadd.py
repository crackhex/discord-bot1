import discord
from discord.ext import commands


class RoleAddCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_roles=True)
    @commands.command(name='roleadd')
    async def roleadd(self, ctx, role: discord.Role, member: discord.Member = None):
        if not role >= ctx.author.top_role or ctx.author == ctx.guild.owner:
            if role in member.roles:
                await ctx.send("Member already has that role.")
            else:
                await member.add_roles(role)
                await ctx.send(f"Role successfully added.")


def setup(bot):
    bot.add_cog(RoleAddCog(bot))
