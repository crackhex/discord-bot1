import discord
from discord.ext import commands
import json


class LogToCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.command(name='logto')
    async def logto(self, ctx, channel: discord.TextChannel):
        with open("logs.json", "r") as f:
            logs = json.load(f)
        if str(ctx.guild.id) not in logs:
            await ctx.send(f"Logging to {channel.mention}")
            logs.update({str(ctx.guild.id): channel.id})
        elif channel.id != logs[str(ctx.guild.id)]:
            await ctx.send(f"Logging to {channel.mention}")
            logs.update({str(ctx.guild.id): channel.id})
        else:
            await ctx.send("`logs` is already set to that channel.")
        with open("logs.json", "w") as f:
            json.dump(logs, f, indent=4)


def setup(bot):
    bot.add_cog(LogToCog(bot))
