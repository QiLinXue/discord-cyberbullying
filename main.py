#-----------------------------------------------------------------------------
# Name:        Discord Cyberbullying Bot
# Purpose:     To provide a streamlined process removing cyberbullying from
#              discord using a variety of techniques
#
# Author:      QiLin
# Created:     31-Sep-2018
# Updated:     17-Jan-2019
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

import time
# -------------------------------
# ------- Initialization --------
# -------------------------------

print("Starting up...") # Notify file was run
wordFilter = badWords.BadWordsDB("us-cdbr-iron-east-01.cleardb.net",DBUSER,DBPASS,"heroku_5e695080c7ef107") # Initialize Variables
baddiesList = wordFilter.fetch() # Intialize Baddies List

# for i in filters.baddiesFull:
#     wordFilter.insert(i,baddiesList)
#     print(i)
# -------------------------------
# -------- Class Setup ----------
# -------------------------------

users = []
userIDs = []

userDatabase = userDB.UserDB("us-cdbr-iron-east-01.cleardb.net",DBUSER,DBPASS,"heroku_5e695080c7ef107")

for u in userDatabase.fetch():
    if u[4] == "Seidelion":
        users.append(seidelions.Seidelion(u[0],u[1],userDatabase,u[2],"Seidelion",0))
    else:
        users.append(user.User(u[0],u[1],userDatabase,u[2],"User"))

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
admin_channel = discord.Object(id='517393346432335872')
reporting_channel = discord.Object(id="524369729796833280")
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
    global admin_channel

    inputText = message.content # The Message Sent (str)
    if str(message.author.id) not in userIDs:
        if "seidelion" in [y.name.lower() for y in message.author.roles]:
            newUser = seidelions.Seidelion(str(message.author.id),str(message.author),userDatabase,0,"Seidelion",0)
        else:
            newUser = user.User(str(message.author.id),str(message.author),userDatabase,0,"User")
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

            '''
            Quicksort Implementation
            '''
            def quickSort(usersArr):
                if len(usersArr)==0: return []
                if len(usersArr)==1: return usersArr
                left = [i for i in usersArr[1:] if i.swearCount > usersArr[0].swearCount]
                right = [i for i in usersArr[1:] if i.swearCount <= usersArr[0].swearCount]
                return quickSort(left)+[usersArr[0]]+quickSort(right)

            users = quickSort(users)
            for u in users:
                await client.send_message(message.channel, "Swear Count for %s - %s" % (u.name,u.swearCount))

        else:
            try:
                mentionedUser = users[userIDs.index(message.mentions[0].id)]
                await client.send_message(message.channel, mentionedUser.swearCount)
            except(ValueError):
                await client.send_message(message.channel,"This user does not exist")
    
    if inputText.startswith("!report") and inputText.count(' ') > 0:
        if "seidelion" in [y.name.lower() for y in message.author.roles]:
            reportID = inputText.split(' ', 1)[1]
            reportMessage = None
            for channel in client.get_all_channels():
                try:
                    reportMessage = await client.get_message(channel,reportID)
                except:
                    continue
            await client.send_message(admin_channel,embed=currentUser.report(reportID,reportMessage))
    # -------------------------------
    # -------- Work Things ----------
    # -------------------------------

    # Add Role
    # NOTE clean this part up LOL
    elif inputText.startswith("!addRole") and inputText.count(' ') == 2:

        if len(message.mentions) == 1 and inputText.split()[2].lower() in [y.name.lower() for y in message.server.roles]:
            tempUser = message.server.get_member(message.mentions[0].id)
            role = message.server.roles[([y.name.lower() for y in message.server.roles].index(inputText.split()[2].lower()))]
            await client.add_roles(tempUser, role)
            await client.send_message(message.channel, "Successfully assigned role %s to %s" % (role, tempUser))

            if inputText.split()[2] == "Seidelion":
                tempUserObject = users[userIDs.index(message.mentions[0].id)]
                tempUserObject.updateRole("Seidelion")

                a = users[userIDs.index(message.mentions[0].id)] = seidelions.Seidelion(tempUserObject.id,tempUserObject.name,userDatabase,tempUserObject.swearCount,"Seidelion",0)
        else:
            await client.send_message(message.channel, "There's a problem with your input. Please make sure it's `!addRole @user rolename`")

    # Remove Role
    elif inputText.startswith("!removeRole") and inputText.count(' ') == 2:

        if len(message.mentions) == 1 and inputText.split()[2].lower() in [y.name.lower() for y in message.server.roles]:
            tempUser = message.server.get_member(message.mentions[0].id)
            role = message.server.roles[([y.name.lower() for y in message.server.roles].index(inputText.split()[2].lower()))]
            await client.remove_roles(tempUser, role)
            await client.send_message(message.channel, "Successfully removed role %s from %s" % (role, tempUser))

            if inputText.split()[2] == "Seidelion":
                tempUserObject = users[userIDs.index(message.mentions[0].id)]
                tempUserObject.updateRole("User")

                a = users[userIDs.index(message.mentions[0].id)] = user.User(tempUserObject.id,tempUserObject.name,userDatabase,tempUserObject.swearCount,"User")
        else:
            await client.send_message(message.channel, "There's a problem with your input. Please make sure it's `!removeRole @user rolename`")

    # Clears Messages
    elif inputText.startswith("!clear") and inputText.count(' ') > 0:
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
    # elif not currentUser.perms == "Seidelion":
    elif not message.author.name =="Mr Seidel": # TODO switch to id
        vulgar_confidence = filters.swears(inputText,baddiesList)
        positivity_confidence = filters.polarity(inputText)

        if positivity_confidence < 0:
            currentUser.updateSwears()

            confidence = -100*positivity_confidence
            await client.send_message(message.channel, "Hey! Don't be such a downer! Confidence: %s %%" % confidence)
            await client.send_message(reporting_channel, "!report %s" % message.id)
            # await client.send_message(discord.utils.get())
        
        elif vulgar_confidence == 1 and positivity_confidence <= 0.1:
            currentUser.updateSwears()
            await client.send_message(message.channel, "Hey! You can't send that message here!")
            await client.send_message(reporting_channel, "!report %s" % message.id)
            # await client.send_message(discord.utils.get())

        if positivity_confidence > 0.6:
            filters.qClassifier_train(inputText,'pos')

        print(positivity_confidence)

    if message.author.name == "Mr Seidel" and message.channel.id == admin_channel.id:
        reactions = ['👍','👎']
        for emoji in reactions:
            await client.add_reaction(message,emoji)

        time.sleep(2) # Wait for emojis to add

        while True:
            res = await client.wait_for_reaction(emoji=None, message=message)

            if res.user.id == "495274911795773441": # Prevents time delay glitch where bot recognizes own reaction
                print("intruder detected!")

            elif res.reaction.emoji == '👍':
                tempMesID = message.embeds[0]['fields'][0]["value"]
                tempContent = message.embeds[0]['fields'][1]["value"]
                tempChanID = message.embeds[0]['fields'][2]["value"]

                # Delete Message
                tempMsg = await client.get_message(discord.Object(id=tempChanID), tempMesID)
                await client.delete_message(tempMsg)

                # Train Classifier
                print(tempContent)
                filters.qClassifier_train(tempContent,'neg')

            elif res.reaction.emoji == '👎':
                tempContent = message.embeds[0]['fields'][1]["value"]

                # Train Classifier
                filters.qClassifier_train(tempContent,'pos')

    if inputText.startswith("!ping"):
        await client.send_message(message.channel, ":ping_pong: pong!")

# async def on_reaction_add(reaction,user):
#     print(reaction)
# Run the Bot
client.run(TOKEN)