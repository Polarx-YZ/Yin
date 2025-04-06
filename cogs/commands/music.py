import discord
from discord.ext import commands
import wavelink

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.bot.lavalink_nodes = [
        #     {"host": "lavalink.devz.cloud", "port": 443, "password": "mathiscool", "https": True},
        # ]
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.node_connect())
    
    async def node_connect(self):
        await self.bot.wait_until_ready()
        
        nodes = [
            wavelink.Node(
                identifier="Node1",
                uri="https://lava-v4.ajieblogs.eu.org",
                password="https://dsc.gg/ajidevserver"
            )
        ]
        
        print("Connecting node...")
        await wavelink.Pool.connect(nodes=nodes, client=self.bot)
    
    
    @commands.Cog.listener()
    async def on_wavelink_node_connect(self, node: wavelink.Node):
        print(f"Node {node.identifier} is ready!")
    
    @commands.Cog.listener()
    async def on_wavelink_track_start(self, payload: wavelink.TrackStartEventPayload):
        if payload.original:
            await payload.original.ctx.send(f"Now playing: {payload.original}")
    
    @commands.Cog.listener()
    async def on_wavelink_track_end(self, payload: wavelink.TrackEndEventPayload):
        if payload.original:
            await payload.original.ctx.send(f"Stopped playing: {payload.original}")
            vc = payload.original.ctx.voice_client
            await vc.play(vc.queue.get())
    
    # Plays a song
    @commands.command()
    async def play(self, ctx: commands.Context, *, search: str):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")
        
        
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client
        
        tracks = await wavelink.Playable.search(search, source=wavelink.TrackSource.YouTube)
        
        if not tracks:
            return await ctx.reply("No tracks found!")

        if isinstance(tracks, wavelink.Playlist):
            tracks.track_extras(ctx=ctx)
            added: int = await vc.queue.put_wait(tracks)
            await ctx.reply(f"Added {added} tracks from the playlist {tracks.name} to the queue!")
        else:
            track: wavelink.Playable = tracks[0]
            track.ctx = ctx
            
            await vc.queue.put_wait(track)
            await ctx.reply(f"Added {track} to the queue!")


        if not vc.playing:
            await vc.play(vc.queue.get(), volume=30, replace=False)
        # If there is no song playing and the queue is empty then play the song provided

        # If there is a song already playing then add the song to the end of the queue
        
        # If no song is provided then let the user know
        
        # If the queue is NOT empty and is paused/stopped then resume playing the queue

    @commands.command()
    async def stop(self, ctx):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")
        
        vc: wavelink.Player = ctx.voice_client
        
        vc.queue.clear()
        await vc.stop()
        # Stop playing the song and keep all songs in the queue
        

    @commands.command()
    async def queue(self, ctx):
        
        if ctx.voice_client is not None:
            vc = wavelink.Player = ctx.voice_client
        else:
            return await ctx.reply("Nothing is playing!")
        
        queue = vc.queue
        current_track = vc.current
        
        queue_list = ""
        
        for i, track in enumerate(queue):
            queue_list += f"{i + 1}. {track.title} by {track.author}\n"
        
        embed = discord.Embed(
            title=f"Song Queue",
            description=f"## Currently Playing:\n### __{current_track.title} by {current_track.author}__\n{queue_list}"
        )
        
        await ctx.reply(embed=embed)
        
        # Show the next 10 songs in the queue with the song name and artist
        
        # Send this in an embed please

    @commands.command()
    async def join(self, ctx):
        if (ctx.author.voice):
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.reply("Joined the voice channel!")
        else:
            await ctx.reply("You are not in a voice channel!")


    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.disconnect()
            await ctx.reply("Left the voice channel!")
        else:
            await ctx.reply("I'm not in a voice channel!")

    @commands.command()
    async def add_song(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # add a song to the queue
        
    @commands.command()
    async def skip(self, ctx):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")
        
        vc: wavelink.Player = ctx.voice_client

        await vc.skip()
        # Skip the song that is currently playing
        
        # If no song is playing then let the invoker know
        
    @commands.command()
    async def clear(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # Clear the queue


async def setup(bot):
    await bot.add_cog(Music(bot))
