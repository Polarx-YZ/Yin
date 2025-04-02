import discord
from discord.ext import commands
import settings
settings.init()


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Get help!", description="Get help for commands", usage=f"{settings.config.get("prefix")}help `[Optional: command]`")
    async def help(self, ctx, arg=None):

        if arg != None:
            command = self.bot.get_command(arg)
            if command != None:
                embed = discord.Embed(
                    title=f"Help | {command.name}",
                    description=f"{command.brief}\n\nDescription: {command.description}\n\nUsage: {command.usage}\n\nAliases: {", ".join(command.aliases)}"
                )
                return await ctx.reply(embed=embed)
            return await ctx.reply(f"`{arg}` is not a valid command!")

        # Send default help message if no arguements are provided
        devs = ', '.join(settings.config.get('devs'))
        support_server = settings.config.get("supportServer")

        helpEmbed = discord.Embed(
            title=f"{settings.config.get('botName')} | Help",
            description=f"A bot made by people who have no idea what they are doing. \nJoin the [Support Server!]({support_server})",
        )
        helpEmbed.set_footer(text=f"Made by {devs}")
        await ctx.reply(embed=helpEmbed)


async def setup(bot):
    await bot.add_cog(Help(bot))
