# import common modules
import discord
from discord.ext import commands
from settings import config

class MemberTracking(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_presence_update(self, before, after):

        if config["tracking"]["enabled"] == False:
            return
        
        # Specify the role name to track
        role_name = config["tracking"]["role_name"]

        # Ensure the 'after' object is a Member instance and belongs to a guild
        if not isinstance(after, discord.Member) or not after.guild:
            return

        # Check if the member's status has changed
        if before.status != after.status:

            # Prevent spamming by ignoring bots
            if after.bot:
                return
            
            # Check if the role exists in the guild
            tracked_role = discord.utils.get(after.guild.roles, name=role_name)
            if not tracked_role:
                print(f"Role '{role_name}' does not exist in the server.")
                return

            # Check if the member has the specified role
            role = discord.utils.get(after.roles, name=role_name)
            if not role:
                print(f"{after.name} does not have the tracked role '{role_name}'.")
                return  
            
            # Log the status change
            print(f"{after.name} with role '{role_name}' changed status from {before.status} to {after.status}")

            # Find the target channel
            channel = discord.utils.get(after.guild.text_channels, name="testing")
            if not channel:
                print("Channel not found.")
                return

            embed = discord.Embed(
                title=f"{after.name} (with role '{role_name}') is now {after.status}!"
            )

            # Change color of embed depending on member status
            if after.status == discord.Status.online:
                embed.colour = discord.Color.green()
                
            elif after.status == discord.Status.idle:
                embed.colour = discord.Color.yellow()
                
            elif after.status == discord.Status.dnd:
                embed.colour = discord.Color.red()
            
            try:
                await channel.send(embed=embed)
            except discord.Forbidden:
                print("Bot does not have permission to send messages in the channel.")

async def setup(bot):
    await bot.add_cog(MemberTracking(bot))