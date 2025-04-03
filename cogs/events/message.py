import discord
from discord.ext import commands
from settings import config
import re


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot:
            return

        dad_triggers = ["i'm", "am", "im"]

        # Checks if any dad_triggers are in the message and stores the string that triggered it
        # TODO Fix it so that it starts the message after the "I am" It will start at a word earlier if it has "am" or "im" in it like "imagine"
        dad_trigger = next((trigger for trigger in dad_triggers if any(x in trigger for x in ctx.content.split())), None)

        if dad_trigger is not None:
            before, key, after = ctx.content.partition(dad_trigger)
            if key == "":
                return
            await ctx.reply(f"Hi{after}! I'm Dad")


async def setup(bot):
    await bot.add_cog(Message(bot))
