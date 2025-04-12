import discord
from discord.ext import commands
import settings
import utils.checks as checks


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    is_authorized = commands.check(checks.authorized_user)
    
    @is_authorized
    @commands.command(hidden=True)
    async def sim_join(self, ctx):
        self.bot.dispatch("member_join", ctx.author)
        await ctx.reply("Join dispatched")
    
    @is_authorized
    @commands.command(hidden=True)
    async def sim_leave(self, ctx):
        self.bot.dispatch("member_remove", ctx.author)
        await ctx.reply("Leave dispatched")
    
    @is_authorized
    @commands.command(hidden=True)
    async def sim_error(self, ctx):
        await ctx.reply()
            
    @is_authorized
    @commands.command(hidden=True)
    async def sim_guild_join(self, ctx):
        self.bot.dispatch("guild_join", ctx)
        await ctx.reply("Guild join dispatched")
    
    @is_authorized
    @commands.command(hidden=True)
    async def echo(self, ctx, *args):
        await ctx.reply(" ".join(args))
    
async def setup(bot):
    await bot.add_cog(Test(bot))