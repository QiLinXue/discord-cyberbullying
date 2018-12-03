#-----------------------------------------------------------------------------
# Name:        Discord Cyberbullying Bot
# Purpose:     To provide a streamlined process removing cyberbullying from
#              discord using a variety of techniques
#
# Author:      QiLin
# Created:     31-Sep-2018
# Updated:     13-Oct-2018
#-----------------------------------------------------------------------------

# pylint: disable=W0614

# File Setup
from botSetup import *

TOKEN = os.getenv('TOKEN')

from serverSetup import DBUSER,DBPASS

# Imports
from client.imports import * # client imports
from server.imports import * # server imports

import discord

# -------------------------------
# ------- Initialization --------
# -------------------------------

print("Starting up...") # Notify file was run
wordFilter = badWords.BadWordsDB("us-cdbr-iron-east-01.cleardb.net",DBUSER,DBPASS,"heroku_5e695080c7ef107") # Initialize Variables
baddiesList = wordFilter.fetch() # Intialize Baddies List
    
# -------------------------------
# -------- Class Setup ----------
# -------------------------------

users = []
userIDs = []

userDatabase = userDB.UserDB("us-cdbr-iron-east-01.cleardb.net",DBUSER,DBPASS,"heroku_5e695080c7ef107")

for u in userDatabase.fetch():
    users.append(user.User(u[0],u[1],userDatabase,u[2]))
    userIDs.append(u[0])

@client.event
async def on_ready():
    '''
    Asynchronous function that runs when bot is ready, changes status, and prints message
    Reference: https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready
    '''
    await client.change_presence(game=discord.Game(name='with your grades bwahahaha'))
    print("Bot is online")

# -------------------------------
# -------- Functions ------------
# -------------------------------

@client.event
async def on_message(message):
    '''
    Asynchronous function that performs several functions based off of the input message
    Reference: https://discordpy.readthedocs.io/en/latest/api.html#discord.on_message

    Commands
    --------
    !trump [str]: fun command that returns how similar a string is to trump's tweets
    !clear [int]: clears the specified number of messages from current channel
    !add [str]: adds the string to the list of bad words
    !delete [str]: deletes the string from the list of bad words
    !print: sends out the current bad words
    !ping: sends message confirming on_message is successfully run
    !names: list out all names
    !swears: list out swears for current user
    !swears [user object]: list out swears for that user
    !report: reports a message

    ..note:: The function also constantly looks for bad words contained within message,
                outputs a message if it violates the conditions
    '''
    # -------------------------------
    # ---------- Setup --------------
    # -------------------------------

    global baddiesList
    global users

    inputText = message.content # The Message Sent (str)
    print(inputText.split())
    if str(message.author.id) not in userIDs:
        if "seidelion" in [y.name.lower() for y in message.author.roles]:
            newUser = seidelions.Seidelion(str(message.author.id),str(message.author),userDatabase,0,0)
        else:
            newUser = user.User(str(message.author.id),str(message.author),userDatabase,0)
        users.append(newUser)
        userIDs.append(str(message.author.id))
        newUser.insert()


    currentUser = users[userIDs.index(message.author.id)]

    # -------------------------------
    # ------- Experimental ----------
    # -------------------------------


    if inputText.startswith("!names"):
        for u in users:
            await client.send_message(message.channel, u.display())

    if inputText.startswith("!swears"):
        if len(message.mentions) == 0:
            await client.send_message(message.channel, currentUser.swearCount)
        else:
            try:
                mentionedUser = users[userIDs.index(message.mentions[0].id)]
                await client.send_message(message.channel, mentionedUser.swearCount)
            except(ValueError):
                await client.send_message(message.channel,"This user does not exist")
    
    # if inputText.startswith("!report") and inputText.count(' ') > 0:
    #     if "seidelion" in [y.name.lower() for y in message.author.roles]:
    #         admin_channel = discord.utils.get(server.channels, name="administration", type="ChannelType.text") 
    #         await client.send_message(admin_channel,currentUser.report(inputText.split(' ', 1)[1]))

    # -------------------------------
    # -------- Fun Things -----------
    # -------------------------------
    if "Quick, type 'duck'" in inputText:
        await client.send_message(message.channel, "duck")

    if inputText.startswith("!trump") and inputText.count(' ') > 0:
        mes = inputText.split(' ', 1)[1]
        await client.send_message(message.channel, trumpCount.run(mes))

    # -------------------------------
    # -------- Work Things ----------
    # -------------------------------

    # Clears Messages
    if inputText.startswith("!clear") and inputText.count(' ') > 0:
        await clear.run(message,client)
    
    # Add Bad Words
    elif inputText.startswith("!add") and inputText.count(' ') > 0:
        mes = inputText.split(' ', 1)[1]
        if mes in baddiesList:
            await client.send_message(message.channel, "Word already added")
        else: 
            wordFilter.insert(mes,baddiesList) # Run and get status
            await client.send_message(message.channel, "Successfully added %s to database" % mes)
            baddiesList.append(mes)

    # Remove Bad Words
    elif inputText.startswith("!delete") and inputText.count(' ') > 0:
        mes = inputText.split(' ', 1)[1]

        if mes in baddiesList:
            wordFilter.delete(mes)
            await client.send_message(message.channel, "Successfully deleted %s from database" % mes)
            baddiesList = wordFilter.fetch()
        else:
            await client.send_message(message.channel, "You silly. %s is not even a banned word!" % mes)

    # Print Bad Words
    elif inputText.startswith("!print"):
        await client.send_message(message.channel,wordFilter.printAll())
    
    # Filters Messages
    elif not message.author.name == "Mr Seidel":
        vulgar_confidence = filters.run(inputText,baddiesList)
        if vulgar_confidence == 1:
            currentUser.updateSwears()
            await client.send_message(message.channel, "Hey! You can't send that message here! Confidence: 100%")
            # await client.send_message(discord.utils.get())
    
    if inputText.startswith("!ping"):
        await client.send_message(message.channel, ":ping_pong: pong!")

# Run the Bot
client.run(TOKEN)