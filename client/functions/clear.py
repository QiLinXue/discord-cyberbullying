# pylint: disable=W0614

def getRange(user_input):
    # Determine how many messages which need to be deleted
    try:
        num = user_input.split(" ")[1]
    except:
        return -1

    try:
        if int(num) == float(num):
            num = int(num) + 1
        else:
            return -2
    except:
        return -2

    # Determine the messages needed to be deleted
    if num < 2 or num > 100:
        return -3
    
    return num

async def getMessages(message,client):
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
    mgs = await getMessages(message,client)

    try:
        mgs = int(mgs)
        await client.send_message(message.channel, "Sorry, but the correct format is `!clear num` where num is an int in the range [1,99]")

    except TypeError:
        await client.delete_messages(mgs)
