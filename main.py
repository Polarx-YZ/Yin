from dotenv import load_dotenv
import asyncio
import os
import discord
from discord.ext import commands
import settings
settings.init()
load_dotenv()

async def get_prefix(self, ctx):
    
    try:
        data = await client.config.find(ctx.guild.id)
        
        if not data or "prefix" not in data:
            return commands.when_mentioned_or(".")(self, ctx)
        return commands.when_mentioned_or(data['prefix'])(self, ctx)
    except:
        return commands.when_mentioned_or(".")(self, ctx)

intents = discord.Intents.all()

client = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=None)

# Load commmands and events
async def load():
    for folder in os.listdir("./cogs"):
        for filename in os.listdir(f"./cogs/{folder}"):
            if filename.endswith(".py"):
                print(f"Loaded {filename}")
                await client.load_extension(f"cogs.{folder}.{filename[: -3]}")


async def main():
    await load()
    await client.start(os.getenv("TOKEN"))


asyncio.run(main())
