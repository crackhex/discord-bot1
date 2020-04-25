import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

Client = discord.Client()
client = commands.Bot(command_prefix = '~')

@client.event
async def on_ready():
    print("Bot is ready!")
#291585359345876993
@client.event
async def on_message(message):
    if message.content.upper() == client.command_prefix + "PING":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper() == client.command_prefix + "COOKIE":
        await client.send_message(message.channel, ":cookie:")
    if message.content.upper().startswith(client.command_prefix + 'SAY'):
        args = message.content.split(" ")
        if len(args[0]) > 4:
            await client.send_message(message.channel, "Its ~say dummy")
        else:
            if len(message.content) < 5:
                await client.send_message(message.channel, "Please put something to say.")
            else:
                args = message.content.split(" ")
                #args[0] = !SAY
                await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content.upper().startswith(client.command_prefix + 'SPEAK'):
        args = message.content.split(" ")
        if len(args[0]) > 6:
            await client.send_message(message.channel, "Its ~speak dummy")
        else:
            if len(message.content) < 7:
                await client.send_message(message.channel, "Please put something to speak.")
            else:
                args = message.content.split(" ")
                userID = message.author.id
                #args[0] = !SAY
                await client.send_message(message.channel, "<@%s>" % (userID) + " Said: " + "%s" % (" ".join(args[1:])))
    if message.content.upper() == client.command_prefix + "ME":
        if message.author.id == '291585359345876993':
            await client.send_message(message.channel, "Hello EpicHacker")
        else:
            await client.send_message(message.channel, "You aren't EpicHacker")
    if message.content.upper() == client.command_prefix + "AMIADMIN":
        if "418160786297323521" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "Hello Admin")
        else:
            await client.send_message(message.channel, "You aren't Admin")

    if message.content.upper() == client.command_prefix + "MOD":
        if "418160786297323521" in [role.id for role in message.author.roles]:
            member = message.author
            role = discord.utils.get(member.server.roles, name="Mod")
            await client.add_roles(member, role)
            await client.send_message(message.channel, "You now have the role Mod")
        else:
            await client.send_message(message.channel, "You do not have permission to use this command.")
    if message.content.upper() == client.command_prefix + "OOF":
        await client.send_message(message.channel, "o0f")
    if message.content.upper() == client.command_prefix + "LOAF":
        for x in range(10):
            rand = random.randint(1,2)
        if rand == 1:
            await client.send_message(message.channel, ":bread:")
        else:
            await client.send_message(message.channel, ":french_bread:")
    if message.content.upper().startswith(client.command_prefix + "CUTE"):
        args = message.content.split(" ")
        if len(args[0]) > 5:
            await client.send_message(message.channel, "The command is ~cute dummy")
        else:
            args = message.content.split(" ")
            for x in range(10):
                randoi = random.randint(1,100)
            rando = str(randoi)
            if message.author.id == '292065503084544000':
                if len(message.content) < 6:
                    await client.send_message(message.channel, "You are " + rando  + "% cute")
                else:
                    await client.send_message(message.channel, "%s " % (" ".join(args[1:])) + "is " + rando + "% cute")
            else:
                if len(message.content) < 6:
                    await client.send_message(message.channel, "You are " + rando + "% cute")
                else:
                    await client.send_message(message.channel, "%s " % (" ".join(args[1:])) + "is " + rando + "% cute")

    if message.content.upper() == client.command_prefix + "HELP":
        await client.send_message(message.channel, "```css\n Prefix - ~ \n List of commands: \n help - show list of commands \n cookie - cookie \n loaf - loaf \n oof - o0f \n say - has the bot say something \n speak - has the bot say what you said while mentioning you \n cute - cuteness meter \n amiadmin - Am I admin? \n mod - gives yourself mod if you are admin \n That is the end of the help list! \n If you want any more commands, request them in #music. \n Have a great day! ```")


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, role)

client.run("NDc4Mzg1NTkyNTQ0MDAyMDQ5.DlJ8sg.VkrWjFIQe9xzYwHj6ylZivnm5FY")
