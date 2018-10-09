#-----------------------------------------------------------------------------
# Name:        Discord Cyberbullying Bot
# Purpose:     To provide a streamlined process removing cyberbullying from
#              discord using a variety of techniques
#
# Author:      QiLin
# Created:     31-Sep-2018
# Updated:     01-Oct-2018
#-----------------------------------------------------------------------------

# pylint: disable=W0614

# File Setup
from botSetup import *

TOKEN = os.getenv('TOKEN')

# Imports
from client.imports import * # client imports
from server.imports import * # server imports

# -------------------------------
# ------- Intialization ---------
# -------------------------------

print("Starting up...") # Notify file was run
baddies = badWords.fetch()

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

    global baddies
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

    if inputText.startswith("!trump") and inputText.count(' ') > 0:
        mes = inputText.split(' ', 1)[1]
        await client.send_message(message.channel, trumpCount.run(mes))

    # -------------------------------
    # -------- Work Things ----------
    # -------------------------------

    # Clears Messages
    if inputText.startswith("!clear"):
        await clear.run(message,client)
    
    # Add Bad Words
    if inputText.startswith("!add") and inputText.count(' ') > 0:
        mes = inputText.split(' ', 1)[1]
        if mes in baddies:
            await client.send_message(message.channel, "Word already added")
        else: 
            badWords.run(mes,baddies) # Run and get status
            await client.send_message(message.channel, "Successfully added %s to database" % mes)
            baddies.append(mes)

    # Remove Bad Words
    if inputText.startswith("!delete") and inputText.count(' ') > 0:
        mes = inputText.split(' ', 1)[1]

        if mes in baddies:
            badWords.delete(mes)
            await client.send_message(message.channel, "Successfully deleted %s from database" % mes)
            baddies = badWords.fetch()
        else:
            await client.send_message(message.channel, "You silly. %s is not even a banned word!" % mes)

    # Print Bad Words
    if inputText.startswith("!print"):
        await client.send_message(message.channel,badWords.printAll())
    
    # Filters Messages
    if not message.author.name == "Mr Seidel":
        vulgar_confidence = sqlFilter.run(inputText,baddies)
        if vulgar_confidence == 1:
            await client.send_message(message.channel, "**Hey!** You can't send that message here! Confidence: 100%")
        elif vulgar_confidence == 0.5:
            await client.send_message(message.channel, "**Hey!** You can't send that message here! Confidence: 50%")

# Run the Bot
client.run(TOKEN)