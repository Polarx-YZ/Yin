import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def authorized_user(self, id):
        whitelist = [
            332300933327355905, # Rin
            478266960505995274, # Mudai
            821371512187387914, # Alam
            1088149438540812448, # Asahi
            706410897429495819, # Yoshi
            820354251640799343, # Yaru
            ]
        if id in whitelist:
            return True
        return False
    
    @commands.command()
    async def sim_join(self, ctx):
        if self.authorized_user(ctx.author.id):
            await ctx.reply("Join dispatched")
            await self.bot.dispatch("member_join", ctx.message.author)
        
    @commands.command()
    async def sim_leave(self, ctx):
        if self.authorized_user(ctx.author.id):
            await ctx.reply("Leave dispatched")
            await self.bot.dispatch("member_remove", ctx.message.author)
        
    @commands.command()
    async def sim_error(self, ctx):
        if self.authorized_user(ctx.author.id):
            await ctx.reply()
    
    @commands.command()
    async def echo(self, ctx, *args):
        if self.authorized_user(ctx.author.id):
            await ctx.reply(" ".join(args))
        
async def setup(bot):
    await bot.add_cog(Test(bot))