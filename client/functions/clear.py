# pylint: disable=W0614

def getRange(user_input):
    '''
    Gets the range by extracting it from user input

    Parameters
    ----------
    user_input: str
        the user inputed message (prefixed with !clear)
    
    Returns
    -------
    int
        -1 if user didn't type in an integer
        -2 if int is out of range [1,99]
        returns the inputed integer if no errors
    '''

    # Determine how many messages which need to be deleted
    num = user_input.split(" ")[1]

    try:
        if int(num) == float(num):
            num = int(num) + 1
        else:
            return -1
    except ValueError:
        return -1

    # Determine the messages needed to be deleted
    if num < 2 or num > 100:
        return -2

    return num

async def getMessages(message,client):
    '''
    Asynchronous function that gets the specified number of messages

    Parameters
    ----------
    message: discord.message.Message
        The user inputed message including all relevant data
    client: discord.ext.commands.bot.Bot
        The Bot which will perform the actions
    
    Returns
    -------
    int
        -1 if user didn't type in an integer
        -2 if int is out of range [1,99]

    discord.message.Message[]
        Returns the messages to be deleted
    '''
    
    num = getRange(message.content)

    if num < 0:
        return num

    toDelete = client.logs_from(message.channel, limit = num)

    mgs = []
    async for x in toDelete:
        mgs.append(x)

    # Return messages to be deleted
    return mgs

async def run(message,client):
    '''
    Asynchronous function that deletes the specified messages

    Parameters
    ----------
    message: discord.message.Message
        The user inputed message including all relevant data
    client: discord.ext.commands.bot.Bot
        The Bot which will perform the actions

    Returns
    -------
    None
    '''
    mgs = await getMessages(message,client)

    try:
        mgs = int(mgs)
        await client.send_message(message.channel, "Sorry, but the correct format is `!clear num` where num is an int in the range [1,99]")

    except TypeError:
        await client.delete_messages(mgs)
    
    return
