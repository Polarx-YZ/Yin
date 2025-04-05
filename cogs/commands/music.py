import discord
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Plays a song
    @commands.command()
    async def play(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # If there is no song playing and the queue is empty then play the song provided
        self.bot.lavalink_nodes = [
            {"host": "lavalink.devz.cloud", "port": 443, "password": "mathiscool", "https": True},
        ]



        # If there is a song already playing then add the song to the end of the queue
        
        # If no song is provided then let the user know
        
        # If the queue is NOT empty and is paused/stopped then resume playing the queue

    @commands.command()
    async def stop(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # Stop playing the song and keep all songs in the queue
        

    @commands.command()
    async def queue(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # Show the next 10 songs in the queue with the song name and artist
        
        # Send this in an embed please

    @commands.command()
    async def join(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # Make the bot join the voice channel the invoker is in.
        
        # If the invoker is not in a voice channel then let the invoker know

    @commands.command()
    async def leave(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # Leave the voice channel but do NOT clear the queue

    @commands.command()
    async def add_song(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # add a song to the queue
        
    @commands.command()
    async def skip(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # Skip the song that is currently playing
        
        # If no song is playing then let the invoker know
        
    @commands.command()
    async def clear(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # Clear the queue


async def setup(bot):
    await bot.add_cog(Music(bot))
