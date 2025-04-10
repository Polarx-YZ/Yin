import discord
from discord.ext import commands
import wavelink
import random

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cosmoto_covers = None
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
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f"Node {node.identifier} is ready!")
    
    @commands.Cog.listener()
    async def on_wavelink_track_start(self, payload: wavelink.TrackStartEventPayload):
        if payload.original:
            embed = discord.Embed(
                title=f"Now playing: {payload.original}",
                color= discord.Color.green()
            )
            await payload.original.ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_wavelink_track_end(self, payload: wavelink.TrackEndEventPayload):
        if payload.original:
            embed = discord.Embed(
                title=f"Stopped playing: {payload.original}",
                color= discord.Color.red()
            )
            
            await payload.original.ctx.send(embed=embed)
            vc = payload.original.ctx.voice_client
            await vc.play(vc.queue.get())
    
    # Plays a song
    @commands.command(aliases=["add_song"], brief="Play a song", description="Adds a song to queue. Typing \"Cosmoto\" will play a random Cosmoto cover.", usage="`search`")
    async def play(self, ctx: commands.Context, *, search: str):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")
        
        
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client
        
        if search.lower() == "cosmoto":
            if self.cosmoto_covers is None:
                await ctx.reply("Loading Cosmoto covers...")
                self.cosmoto_covers = await wavelink.Playable.search("https://youtube.com/playlist?list=PLWyGOSOIpA27BGx5DNfIT6xhzHh7hzNIR&si=kq5N9C0BpLUSLFSx", source=wavelink.TrackSource.YouTube)
            tracks = [random.choice(self.cosmoto_covers)]
        
        else:
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
        if vc.paused is True:
            await vc.pause(False)
        # If there is no song playing and the queue is empty then play the song provided

        # If there is a song already playing then add the song to the end of the queue
        
        # If no song is provided then let the user know
        
        # If the queue is NOT empty and is paused/stopped then resume playing the queue

    @commands.command(brief="Stop the song")
    async def stop(self, ctx):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")
        
        vc: wavelink.Player = ctx.voice_client
        
        vc.queue.clear()
        await vc.stop()
        # Stop playing the song and keep all songs in the queue
        

    @commands.command(brief="Show song queue")
    async def queue(self, ctx):
        
        if ctx.voice_client is not None:
            vc = wavelink.Player = ctx.voice_client
        else:
            return await ctx.reply("Nothing is playing!")
        
        queue = vc.queue
        current_track = vc.current
        
        queue_list = ""
        
        for i, track in enumerate(queue):
            queue_list += f"{i + 1}. [{track.title}]({track.uri}) by {track.author}\n"
        
        embed = discord.Embed(
            title=f"Song Queue",
            description=f"### Currently Playing: [{current_track.title}]({current_track.uri}) by {current_track.author}\n{queue_list}"
        )
        
        await ctx.reply(embed=embed)
        
        # Show the next 10 songs in the queue with the song name and artist
        
        # Send this in an embed please

    @commands.command(brief="Join current voice channel")
    async def join(self, ctx):
        if (ctx.author.voice):
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.reply("Joined the voice channel!")
        else:
            await ctx.reply("You are not in a voice channel!")


    @commands.command(brief="Leave the voice channel")
    async def leave(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.disconnect()
            await ctx.reply("Left the voice channel!")
        else:
            await ctx.reply("I'm not in a voice channel!")
        
    @commands.command(brief="Skip current song")
    async def skip(self, ctx):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")
        
        vc: wavelink.Player = ctx.voice_client
        
        if (vc is None or vc.playing is False):
            return await ctx.reply("Nothing is playing!")
        await vc.skip()
        # Skip the song that is currently playing
        
        # If no song is playing then let the invoker know
        
    @commands.command(brief="Clear song queue")
    async def clear(self, ctx):
        await ctx.reply("Command not yet implemented")
        
        # Clear the queue
    @commands.command(brief="Change volume")
    async def volume(self, ctx, percent: int, opt=""):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")
        
        if opt=="force" and ctx.author.id == 332300933327355905:
            force = True
        else:
            force = False
        
        msg_str = "Set volume to `{0}`"
        if percent > 100 and force is False:
            msg_str += " Let's not destroy our ears..."
            percent = 100
        
        vc: wavelink.Player = ctx.voice_client
        
        await vc.set_volume(percent)
        await ctx.reply(msg_str.format(percent))

    @commands.command(brief="Go to a different part of the current song")
    async def seek(self, ctx, option: str=None, seconds: int=None):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")

        try:
            int(option)
            return await ctx.reply(f"No option given! Please choose whether to seek to, seek forward, or seek back!\n Example: {self.bot.command_prefix}seek to 100")
        except:
            pass

        
        if isinstance(option, int) or option is None:
            return await ctx.reply(f"No option given! Please choose whether to seek to, seek forward, or seek back!\n Example: {self.bot.command_prefix}seek to 100")
        if seconds is None:
            return await ctx.reply(f"Please specify how many seconds to seek!")
            
        vc: wavelink.Player = ctx.voice_client
        
        if vc is None or vc.playing is False:
            return await ctx.reply("Nothing is playing!")
        
        length = vc.current.length
        current_pos = vc.position
        milliseconds = seconds * 1000
        message = ""
        
        if option.lower() == "to":
            new_pos = milliseconds
            message = f"Went to {seconds} seconds!"
        elif option.lower() == "forward" or option.lower() == "f":
            new_pos = current_pos + milliseconds
            message = f"Fast forwarded {seconds} seconds!"
        elif option.lower() == "back" or option.lower() == "backward" or option.lower() == "rewind":
            new_pos = current_pos - milliseconds
            message = f"Rewinded {seconds} seconds!"
            
        
        await vc.seek(new_pos)
        await ctx.reply(message)
    
    @commands.command(brief="Pause the current song")
    async def pause(self, ctx):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")
        
        vc: wavelink.Player = ctx.voice_client
        
        if vc is None or vc.playing is False:
            return await ctx.reply("Nothing is playing!")
        if vc.paused is True:
            return await ctx.reply("The music is already paused!")
        
        await vc.pause(True)
        await ctx.reply("Paused the queue!")
    
    @commands.command(brief="Unpause the current song")
    async def unpause(self, ctx):
        if ctx.author.voice is None:
            return await ctx.reply("You are not in a voice channel!")
        
        vc: wavelink.Player = ctx.voice_client
        
        if vc is None or vc.playing is False:
            return await ctx.reply("Nothing is playing!")
        if vc.paused is False:
            return await ctx.reply("The music is already playing!")
        
        await vc.pause(False)
        await ctx.reply("Unpaused the queue!")
    
    @commands.command(brief="Get info about the current song")
    async def songinfo(self, ctx):
        vc: wavelink.Player = ctx.voice_client
    
        if vc is None or vc.playing is False:
            return await ctx.reply("Nothing is playing!")

        track = vc.current
        title = track.title
        author_name = track.author
        author = track.artist
        author_icon = author.artwork
        author_url = author.url
        curr_position = vc.position / 1000
        curr_minutes = round(curr_position / 60)
        curr_seconds = round(curr_position % 60)
        length = track.length / 1000
        len_minutes = round(length / 60)
        len_seconds = round(length % 60)
        artwork = track.artwork
        song_url = track.uri
        
        embed = discord.Embed()
        embed.title = title
        embed.description = f"**{curr_minutes}:{curr_seconds}-{len_minutes}:{len_seconds}**\n{song_url}"
        embed.set_author(name=author_name, icon_url=author_icon, url=author_url)
        embed.set_image(url=artwork)
        
        await ctx.reply(embed=embed)
    
async def setup(bot):
    await bot.add_cog(Music(bot))
