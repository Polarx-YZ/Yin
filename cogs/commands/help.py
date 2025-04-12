import discord
from discord.ext import commands
from settings import config


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Get help!", description="Get help for commands", usage=f"`[Optional: command]`")
    async def help(self, ctx, arg=None):
        config = await self.bot.config.find(ctx.guild.id)
        prefix = config["prefix"]
        
        if arg != None:
            command = self.bot.get_command(arg)
            if command != None:
                embed = discord.Embed(
                    title=f"Help | {command.name}",
                    description=f"{command.brief}\n\nDescription: {command.description}\n\nUsage: {prefix}{command.name} {command.usage}\n\nAliases: `{"`, `".join(command.aliases)}`"
                )
                return await ctx.reply(embed=embed)
            return await ctx.reply(f"`{arg}` is not a valid command!")

        # Send default help message if no arguements are provided
        devs = ', '.join(config.get('devs'))
        support_server = config.get("support_server")

        helpEmbed = discord.Embed(
            title=f"{config.get('bot_name')} | Help",
            description=f"A bot made by people who have no idea what they are doing!! \n\nJoin the [Support Server!]({support_server})",
        )
        helpEmbed.set_footer(text=f"Made by {devs}")
        await ctx.reply(embed=helpEmbed)


async def setup(bot):
    await bot.add_cog(Help(bot))
