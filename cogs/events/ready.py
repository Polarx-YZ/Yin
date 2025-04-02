import discord
from discord.ext import commands
import settings
settings.init()

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is ready in {len(self.bot.guilds)} guilds!")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.guilds)} guilds"))

        # If the bot is the test bot then use the test prefix
        if (self.bot.user.id == settings.config.get("testID")):
            self.bot.command_prefix = settings.config.get("testPrefix")


async def setup(bot):
    await bot.add_cog(Ready(bot))
