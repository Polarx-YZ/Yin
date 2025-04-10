import discord
from discord.ext import commands
import re
import random


class Generator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_vowels(self, sentence):
        vowels = list("aieou")
        letters = []
        for letter in sentence:
            if letter in vowels:
                letters.append(letter)
        return letters

    @commands.command(brief="Talk like LOR3!", description="Talk like LOR3 from the Gaming Tavern!", usage="`message`")
    async def lore(self, ctx, *args):
        if len(args) <= 0:
            return await ctx.reply("Please supply a message to generate!")
        
        message = re.sub(r"(?is)e", "3", " ".join(args)) 
        message = re.sub(r"(?is)s", "2", message)
        message = re.sub(r"(?is)b", "6", message)
        message = re.sub(r"(?is)t", "7", message)
        message = re.sub(r"(?is)k", "l<", message)
        message = re.sub(r"(?is)a", "4", message)
        message = re.sub(r"(?is)w", "vv", message)
        message = re.sub(r"(?is)o", "0", message)
        message = re.sub(r"(?is)i", "1", message)
        message = re.sub(r"(?is)!\?", "⁉️", message)
        message = re.sub(r"(?is)!", "‼️", message)
        message = re.sub(r"(?is)\?", "❓️", message)
        message = re.sub(r"(?is)c", "€", message)

        await ctx.reply(message)

    @commands.command(aliases=["meow", "nyan"], brief="Talk like a cat!", description="Meow meow meow! Talk like a cat!", usage="`message`")
    async def cat(self, ctx, *args):
        if len(args) <= 0:
            return await ctx.reply("Please supply a message to generate nya!")
        
        meows = {
            "a": "maow",
            "e": "meow",
            "i": "miuw",
            "o": "mroow",
            "u": "mew"
        }

        message = ""
        vowels = await self.get_vowels("".join(args))
            
        for vowel in vowels:
            message += " " + meows.get(vowel, "meow")

        await ctx.reply(message)

    @commands.command(aliases=["woof", "wan", "bark"], brief="Talk like a dog!", description="Woof woof woof!! Talk like a dog!", usage="`message`")
    async def dog(self, ctx, *args):
        if len(args) <= 0:
            return await ctx.reply("Please supply a message to generate woof!")
        
        barks = {
            "a": "wan",
            "e": "grer",
            "i": "*whine*",
            "o": "woof",
            "u": "wuuu"
        }

        message = ""
        vowels = await self.get_vowels("".join(args))

        for vowel in vowels:
            message += " " + barks.get(vowel, "woof")

        await ctx.reply(message)

    async def owoify(self, message):
        message = re.sub(r"(?is)no", "nyo", message)
        message = re.sub(r"(?is)lit", "wit", message)
        message = re.sub(r"(?is)!", "!!!", message)
        message = re.sub(r"(?is)r", "w", message)

        faces = ["uwu", "owo", ">w<", ">///<", "ovo", "uvu", ";w;", "TwT", ":3", ":P", ":c", "OWO", "UWU", ">W<"]
        
        message += " " + random.choice(faces)

        return message
        
    @commands.command(alises=["uwu", "owo"], brief="Uwuify a message!", usage="`message`")
    async def owo(self, ctx, args=[]):
        if ctx.message.reference is not None:
            message_id = ctx.message.reference.message_id
            msg = await ctx.fetch_message(message_id)
            author = msg.author
            sentence = msg.content
     
        elif len(args) > 0:
            sentence = " ".join(args)
            author = ctx.author
        
        else:
            messages = [message async for message in ctx.channel.history(limit=5)]
            
            # Get the latest message that is not a bot
            for msg in messages[1:]:
                if not msg.author.bot:
                    last_message = await ctx.fetch_message(msg.id)
                    break
            
            sentence = last_message.content
            author = last_message.author
            
        embed = discord.Embed()
        embed.set_author(name=author)
        embed.description = await self.owoify(sentence)
        await ctx.reply(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Generator(bot))
