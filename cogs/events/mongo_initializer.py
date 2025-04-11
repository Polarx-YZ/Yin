import discord
from discord.ext import commands
import pymongo
import motor.motor_asyncio
from utils.mongo import Document
from dotenv import load_dotenv
load_dotenv()
import os
from settings import config

class Initializer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def initialize(self, guild):
        await self.bot.config.insert({
                    "_id": guild.id, 
                    "prefix": ".",
                })
        
    # Make sure all guilds have all the configs
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.connection_url = os.getenv("MONGO_ENTRY")
        print("Connecting to Mongo")
        self.bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(self.bot.connection_url))
        self.bot.db = self.bot.mongo['Yin-DB']
        self.bot.config = Document(self.bot.db, 'config')
        collection_name = 'config'
        
        
        if self.bot.user.id == config.get("testID"):
            self.bot.config = Document(self.bot.db, 'test_config')
            collection_name = 'test_config'
            
        print("Mongo connected")
          
        collection = self.bot.db[collection_name]
        
        # Sets up 
        for guild in self.bot.guilds:
            await self.initialize(guild)
            
        await collection.update_many({"autoresponse_dad": {"$exists": False}},{"$set": {"autoresponse_dad": True}})
        await collection.update_many({"autoresponse_narration": {"$exists": False}},{"$set": {"autoresponse_narration": True}})
        print("Set missing fields")

            
    
    # Set default values for config
    @commands.Cog.listener()
    async def on_guild_join(self, ctx):
        if await self.bot.config.find(ctx.guild.id):
            return print("Guild already has config")
        print(f"Initializing config for '{ctx.guild.name} | {ctx.guild.id}'")
        await self.initialize(ctx.guild)
        print(f"Finished initializing config for '{ctx.guild.name} | {ctx.guild.id}'")
        
async def setup(bot):
    await bot.add_cog(Initializer(bot))