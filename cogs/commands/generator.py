import discord
from discord.ext import commands
import re

class generator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def lore(self, ctx, *args):
        message = re.sub(r"(?is)e", "3", " ".join(args)) # Replace the E's with 3's
        message = re.sub(r"(?is)s", "2", message) # Replace the S's with 2's
        message = re.sub(r"(?is)b", "6", message)
        message = re.sub(r"(?is)t", "7", message)
        message = re.sub(r"(?is)k", "l<", message)
        message = re.sub(r"(?is)a", "4", message)
        message = re.sub(r"(?is)w", "vv", message)
        message = re.sub(r"(?is)o", "0", message)
        message = re.sub(r"(?is)i", "1", message)
        message = re.sub(r"(?is)!\?", "⁉️", message)
        message = re.sub(r"(?is)!", "‼️", message)
        message = re.sub(r"(?is)\?", "❓️", message)
        message = re.sub(r"(?is)c", "€", message)
          
        await ctx.reply(message)
        
async def setup(bot):
    await bot.add_cog(generator(bot))