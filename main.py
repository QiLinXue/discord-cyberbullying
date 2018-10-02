#-----------------------------------------------------------------------------
# Name:        Discord Cyberbullying Bot
# Purpose:     To provide a streamlined process removing cyberbullying from
#              discord using a variety of techniques
#
# Author:      QiLin
# Created:     31-Sep-2018
# Updated:     01-Oct-2018
#-----------------------------------------------------------------------------

# File Setup
import settings
from bot_setup import * # pylint: disable=W0614

TOKEN = os.getenv('TOKEN')

# Imports
from client.imports import * # client imports

# -------------------------------
# ------- Intialization ---------
# -------------------------------

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
    
    # Filter Prototype
    if simpleFilter.run(inputText):
        await client.send_message(message.channel, "**Hey!** You can't send that message here!")
    
    if inputText.startswith("!clear"):
        await clear.run(message)




# Run the Bot
client.run(TOKEN)