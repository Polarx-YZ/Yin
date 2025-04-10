import discord
import random
from discord.ext import commands

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["dice",], brief="Roll a dice", description="Rolls a six-sided die by default", usage="`optional: number of sides`")
    async def roll(self, ctx, arg=6):
        
        if int(arg) <= 0:
            await ctx.reply ("You can't roll a dice that has zero or less sides!")
        
        max = int(arg)
        
        if isinstance(max, int):
            await ctx.reply(f"You rolled a {random.randint(1, max)}!")
        else:
            await ctx.reply("You need to specify the amount of sides!")
        
async def setup(bot):
    await bot.add_cog(Dice(bot))