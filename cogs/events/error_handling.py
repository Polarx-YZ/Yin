import discord
from discord.ext import commands
from settings import config


class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error) -> None:
        print(error)
        ping = False

        embed = discord.Embed(
            title="There seems to have been an error!",
            description=f"Please report this bug to the [Support Server](https://discord.gg/xHB5XUMhbu) with a screenshot of the information below!\n---\n\nError: `{error}`\n\nTrigger: `{ctx.message.content}`"
        )

        if ctx.guild.id == config.get("support_server_ID"):
            if ping:
                await ctx.reply(content="<@&1356024937365770370>", embed=embed)
            else:
                await ctx.reply(embed=embed)
        else:
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(ErrorHandling(bot))
