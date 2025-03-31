import discord
from discord.ext import commands

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def commands(self, ctx):
        helptext = "```"
        for command in self.bot.commands:
            helptext+=f"{command.name}\n"
        helptext += "```"
        await ctx.reply(helptext)
        
async def setup(bot):
    await bot.add_cog(commands(bot))