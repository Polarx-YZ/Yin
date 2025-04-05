import discord
from discord.ext import commands
from settings import config

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # Display the amount of guilds the bot is in
        print(f"Bot is ready in {len(self.bot.guilds)} guilds!")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.guilds)} guilds"))

        # If the bot is the test bot
        if self.bot.user.id == config.get("testID"):
            self.bot.command_prefix = config.get("test_prefix")
            
            # Show bot status
            # TODO Later Yin Manager should be the one doing this
            try:
                await self.bot.wait_until_ready()
                channel = self.bot.get_channel(1356027989338619954)
                await channel.send("`Bot is ready!`")
            except Exception as e:
                print(e)
            


async def setup(bot):
    await bot.add_cog(Ready(bot))
