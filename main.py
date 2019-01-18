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

from serverSetup import *
from client.imports import * # client imports
from server.imports import * # server imports
import discord
import time

print("Starting up...") # Notify file was run

@client.event
async def on_ready():
    '''
    Asynchronous function that runs when bot is ready, changes status, and prints message
    Reference: https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready
    '''
    await client.change_presence(game=discord.Game(name='with your grades bwahahaha'))
    print("Bot is online")


admin_channel = -1
reporting_channel = -1

@client.event
async def on_message(message):
    '''
    Welcome to the Cyberbullying Detection and Assistance Tool. If this is your first
    Asynchronous function that performs several functions based off of the input message
    Reference: https://discordpy.readthedocs.io/en/latest/api.html#discord.on_message

    Commands
    --------
    !trump [str]: fun command that returns how similar a string is to trump's tweets
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

    global baddiesList
    global users
    global admin_channel
    global users, userIDs

    '''
    Update database if it's a new user
    '''
    if str(message.author.id) not in userIDs:
        if "Seidelion" in [y.name for y in message.author.roles]:
            newUser = seidelions.Seidelion(str(message.author.id),str(message.author),userDatabase,0,"Seidelion",0)
        else:
            newUser = user.User(str(message.author.id),str(message.author),userDatabase,0,"User")
        users.append(newUser)
        userIDs.append(str(message.author.id))
        newUser.insert()

    '''
    Predefine commonly used values to increase reusability
    '''
    inputText = message.content # Text of the message
    currentUser = users[userIDs.index(message.author.id)] # The current user typing
    mentionedUser_index = -1 # The index of the user mentioned
    if len(message.mentions) > 0:

        def binarySearch(idList,idToFind): 
            '''
            Binary Search to get index of mentioned user in the "users" array
            '''
            first = 0
            last = len(idList) - 1
            while first <= last: 
        
                mid = (first+last)//2

                if idList[mid] == idToFind: 
                    return mid 
        
                elif idList[mid] < idToFind: 
                    first = mid + 1
        
                else:
                    last = mid - 1

            return -1

        mentionedUser_index = binarySearch(userIDs,message.mentions[0].id)

    admin_channel, reporting_channel = -1, -1
    for channel in message.server.channels:
        if channel.name == "administration":
            admin_channel = discord.Object(id=channel.id)
        if channel.name == "reporting":
            reporting_channel = discord.Object(id=channel.id)

    hasNoChannel = admin_channel == -1 or reporting_channel == -1
    isCommand = inputText.startswith("1") and not inputText == "!setup"
    if hasNoChannel and isCommand:
        await client.send_message(message.channel,"The channels 'administration' and/or 'reporting' are not found. Please initialize setup by typing `!setup`")

    '''
    Experimental (testing)
    '''

    '''
    Administrative Functions
    '''

    if inputText.startswith("!setup"):
        if hasNoChannel:
            # try:
                # Reusable Components
                server = message.server
                everyone = discord.PermissionOverwrite(read_messages=False, send_messages=False)
                mine = discord.PermissionOverwrite(read_messages=True)

                # Create Seidelion Role
                role = await client.create_role(message.server, name='Seidelion', colour=discord.Colour(0x0FF4C6))
                await client.add_roles(message.author, role)

                # Create Administration Channel
                await client.create_channel(server, 'administration', (server.default_role, everyone), (server.me, mine))
                overwrite = discord.PermissionOverwrite(read_messages=True, send_messages=True)
                rolesearch = discord.utils.get(server.roles, name="Seidelion")
                await client.edit_channel_permissions(message.channel, rolesearch, overwrite)
                await client.send_message(message.channel, "The 'administration' channel has been added!")

                # Creating Reporting Channel
                await client.create_channel(server, 'reporting', (server.default_role, everyone), (server.me, mine))
                overwrite = discord.PermissionOverwrite(read_messages=True, send_messages=True)
                rolesearch = discord.utils.get(server.roles, name="Seidelion")
                await client.edit_channel_permissions(message.channel, rolesearch, overwrite)
                await client.send_message(message.channel, "The 'reporting' channel has been added!")

                # Add Role to Admin
                currentUser.updateRole("Seidelion")

                # Update User Database for Admin
                currentUser = seidelions.Seidelion(currentUser.id,currentUser.name,userDatabase,currentUser.swearCount,"Seidelion",0)
                await client.send_message(message.channel, "Successfully assigned role %s to %s" % (role, message.author))

                # Add User Role for Mr Seidel
                tempUser = message.server.get_member("495274911795773441")
                await client.add_roles(tempUser, role)

                # Update User Database for Mr Seidel
                tempUserObject = users[userIDs.index("495274911795773441")]
                tempUserObject.updateRole("Seidelion")
                users[mentionedUser_index] = seidelions.Seidelion(tempUserObject.id,tempUserObject.name,userDatabase,tempUserObject.swearCount,"Seidelion",0)
                await client.send_message(message.channel, "Successfully assigned role 'Seidelion' to self")

                # Initialize custom classifier
                classifiers.qClassifier_init()
                await client.send_message(message.channel, "Successfully created and reset custom classifier")
            # except Exception as e:
            #     print(e)
            #     await client.send_message(message.channel, "Oh no! Something went horrendously wrong.")
        else:
            await client.send_message("Server is already set up")
   
    # Basic Ping for troubleshooting
    elif inputText.startswith("!ping"):
        await client.send_message(message.channel, ":ping_pong: pong!")
    
    elif inputText == "!help":
        await client.send_message(message.channel, on_message.__doc__)
    
    '''
    Functions relating to users
    '''
    if inputText.startswith("!names"):
        for u in users:
            await client.send_message(message.channel, u.display())

    # Add / Remove roles
    if inputText.startswith("!role"):
        isCorrectFormat = inputText.count(' ') == 2 and len(message.mentions) == 1
        isRealRole = inputText.split()[2] in [y.name for y in message.server.roles]
        hasPermissions = currentUser.perms == "Seidelion"

        # Add Roles
        if message.mentions[0].id == "495274911795773441":
            await client.send_message(message.channel, "Sorry, but you can't edit a bot's roles.")

        elif inputText.startswith("!roleAdd") and isCorrectFormat and isRealRole and hasPermissions:
            tempUser = message.server.get_member(message.mentions[0].id)
            role = message.server.roles[([y.name for y in message.server.roles].index(inputText.split()[2]))]
            try:
                await client.add_roles(tempUser, role)
                await client.send_message(message.channel, "Successfully assigned role %s to %s" % (role, tempUser))

                if inputText.split()[2] == "Seidelion":
                    tempUserObject = users[mentionedUser_index]
                    tempUserObject.updateRole("Seidelion")

                    users[mentionedUser_index] = seidelions.Seidelion(tempUserObject.id,tempUserObject.name,userDatabase,tempUserObject.swearCount,"Seidelion",0)
            except Exception as e:
                print(e)
                await client.send_message(message.channel, "Oh No! Something went wrong!")

        # Remove Role
        elif inputText.startswith("!roleRemove") and isCorrectFormat and isRealRole and hasPermissions:
            tempUser = message.server.get_member(message.mentions[0].id)
            role = message.server.roles[([y.name for y in message.server.roles].index(inputText.split()[2]))]
            try:
                await client.remove_roles(tempUser, role)
                await client.send_message(message.channel, "Successfully removed role %s from %s" % (role, tempUser))

                if inputText.split()[2] == "Seidelion":
                    tempUserObject = users[mentionedUser_index]
                    tempUserObject.updateRole("User")
                    users[mentionedUser_index] = user.User(tempUserObject.id,tempUserObject.name,userDatabase,tempUserObject.swearCount,"User")
            except Exception as e:
                print(e)
                await client.send_message(message.channel, "Oh No! Something went wrong!")

        if not hasPermissions:
            await client.send_message(message.channel, "You don't have the permissions to do that!")
        if not isCorrectFormat:
            await client.send_message(message.channel, "There's a problem with your input. Please make sure it's `!roleAdd/roleRemove @user rolename`")
        if not isRealRole:
                await client.send_message(message.channel, "That's not a real role!")

    elif inputText.startswith("!swears"):

        if len(message.mentions) == 0:
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
                mentionedUser = users[mentionedUser_index]
                await client.send_message(message.channel, mentionedUser.swearCount)
            except ValueError as e:
                print(e)
                await client.send_message(message.channel,"This user does not exist")
    
    '''
    Functions relating to Cyberbullying Reporting
    '''

    # Prints the bad word list
    if inputText.startswith("!print"):
        await client.send_message(message.channel,wordFilter.printAll())

    if currentUser.perms == "Seidelion":
        # Add Bad Words
        if inputText.startswith("!add ") and inputText.count(' ') > 0:
            mes = inputText.split()[1]
            if mes in baddiesList:
                await client.send_message(message.channel, "Word already added")
            else:
                wordFilter.insert(mes,baddiesList) # Run and get status
                await client.send_message(message.channel, "Successfully added %s to database" % mes)
                baddiesList.append(mes)

        # Remove Bad Words
        elif inputText.startswith("!delete") and inputText.count(' ') > 0:
            mes = inputText.split()[1]

            if mes in baddiesList:
                wordFilter.delete(mes)
                await client.send_message(message.channel, "Successfully deleted %s from database" % mes)
                baddiesList = wordFilter.fetch()
            else:
                await client.send_message(message.channel, "You silly. %s is not even a banned word!" % mes)

    # Print Bad Words
    elif inputText.startswith("!print"):
        await client.send_message(message.channel,wordFilter.printAll())
    
    # Checks and classifiers messages
    # elif not currentUser.perms == "Seidelion":
    if not message.author.name =="Mr Seidel":
 
        cyberbullying_confidence = classifiers.isCyberbullying(inputText,baddiesList)
        if cyberbullying_confidence > 0:
            currentUser.updateSwears()
            await client.send_message(message.channel, "Hey! Don't be such a downer! Confidence: %s %%" % cyberbullying_confidence)
            await client.send_message(reporting_channel, "!report %s" % message.id)

    # Classification Feedback Mechanism
    if message.author.id == "495274911795773441" and message.channel.id == admin_channel.id and len(message.embeds) > 0:
        reactions = ['👍','👎']
        for emoji in reactions:
            await client.add_reaction(message,emoji)

        time.sleep(2) # Wait for emojis to add

        searching_for_a_meaning_in_life = True
        while searching_for_a_meaning_in_life:
            res = await client.wait_for_reaction(emoji=None, message=message)

            if res.user.id == "495274911795773441": # Prevents time delay glitch where bot recognizes own reaction
                continue

            elif res.reaction.emoji == '👍':
                tempMesID = message.embeds[0]['fields'][0]["value"]
                tempContent = message.embeds[0]['fields'][1]["value"]
                tempChanID = message.embeds[0]['fields'][2]["value"]

                # Delete Message
                tempMsg = await client.get_message(discord.Object(id=tempChanID), tempMesID)
                await client.delete_message(tempMsg)

                # Train Classifier
                classifiers.qClassifier_train(tempContent,'neg')

            elif res.reaction.emoji == '👎':
                tempContent = message.embeds[0]['fields'][1]["value"]

                # Train Classifier
                classifiers.qClassifier_train(tempContent,'pos')

    if inputText.startswith("!report") and inputText.count(' ') > 0:
        if "Seidelion" in [y.name for y in message.author.roles]:
            reportID = inputText.split(' ', 1)[1]
            reportMessage = None
            for channel in client.get_all_channels():
                try:
                    reportMessage = await client.get_message(channel,reportID)
                except Exception as e:
                    print(e)
                    continue
            await client.send_message(admin_channel,embed=currentUser.report(reportID,reportMessage))

    # if inputText == "asidasidjh":
    #     for i in message.server.channels:
    #         if i.name == "administration" or i.name == "reporting":
    #             await client.delete_channel(i)
    #         print(i)
# async def on_reaction_add(reaction,user):
#     print(reaction)
# Run the Bot
client.run(TOKEN)