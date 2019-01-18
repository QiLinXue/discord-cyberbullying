import os
from discord.ext.commands import Bot
from dotenv import load_dotenv
from server.imports import * # server imports
from dotenv import load_dotenv


# Initialize Client
client = Bot('')

load_dotenv(verbose=True)
TOKEN = os.getenv('TOKEN')
DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')
DBNAME = os.getenv('DBNAME')

# Setup Bad Word Database
wordFilter = badWords.BadWordsDB(DBHOST,DBUSER,DBPASS,DBNAME) # Initialize Variables
baddiesList = wordFilter.fetch() # Intialize Baddies List

# Setup User Database / Assign Values / Sort Values
userDatabase = userDB.UserDB(DBHOST,DBUSER,DBPASS,DBNAME)
users, userIDs = [], []
for u in userDatabase.fetch():
    if u[4] == "Seidelion":
        users.append(seidelions.Seidelion(u[0],u[1],userDatabase,u[2],"Seidelion",0))
    else:
        users.append(user.User(u[0],u[1],userDatabase,u[2],"User"))
    userIDs.append(u[0])

def inserTionSort(usersList,idList):
    '''
    Implement Insertion Sort to sort users by id, allowing easy id lookup after
    '''
    for i in range(1,len(idList)):

        currentvalue_id, currentvalue_user = idList[i], usersList[i]
        pos = i

        while pos > 0 and idList[pos - 1] > currentvalue_id:
            usersList[pos], idList[pos] = usersList[pos-1], idList[pos-1]
            pos -= 1

        usersList[pos], idList[pos] = currentvalue_user, currentvalue_id
    return (usersList, idList)

sortedTuple = inserTionSort(users,userIDs)
users, userIDs = sortedTuple[0], sortedTuple[1]