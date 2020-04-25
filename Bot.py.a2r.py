import discord
from discord.ext import commands
import random
import sys
import traceback
import json


def prefix(bot, message):
    with open("prefixes.json") as f:
        prefixes = json.load(f)
    id = message.guild.id
    if str(id) in prefixes:
        return prefixes[str(id)]
    else:
        return "~"


initial_extensions = ['cogs.cookie',
                      'cogs.roleadd',
                      'cogs.roleremove',
                      'cogs.help',
                      'cogs.massoof',
                      'cogs.ping',
                      'cogs.invite',
                      'cogs.purge',
                      'cogs.prefix',
                      'cogs.logto',
                      'cogs.speak',
                      'cogs.say',
                      'cogs.mod',
                      'cogs.loaf',
                      'cogs.oof',
                      'cogs.cute',
                      'cogs.roleadde',
                      'cogs.roleremovee',
                      'cogs.picture']


client = discord.Client()
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command("help")

for extension in initial_extensions:
    try:
        bot.load_extension(extension)
    except ModuleNotFoundError:
        print(f'Failed to load extension {extension}.', file=sys.stderr)
        traceback.print_exc()


@bot.event
async def on_ready():
    activity = discord.Activity(type=3, name="For Help", url='https://www.twitch.tv/ There is no god lmao')
    await bot.change_presence(activity=activity)
    print('Bot is ready!')


@commands.has_permissions(manage_messages=True)
@bot.command(ignore_extra=False)
async def evsay(ctx, amount, *args):
    userid = ctx.author.id
    theamount = int(amount)
    uptoamount = 0
    if amount.isdigit():
        if int(amount) < 1:
            raise ValueError
        else:
            if args == ():
                raise TabError
            else:
                @bot.event
                async def on_message(message):
                    user = message.author.id
                    if message.author.id == 491795532004589568:
                        pass
                    else:
                        nonlocal userid
                        nonlocal uptoamount
                        nonlocal theamount
                        if message.content.upper() == "STOP" and userid == user:
                            uptoamount = theamount
                            await ctx.send("It finished")
                            await bot.process_commands(message)

                        else:
                            if theamount > uptoamount:
                                await message.delete()
                                uptoamount += 1
                                await message.channel.send(f"<@{user}> Said: " + (" ".join(args[0:])))
                            if uptoamount == theamount:
                                await ctx.send("It finished")
                                uptoamount += 1
                                await bot.process_commands(message)
                            else:
                                pass
                                await bot.process_commands(message)
                            await bot.process_commands(message)
                        await bot.process_commands(message)
                    await bot.process_commands(message)
    else:
        raise TypeError


@evsay.error
async def evsay_handler(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        if isinstance(error.original, ValueError):
            await ctx.send("`amount` can't be smaller than 1.")
        elif isinstance(error.original, TypeError):
            await ctx.send("`amount` is not a digit.")
        elif isinstance(error.original, TabError):
            await ctx.send("`args` is a required argument that's missing.")
    elif isinstance(error, commands.MissingRequiredArgument):
        if error.param.name == 'amount':
            await ctx.send("`amount` is a required argument that's missing.")
    elif isinstance(error, commands.MissingPermissions):
        return await ctx.send(f'You lack permissions to execute `{bot.command_prefix}{ctx.command}`.')
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


@bot.event
async def on_message(message):
    if message.content.lower() == "johnny johnny":
            with open("gay.json", "r") as filegay:
                users = json.load(filegay)
            if str(message.guild.id) not in users or users[str(message.guild.id)][str(message.author.id)] not in users[str(message.author.id)]:
                with open("gay.json", "r+") as filegay:
                    users = json.load(filegay)
                    users.update({str(message.guild.id): {str(message.author.id): "yes"}})
                    filegay.seek(0)
                    json.dump(users, filegay, indent=4)
                    filegay.truncate()
                await message.channel.send("Yes, papa?")

                def check(m):
                    return m.content.endswith("?")\
                           and len(m.content) != 11\
                           and m.channel == message.channel\
                           and m.author == message.author

                def check2(m):
                    return m.content.lower() == "telling lies?"\
                           and m.channel == message.channel\
                           and m.author == message.author

                def check3(m):
                    return m.content.lower() == "open wide"\
                           and m.channel == message.channel\
                           and m.author == message.author
 
                await bot.wait_for("message", check=check)
                await message.channel.send("No, papa...")
                await bot.wait_for("message", check=check2)
                await message.channel.send("No, papa...")
                await bot.wait_for("message", check=check3)
                await message.channel.send("aah aah aaaaah")
                with open("gay.json", "r+") as filegay:
                    users = json.load(filegay)
                    users[str(message.guild.id)].pop(str(message.author.id))
                    if len(users[str(message.guild.id)]) == 0:
                        users.pop(str(message.guild.id))
                    filegay.seek(0)
                    json.dump(users, filegay, indent=4)
                    filegay.truncate()
    await bot.process_commands(message)

@bot.event
async def on_command_completion(ctx):
    color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    with open("logs.json", "r") as f:
        logs = json.load(f)
        if str(ctx.guild.id) in logs:
            channel = bot.get_channel(logs[str(ctx.guild.id)])
            embed = discord.Embed(title="Command Execution", description=f"{ctx.author.mention} Executed the Command "
                                                                         f"`{ctx.message.content}`", color=color)
            await channel.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
        return
    ignored = ()
    error = getattr(error, 'original', error)
    if isinstance(error, ignored):
        return
    elif isinstance(error, commands.MissingPermissions):
        return await ctx.send(f'You lack permissions to execute `{bot.command_prefix(bot, ctx.message)}{ctx.command}`.')
    elif isinstance(error, commands.NotOwner):
        return await ctx.send(f'Only the bot owner has permission to execute `{bot.command_prefix}{ctx.command}`.')
    elif isinstance(error, commands.CommandNotFound):
        return await ctx.send(f"Please type like an actual command.")
    print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


bot.run('NDkxNzk1NTMyMDA0NTg5NTY4.DoNEVg.NWCYdeRna_BRkTNYYsyIFknLW0g')
