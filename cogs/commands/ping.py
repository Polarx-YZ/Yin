import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready!")
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
        
        
async def setup(bot):
    await bot.add_cog(ping(bot))