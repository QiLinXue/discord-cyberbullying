#-----------------------------------------------------------------------------
# Name:        Discord Cyberbullying Bot
# Purpose:     To provide a streamlined process removing cyberbullying from
#              discord using a variety of techniques
#
# Author:      QiLin
# Created:     31-Sep-2018
# Updated:     01-Oct-2018
#-----------------------------------------------------------------------------

# Discord Imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

# File Setup
import settings
TOKEN = os.getenv('TOKEN')

# -------------------------------
# ------- Intialization ---------
# -------------------------------

client = Bot('') # Initialize
chat_filter = ["FUCK","BITCH","ASS","FUCKING","CUNT","DESPACITO","IDIOT","PATHETIC"] # Vocabulary
print("Starting up...") # Notify file was run

# Notify if Bot was setup correctly
@client.event
async def on_ready():
    print("Bot is online")

# -------------------------------
# -------- Functions ------------
# -------------------------------

@client.event
async def on_message(message):

    # -------------------------------
    # ---------- Setup --------------
    # -------------------------------

    inputText = message.content # The Message Sent (str)

    # -------------------------------
    # -------- Fun Things -----------
    # -------------------------------

    if inputText == ("Am I smart?"):
        if message.author.name == "Qcumber":
            await client.send_message(message.channel, "Yes!")
        else:
            smartPerson = '<@285571058353045505>'
            await client.send_message(message.channel, "No, but %s is!" % smartPerson)

    elif inputText.startswith("!ping"):
        await client.send_message(message.channel, ":ping_pong: pong!")

    elif message.content.startswith("!say"):
        args = inputText.split(" ")
        if len(args) > 1: await client.send_message(client.get_channel('496435880852979721'), "%s" % (" ".join(args[1:])))
    
    # -------------------------------
    # --------- Utilities -----------
    # -------------------------------

    if inputText.startswith("!clear"):
        number = inputText.split(" ")[1]
        mgs = [] #Empty list to put all the messages in the log

        try:
            number = int(number) #Converting the amount of messages to delete to an integer
        except ValueError:
            await client.send_message(message.channel, "Invalid Syntax. Please phrase it as `!clear number`")
            return

        try:
            async for x in client.logs_from(message.channel, limit = number):
                mgs.append(x)
            await client.delete_messages(mgs)

        except discord.errors.ClientException:
            return

    # -------------------------------
    # ------ Useful Functions -------
    # -------------------------------

    # Filter Prototype
    for word in inputText.split(" "):
        if word.upper() in chat_filter:
            await client.send_message(message.channel, "**Hey!** You can't send that message here!")
            break

# Run the Bot
client.run(TOKEN)
