import discord
from discord.ext import commands
import settings
settings.init()

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def help(self, ctx):
        
        helpEmbed = discord.Embed(
            title=f"{settings.config.get('botName')} | Help", 
            description=f"A bot made by people who have no idea what they are doing. \nJoin the [Support Server!](https://discord.gg/xHB5XUMhbu)",
            )
        helpEmbed.set_footer(text= f"Made by {', '.join(settings.config.get('devs'))}")
        await ctx.reply(embed=helpEmbed)
        
async def setup(bot):
    await bot.add_cog(help(bot))