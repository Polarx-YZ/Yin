'''
For @SpaceDuck16
'''

import discord
from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(aliases=["sum", "plus", "total"], brief="Add numbers", description="Outputs a sum of two or more numbers", usage="`Num1` `Num2` `etc...`")
    async def add(self, ctx, *args: float):
        
        sum = args[0]
        
        for num in args[1:]:
            sum += num
        
        addends = " + ".join(str(x) for x in args)

        await ctx.reply(addends + " = " + str(sum)) 
        
    @commands.command(aliases=["diff", "difference", "minus", "sub"], brief="Subtract numbers", description="Outputs a difference between two or more numbers", usage="`Num1` `Num2` `etc...`")
    async def subtract(self, ctx, *args: float):
        
        diff = args[0]

        for num in args[1:]:
            diff -= num
            
        equation = " - ".join(str(x) for x in args)

        await ctx.reply(equation + " = " + str(diff))
    
    @commands.command(aliases=["prod", "product", "times", "mult"], brief="Multiply numbers", description="Outputs a product of two or more numbers", usage="`Num1` `Num2` `etc...`")
    async def multiply(self, ctx, *args: float):
        
        prod = args[0]
        
        for num in args[1:]:
            prod *= num

        factors = " x ".join(str(x) for x in args)

        await ctx.reply(factors + " = " + str(prod))
    
    @commands.command(aliases=["quot", "quotient", "div"], brief="Divide numbers", description="Outputs a quotient (rounded to hundredths) of two or more numbers", usage="`Num1` `Num2` `etc...`")
    async def divide(self, ctx, *args: float):

        for num in args[1:]:
            if num == 0:
                await ctx.reply("You can't divide by zero you dumbo!")
                return
        
        quot = args[0]

        for num in args[1:]:
            quot /= num

        dividends = " / ".join(str(x) for x in args)

        await ctx.reply(dividends + " = " + str(round(quot, 2)))
        
    @commands.command()
    async def round(self, ctx, num: float, place: int=1):
        await ctx.reply(str(round(num, place)))
    
    
    @commands.command()
    async def calculate(self, ctx):
        pass
    
async def setup(bot):
    await bot.add_cog(Calculator(bot))