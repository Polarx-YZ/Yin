import discord
import random
from discord.ext import commands
import settings

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class Suggestion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def suggest(self, ctx, *args):
        author = ctx.author
        guild_name = ctx.guild.name
        suggestion_channel_id = 1360389313908707529
        suggestion_channel = self.bot.get_channel(suggestion_channel_id)
        
        embed = discord.Embed(
            title=f"Suggestion",
            description=" ".join(args)
        )
        
        embed.set_author(name=f"{author} from {guild_name}", icon_url=ctx.author.avatar.url)
        
        suggestion_message = await suggestion_channel.send(embed=embed)

        await suggestion_message.add_reaction("👍")
        await suggestion_message.add_reaction("👎")
        thread = await suggestion_message.create_thread(name="Comments")
        
        support_server = self.bot.get_guild(settings.config["support_server_ID"])
        
        '''
            If the user is in the support server it will ping them
            This is useful for moderation purposes as well. If bad
            suggestions are made then it will be easy to find and
            ban them
        '''
        if support_server.get_member(ctx.author.id) is not None:
            await thread.send(f"Hey {ctx.author.mention}! Thanks for making this suggestion! If you'd like to add onto your idea you may add them in this thread!")

        reply_embed = discord.Embed(
            description = f"Suggestion sent successfully! [Click here to see your suggestion!]({suggestion_message.jump_url})"
        )
        
        reply_embed.color = discord.Color.green()
        
        await ctx.reply(embed=reply_embed)

        #self.send_email(ctx, " ".join(args))
            
        
    def send_email(self, ctx, msg):
        
        guild_name = ctx.guild.name
        
        # Load the email configuration from the config.json file
        email_config = settings.config.get("email")
        sender_email = email_config.get("sender_email")
        reciever_email = email_config.get("reciever_email")
        
        # Get the Gmail password from the environment variables
        # This password is used to authenticate with the Gmail SMTP server
        password = os.getenv("GMAIL_PASSWORD")

        # Create a MIMEMultipart message object
        # This object is used to define the email content and headers
        message = MIMEMultipart("alternative")
        message["Subject"] = f"Suggestion from {guild_name}"
        message["From"] = sender_email
        #message["To"] = ", ".join(reciever_email)
        message["To"] = reciever_email[1]

        # Create the plain-text
        part1 = MIMEText(f"From {ctx.author} \n\n Suggestion: {msg}", "plain")

        # Add plain text part to MIMEMultipart message
        message.attach(part1)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message.as_string())
    
async def setup(bot):
    await bot.add_cog(Suggestion(bot))