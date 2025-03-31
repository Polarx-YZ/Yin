import discord
from discord.ext import commands
import json
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

with open("config.json", "r") as file:
    config = json.load(file)
    print(config)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = config.get("prefix"), intents=intents)

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

