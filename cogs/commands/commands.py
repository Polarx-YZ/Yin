import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def commands(self, ctx):
        sorted_commands = sorted(list(self.bot.commands), key=lambda x: x.name)

        text = "```"
        for command in sorted_commands:
            text+=f"{command.name}\n"
        text += "```"
        text += f"\n`Total: {len(self.bot.commands)}`"
        await ctx.reply(text)
        
async def setup(bot):
    await bot.add_cog(Commands(bot))