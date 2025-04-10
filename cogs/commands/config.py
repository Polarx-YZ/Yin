import discord
import random
from discord.ext import commands

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def convert_bool(self, value):
        if value == "true":
            return True
        else:
            return False
    
    async def change_prefix(self, ctx, prefix):
        await self.bot.config.upsert({"_id": ctx.guild.id, "prefix": prefix})
        await ctx.reply(f"The server prefix has been set to `{prefix}`")
    
    async def change_autoresponses(self, ctx, setting, value):
        value = await self.convert_bool(value)
        
        if setting == "dad":
            await self.bot.config.upsert({"_id": ctx.guild.id, "autoresponse_dad": value})
            return await ctx.reply(f"Dad bot response set to `{value}`")
            
        if setting == "narration":
            await self.bot.config.upsert({"_id": ctx.guild.id, "autoresponse_narration": value})
            return await ctx.reply(f"Narration set to `{value}`")
        
    @commands.has_permissions(manage_guild=True)
    @commands.command(aliases=["settings"])
    async def config(self, ctx, setting=None, *args):
        
        print(f"Setting: {setting}, values: {args}")
        
        if setting == "prefix":
            return await self.change_prefix(ctx, args[0])
        if setting == "autoresponse":
            return await self.change_autoresponses(ctx, args[0], args[1])

        server_config = await self.bot.config.find(ctx.guild.id)
        
        setting_string = ""
        for config in server_config:
            setting_string += f"**{config}**: {server_config[config]}\n"
        
        embed = discord.Embed(
            title="Server Configuration",
            description=setting_string
        )
        
        await ctx.reply(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Config(bot))