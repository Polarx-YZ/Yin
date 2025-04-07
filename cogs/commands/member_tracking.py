# import common modules
import discord
from discord.ext import commands

import time
from datetime import datetime 

# create a class for the cog
# This class is used to track member presence updates in Discord
class MemberTracking(commands.Cog):

    # Initialize the MemberTracking class with the bot instance
    # This method is called when the cog is loaded
    def __init__(self, bot):
        self.bot = bot
        self.cooldowns = {}  # to store cooldown timestamps for each member

    # Define the on_presence_update event listener
    # This event is triggered whenever a member's presence changes
    @commands.Cog.listener()
    async def on_presence_update(self, before, after):

        # Specify the role name to track
        role_name = "Tracking"  # Replace with the name of the role you want to track
        cooldown_period = (1) * (3600)  # Cooldown period in hours

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
                return  # Member does not have the tracked role
            
            # Cooldown check
            current_time = time.time()
            last_update_time = self.cooldowns.get(after.id, 0)  # Get the last update time for the member
            if current_time - last_update_time < cooldown_period:
                remaining_time = cooldown_period - (current_time - last_update_time)
                minutes = int(remaining_time // 60)
                seconds = int(remaining_time % 60)

                print(f"Ignoring status update for {after.name} due to cooldown.")
                print(f"Last update time: {last_update_time}, Current time: {current_time}")
                print(f"Cooldown remaining: {minutes} minutes and {seconds} seconds")
                # If the cooldown period has not passed, ignore the update
                return  # Ignore updates within the cooldown period

            # Update the cooldown timestamp
            date_stamp = datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S') 
            self.cooldowns[after.id] = date_stamp  # Update the cooldown timestamp for the member
            
            print(self.cooldowns)  # Debugging line to check cooldowns

            # Log the status change
            print(f"{after.name} with role '{role_name}' changed status from {before.status} to {after.status}")


            # Find the target channel
            channel = discord.utils.get(after.guild.text_channels, name="testing")  # Replace with your channel name
            if not channel:
                print("Channel not found.")
                return

            try:
                await channel.send(f"{after.name} (with role '{role_name}') is now online!")
            except discord.Forbidden:
                print("Bot does not have permission to send messages in the channel.")

async def setup(bot):
    await bot.add_cog(MemberTracking(bot))