import discord
from discord.ext import commands


class PurgeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.command(ignore_extra=False, name='purge')
    async def purge(self, ctx, limit, member: discord.Member = None):
        if limit.isdigit():
            if int(limit) < 1:
                raise ValueError

            else:
                def check(msg: discord.Message) -> bool:
                    return msg == ctx.message or member is None or msg.author == member

                await ctx.channel.purge(limit=int(limit) + 1, bulk=True, check=check)
        else:
            raise TypeError

    @purge.error
    async def purge_handle(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            if isinstance(error.original, ValueError):
                await ctx.send("`limit` can't be smaller than 1.")
            elif isinstance(error.original, TypeError):
                await ctx.send("`limit` is not a digit.")
        elif isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'limit':
                await ctx.send("`limit` is a required argument that's missing.")
        elif isinstance(error, commands.MissingPermissions):
            return await ctx.send(f'You lack permissions to execute `{bot.command_prefix}{ctx.command}`.')
        elif isinstance(error, commands.BadArgument):
            await ctx.send("`member` is invalid. Make sure the member exists in the server.")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send("There are too many arguments. There can only be 2 arguments.")
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(PurgeCog(bot))
