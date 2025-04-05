import discord
import random
from discord.ext import commands
import difflib

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def rps(self, ctx, arg=None):
        choices = ["rock", "paper", "scissors"]
        
        original_choice = arg
        
        arg = "".join(difflib.get_close_matches(arg, choices, 1, 0.5))
        
        if (arg == None):
            return await ctx.reply("You need to choose rock, paper, or scissors!")
        
        if arg in choices:
            user = choices.index(arg.lower())
        else:
            return await ctx.reply(f"`{original_choice}` is not an option! Pick rock, paper, or scissors!")
        
        comp = random.randint(0,2)
        winner = (comp-user)%3
        
        if winner == 0:
            await ctx.reply(f"There was a tie! We both chose {choices[user]}!")
        elif winner == 1:
            await ctx.reply(f"I won! You chose {choices[user]} and I chose {choices[comp]}!")
        else:
            await ctx.reply(f"You win! You chose {choices[user]} and I chose {choices[comp]}!")
            
        

        
async def setup(bot):
    await bot.add_cog(Games(bot))