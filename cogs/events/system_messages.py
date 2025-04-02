import discord
from discord.ext import commands
import settings
settings.init()


class SystemMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        if settings.config.get("guild").get("welcomeMessage") == False:
            return

        welcomeID = settings.config.get("guild").get("welcomeChannel")

        channel = self.bot.get_channel(welcomeID)

        embed = discord.Embed(
            description=f"## Welcome {member.mention}!\n Enjoy your stay!",
        )

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):

        if settings.config.get("guild").get("departureMessage") == False:
            return

        departureID = settings.config.get("guild").get("departureChannel")

        channel = self.bot.get_channel(departureID)

        embed = discord.Embed(
            description=f"### {member.mention} has left the server!"
        )

        await channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(SystemMessages(bot))
