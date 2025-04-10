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

    @commands.command(aliases=["commands"])
    async def commandlist(self, ctx):
        sorted_commands = sorted(list(self.bot.commands), key=lambda x: x.name)

        text = "```"
        for command in [x for x in sorted_commands if not x.hidden]:
            if command.brief:
                brief = f"- {command.brief}"
            else:
                brief = ""
                
            text += f"| {command.name} {brief}\n"
        text += "```"
        text += f"\n`Total: {len([x for x in self.bot.commands if not x.hidden])}`"
        await ctx.reply(text)

    @commands.command()
    async def botinfo(self, ctx):
        total_commands = len([x for x in self.bot.commands if not x.hidden])
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
            description=f"Info for {config.get("bot_name")}"
        )
        embed.add_field(name="Total Commands", value=total_commands)
        embed.add_field(name="Total Servers", value=total_servers)
        embed.add_field(name="Total Members", value=total_members)
        embed.add_field(name="Uptime", value=uptime)
        embed.set_footer(text=f"Made by {devs}")
        
        await ctx.reply(embed=embed)

    @commands.command(aliases=["about", "whois", "profile"])
    async def memberinfo(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        
        display_name = member.display_name
        nickname = member.nick
        creation_date = member.created_at.strftime("%a %#d %B %Y, %I:%M %p")
        age = round((time() - member.created_at.timestamp()) / 31536000, 2) # in years
        joined_date = member.joined_at.strftime("%a %#d %B %Y, %I:%M %p")
        
        embed = discord.Embed(
            title=f"About {member}",
            description=f"__**Aliases**__\n**Username**: {member}\n**Display Name**: {display_name}\n**Nickname**: {nickname}\n\n__**Info**__\n**Account Age**: {age} years\n**Creation Date**: {creation_date}\n**Joined at**: {joined_date}"
        )
        
        embed.set_image(url=member.avatar.url)
        
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
