import discord
from discord.ext import commands

class UpdateStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.guilds)} guilds"))
            
    @commands.Cog.listener()
    async def on_guild_leave(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.guilds)} guilds"))

async def setup(bot):
    await bot.add_cog(UpdateStatus(bot))
