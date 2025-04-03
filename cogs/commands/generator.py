import discord
from discord.ext import commands
import re


class Generator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Talk like LOR3!", description="Talk like LOR3 from the Gaming Tavern!")
    async def lore(self, ctx, *args):
        message = re.sub(r"(?is)e", "3", " ".join(args)
                         )  # Replace the E's with 3's
        message = re.sub(r"(?is)s", "2", message)  # Replace the S's with 2's
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

    @commands.command(aliases=["meow", "nyan"], brief="Meow meow meow!", description="Talk like a cat!")
    async def cat(self, ctx, *args):
        meows = {
            "a": "maow",
            "e": "meow",
            "i": "miuw",
            "o": "mroow",
            "u": "mew"
        }

        def get_vowels(sentence):
            vowels = list("aieou")
            letters = []
            for letter in sentence:
                if letter in vowels:
                    letters.append(letter)
            return letters

        message = ""
        vowels = get_vowels("".join(args))

        for vowel in vowels:
            message += " " + meows.get(vowel, "meow")

        await ctx.reply(message)

    @commands.command(aliases=["woof", "wan", "bark"], brief="Woof woof woof!!", description="Talk like a dog!")
    async def dog(self, ctx, *args):
        meows = {
            "a": "wan",
            "e": "grer",
            "i": "*whine*",
            "o": "woof",
            "u": "wuuu"
        }

        def get_vowels(sentence):
            vowels = list("aieou")
            letters = []
            for letter in sentence:
                if letter in vowels:
                    letters.append(letter)
            return letters

        message = ""
        vowels = get_vowels("".join(args))

        for vowel in vowels:
            message += " " + meows.get(vowel, "woof")

        await ctx.reply(message)


async def setup(bot):
    await bot.add_cog(Generator(bot))
