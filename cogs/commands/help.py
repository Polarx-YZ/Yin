import discord
from discord.ext import commands
import settings
settings.init()


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        devs = ', '.join(settings.config.get('devs'))
        support_server = settings.config.get("supportServer")

        helpEmbed = discord.Embed(
            title=f"{settings.config.get('botName')} | Help",
            description=f"A bot made by people who have no idea what they are doing. \nJoin the [Support Server!]({support_server})",
        )
        helpEmbed.set_footer(text=f"Made by {devs}")
        await ctx.reply(embed=helpEmbed)
        
    @commands.command()
    async def help(self,ctx, args):
        await ctx.reply("test")


async def setup(bot):
    await bot.add_cog(Help(bot))
