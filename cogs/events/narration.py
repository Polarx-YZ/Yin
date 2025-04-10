import discord
from discord.ext import commands
import random

class Narration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        config = await self.bot.config.find(ctx.guild.id)
        
        if ctx.author.bot or config["autoresponse_narration"] == False:
            return

        user = ctx.author
        dead_triggers = ["kms", "i'm dead", "killing myself", "i died"]

        
        if (any(x for x in dead_triggers if x in ctx.content.lower())):
            options = [
                "{0} dies",
                "{0} fucking dies",
                "{0} disappeared",
                "{0} disappeared into a cloud of smoke",
                "{0} left and was never seen again",
                "{0} left to buy milk",
                "{0} killed {0} and then died",
                "{0} MORE MORE JUMPed off a cliff",
                "{0} exploded",
                "{0} is dead",
                "{0} forced {1} to kill them",
                "{0} was slain by {1}",
                "{0} starred in Romeo and Juliet",
                "{0}'s name is David",
                "MY NAME IS {0}. DAD, I WANT SOME ICE CREAM. {0} THAT IS MY NAME. {0} I WANT ANOTHER. {0} WHERE IS MY BALL? I'M RUNNING OUT ON THE ROAD. THERE IS A CAR. AND IT IS GOING TO HIT ME. AAAAAAAAAAH",
                "{0} couldn't do anything but sing a stupid song",
                "{0} got impaled by a rebar",
                "A passing trucking suddenly ran over {0} and drove away, while {1} screamed",
                "A falling metal pole pierced through {0}",
                "{0}: \"Here I goooo!!!\" <a:sakura_minamoto:1358212322295808070>",
                "{0} flew away",
                "The Disappearance of {0}",
                "{1} used the Elements of Harmony on {0}",
                "{0} was banished to the moon for a thousand years",
                "{0} got springlocked"
            ]
            await ctx.channel.send(random.choice(options).format(user.mention, random.choice(ctx.guild.members).mention))
                
            if (any(x for x in dead_triggers if x in ctx.content.lower())):
                pass

async def setup(bot):
    await bot.add_cog(Narration(bot))
