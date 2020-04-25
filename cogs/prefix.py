import discord
from discord.ext import commands
import json

class PrefixCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.command(name='prefix')
    async def prefix(self, ctx, new_prefix):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        if new_prefix == "<@!478385592544002049>":
            new_prefix = "<@!478385592544002049> "
            prefixes.update({str(ctx.guild.id): new_prefix})
            with open("prefixes.json", "w") as f:
                json.dump(prefixes, f)
        elif len(new_prefix) > 3:
            await ctx.send("`prefix` must not be longer than 3 characters")
        elif new_prefix == prefixes:
            await ctx.send(f"`prefix` is already {new_prefix}!")
        else:
            await ctx.send(f"Prefix set to {new_prefix}")
            prefixes.update({str(ctx.guild.id): new_prefix})
            with open("prefixes.json", "w") as f:
                json.dump(prefixes, f)


def setup(bot):
    bot.add_cog(PrefixCog(bot))
