import discord
from discord.ext import commands
import random
class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        config = await self.bot.config.find(ctx.guild.id)
        
        # if await self.bot.config.find({"autoresponse_dad": {"$exists": False}}):
        #     print("No autoresponse_dad")
        #     await self.bot.config.insert({"autoreponse_dad": True})
        
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
        if ctx.content.isupper() and len(ctx.content) > 1:

            shouts_options = [
                "Hey {0}, no yelling!",
                "HEY {0}, THIS IS A LIBRARY!",
                "Shut up {0}.",
                "Jesus christ {0} you scared me!",
                F"> {self.alternate_case(ctx.content)}\n# SHUT UP",
                "Hey {0}, do you know how stupid you sound right now?",
                "{0}, you're so annoying.",
                "{0}, pipe down!",
                "{0}, YOU'RE GROUNDED FOR YELLING!"
            ]
            return await ctx.reply(random.choice(shouts_options).format(user.mention))
        
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
        
    def alternate_case(self, message):

        words = message.split(" ")
        new_message = ""
        
        for word in words:
            chars = list(word)
            new_word = ""
            for i, char in enumerate(chars):
                if i % 2 == 0:
                    new_word += char.upper()
                else:
                    new_word += char.lower()
            new_message += new_word + " "

        return new_message
    
async def setup(bot):
    await bot.add_cog(Message(bot))
