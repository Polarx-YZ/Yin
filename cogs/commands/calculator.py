'''
For @SpaceDuck16
'''

import discord
from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def add(self, ctx, *args: int):
        
        sum = args[0]
        
        for num in args[1:]:
            sum += num
        
        await ctx.reply(str(sum))
        
    @commands.command()
    async def subtract(self, ctx, *args: int):
        
        diff = args[0]

        for num in args[1:]:
            diff -= num

        await ctx.reply(str(diff))
    
    @commands.command()
    async def multiply(self, ctx, *args: int):
        
        prod = args[0]
        
        for num in args[1:]:
            prod *= num

        await ctx.reply(str(prod))
    
    @commands.command()
    async def divide(self, ctx, *args: int):
        
        quot = args[0]

        for num in args[1:]:
            quot /= num

        await ctx.reply(str(round(quot, 2)))
        
    @commands.command()
    async def round(self, ctx, num: float, place: int=1):
        await ctx.reply(str(round(num, place)))
    
    
    @commands.command()
    async def calculate(self, ctx):
        pass
    
async def setup(bot):
    await bot.add_cog(Calculator(bot))