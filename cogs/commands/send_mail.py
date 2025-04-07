import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

import discord
from discord.ext import commands
from settings import config

load_dotenv(override=True)


class SendMail(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sendmail(self, ctx, *, message: str):

        await ctx.reply("`Sending email...`")
        self.send_email(message)
        await ctx.reply("`Email sent!`")

    def send_email(self, msg):

        # sender_email = "pythonsmtpdeveloper@gmail.com"
        # receiver_email = [
        #     "polarkun761@gmail.com",
        #     "notpolarpup@gmail.com"
        # ]
        
        sender_email = config.get("sender_email")
        receiver_emails = config.get("receiver_emails")
        
        password = os.getenv("GMAIL_PASSWORD")

        message = MIMEMultipart("alternative")
        message["Subject"] = "Test Yin Bot Email Send"
        message["From"] = sender_email
        message["To"] = ", ".join(receiver_emails)

        # Create the plain-text
        part1 = MIMEText(msg, "plain")

        # Add plain text part to MIMEMultipart message
        message.attach(part1)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_emails, message.as_string())
            
            
async def setup(bot):
    await bot.add_cog(SendMail(bot))
