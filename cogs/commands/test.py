import discord
from discord.ext import commands
import settings

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
    
    @commands.command(hidden=True)
    async def sim_join(self, ctx):
        if self.authorized_user(ctx.author.id):
            await self.bot.dispatch("member_join", ctx.message.author)
            await ctx.reply("Join dispatched")
        
    @commands.command(hidden=True)
    async def sim_leave(self, ctx):
        if self.authorized_user(ctx.author.id):
            await self.bot.dispatch("member_remove", ctx.message.author)
            await ctx.reply("Leave dispatched")
        
    @commands.command(hidden=True)
    async def sim_error(self, ctx):
        if self.authorized_user(ctx.author.id):
            await ctx.reply()
            
    @commands.command(hidden=True)
    async def sim_guild_join(self, ctx):
        if self.authorized_user(ctx.author.id):
            self.bot.dispatch("guild_join", ctx)
            await ctx.reply("Guild join dispatched")
            
    @commands.command(hidden=True)
    async def echo(self, ctx, *args):
        if self.authorized_user(ctx.author.id):
            await ctx.reply(" ".join(args))
    
async def setup(bot):
    await bot.add_cog(Test(bot))