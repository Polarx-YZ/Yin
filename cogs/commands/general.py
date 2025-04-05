import discord
from discord.ext import commands
from settings import config
import datetime
from time import time

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time()

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     self.start_time = time()
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"Pong! `{round(self.bot.latency * 1000) }ms`")

    @commands.command(aliase=["commands"])
    async def commandlist(self, ctx):
        sorted_commands = sorted(list(self.bot.commands), key=lambda x: x.name)

        text = "```"
        for command in sorted_commands:
            text += f"{command.name}\n"
        text += "```"
        text += f"\n`Total: {len(self.bot.commands)}`"
        await ctx.reply(text)

    @commands.command()
    async def botinfo(self, ctx):
        total_commands = len(self.bot.commands)
        total_servers = len(self.bot.guilds)
        total_members = 0
        uptime = str(datetime.timedelta(seconds=int(round(time()-self.start_time))))
        devs = ", ".join(config.get("devs"))
        
        # TODO In the future I would like this to not include duplicate members
        for guild in self.bot.guilds:
            user_count = len([x for x in guild.members if not x.bot]) # Excludes bots from the member count
            total_members += user_count

        embed = discord.Embed(
            title=f"- Bot Info -",
            description=f"Info for {config.get("botName")}"
        )
        embed.add_field(name="Total Commands", value=total_commands)
        embed.add_field(name="Total Servers", value=total_servers)
        embed.add_field(name="Total Members", value=total_members)
        embed.add_field(name="Uptime", value=uptime)
        embed.set_footer(text=f"Made by {devs}")
        
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
