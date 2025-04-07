#import local modules used for this .py file only
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import json

#import common modules
import discord
from discord.ext import commands
from settings import config


# Load the config.json file
with open("config.json", "r") as config_file:
    config = json.load(config_file)


# Load environment variables from .env file
load_dotenv(override=True)


# Define the SendMail class as a cog
# This class is used to send emails using the Gmail SMTP server
class SendMail(commands.Cog):

    # Initialize the SendMail class with the bot instance
    # This method is called when the cog is loaded
    def __init__(self, bot):
        self.bot = bot

    # Define the sendmail command
    # This command accepts arguments and sends an email with the provided message
    @commands.command()
    async def sendmail(self, ctx, *, message: str):

        await ctx.reply("`Sending email...`")
        self.send_email(message) #This function is called to handle mail process
        await ctx.reply("`Email sent!`")


    # Define the send_email method
    # This method sends an email using the Gmail SMTP server
    def send_email(self, msg):
        
        # Load the email configuration from the config.json file
        email_config = config.get("email")
        sender_email = email_config.get("sender_email")
        reciever_email = email_config.get("reciever_email")

        # Print the sender and receiver email addresses for debugging purposes
        print(f"Sender email: {sender_email}")
        print(f"Receiver emails: {reciever_email}")
        
        # Get the Gmail password from the environment variables
        # This password is used to authenticate with the Gmail SMTP server
        password = os.getenv("GMAIL_PASSWORD")

        # Create a MIMEMultipart message object
        # This object is used to define the email content and headers
        message = MIMEMultipart("alternative")
        message["Subject"] = "Test Yin Bot Email Send"
        message["From"] = sender_email
        message["To"] = ", ".join(reciever_email)

        # Create the plain-text
        part1 = MIMEText(msg, "plain")

        # Add plain text part to MIMEMultipart message
        message.attach(part1)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message.as_string())
            

# Define the setup function
# This function is called when the cog is loaded
async def setup(bot):
    await bot.add_cog(SendMail(bot))
