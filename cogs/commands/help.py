import discord
from discord.ext import commands
import settings
settings.init()

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(title=f"{settings.config.get("botName")} | Help")
        await ctx.reply(embed=helpEmbed)
        
async def setup(bot):
    await bot.add_cog(help(bot))