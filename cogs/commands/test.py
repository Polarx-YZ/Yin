import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def sim_join(self, ctx):
        await ctx.reply("Join dispatched")
        await self.bot.dispatch("member_join", ctx.message.author)
        
    @commands.command()
    async def sim_leave(self, ctx):
        await ctx.reply("Leave dispatched")
        await self.bot.dispatch("member_remove", ctx.message.author)
        
async def setup(bot):
    await bot.add_cog(Test(bot))