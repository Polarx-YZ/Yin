import discord
import random
from discord.ext import commands
import settings

class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="Get a random quote")
    async def quote(self, ctx):
        quotes = settings.quotes
        
        choice = random.choice(quotes)
        quote = choice["quote"]
        author = choice["author"]
        
        embed = discord.Embed(
            title=quote,
            description=f"-{author}"
        )
        
        await ctx.reply(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Quote(bot))