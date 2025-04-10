import discord
from discord.ext import commands

class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        config = await self.bot.config.find(ctx.guild.id)
        
        if ctx.author.bot or config["autoresponse_dad"] == False:
            return

        user = ctx.author
        dad_triggers = ["i'm", "am", "im"]
        
        # Checks if any dad_triggers are in the message and stores the string that triggered it
        if (any(x for x in dad_triggers if x in ctx.content.lower())):
            for trigger in dad_triggers:
                for index, word in enumerate(ctx.content.lower().split(" ")):
                    if word == trigger:
                        words_after = ctx.content.split()[index + 1:]
                        return await ctx.reply(f"Hi {" ".join(words_after)}! I'm Dad!")
                    
        # Respond to 'shouting'
        if ctx.content.isupper():
            return await ctx.reply(f"Hey {user.mention}, no yelling!")
        
        #! OLD CODE DOESN'T WORK AND IT'S WAY TOO COMPLICATED LOL - @Polarx-YZ
        # dad_trigger = next((trigger for trigger in dad_triggers if any(x in trigger for x in ctx.content.split())), None)

        # if dad_trigger is not None:
        #     print(dad_trigger)
        #     after = re.search(r"(?<={dad_trigger})\s*(.*)", ctx.content)
            
        #     print(after)
        
        #     #await ctx.reply(f"Hi {after}! I'm Dad!")
        #     # before, key, after = ctx.content.partition(dad_trigger)
        #     # if key == "":
        #     #     return
        #     # await ctx.reply(f"Hi{after}! I'm Dad")


async def setup(bot):
    await bot.add_cog(Message(bot))
