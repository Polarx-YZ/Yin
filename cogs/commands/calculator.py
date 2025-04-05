'''
For @MudaiP
'''

import discord
from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def add(self, ctx):
        pass
    
    @commands.command()
    async def subtract(self, ctx):
        pass
    
    @commands.command()
    async def multiply(self, ctx):
        pass
    
    @commands.command()
    async def divide(self, ctx):
        pass
        
    @commands.command()
    async def calculate(self, ctx):
        pass
    
async def setup(bot):
    await bot.add_cog(Calculator(bot))