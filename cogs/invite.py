import discord
from discord.ext import commands


class InviteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='invite')
    async def invite(self, ctx):
        await ctx.send("Sent an invite template in your DMs!")
        await ctx.author.send(
            "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n☣RadiationCraft☣\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \nWhat we offer:\n☣ Active Staff Team ☣\n"
            "☣ Fair, safe, fun, and kind environment ☣\n☣ OP Factions ☣\n☣ Custom Enchants ☣\n☣ "
            "1st Place: $50 Buycraft ☣\n☣ 2nd Place: $30 Buycraft ☣\n☣ 3rd Place: $20 Buycraft ☣\n☣ "
            "Total of $100 Buycraft ☣\n☣ We do giveaways for ranks, items, and vouchers! ☣\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
            "☣ Apply for any rank you wish, make it detailed and put effort into it. "
            "You will get accepted for sure! Spots are limited and we are looking for mature and fun people! ☣\n"
            "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n☣Forums: https://radiationcraft.enjin.com/ ☣\n"
            "☣ Store: On Site☣\n☣ IP: radiation.mcserv.co ☣\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
            "☣ Join Now! https://discord.gg/QGpfuw2 ☣")


def setup(bot):
    bot.add_cog(InviteCog(bot))
