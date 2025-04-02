import discord
from discord.ext import commands
import settings
settings.init()
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = settings.config.get("prefix"), intents=intents, help_command=None)

#Load commmands and events
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

