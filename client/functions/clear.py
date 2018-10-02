# pylint: disable=W0614
from bot_setup import *

async def get(message):
    
    # Determin how many messages which need to be deleted
    num = message.content.split(" ")[1]
    try:
        num = int(num) + 1
    except:
        return -1

    # Determine the messages needed to be deleted
    if num < 2 or num > 100:
        return -1
        
    toDelete = client.logs_from(message.channel, limit = num)

    mgs = []
    async for x in toDelete:
        mgs.append(x)

    # Return messages to be deleted
    return mgs

async def run(message):
    mgs = await get(message)

    if mgs == -1:
        await client.send_message(message.channel, "Sorry, but the correct format is `!clear num` where num is an int in the range [1,99]")
    else:
        await client.delete_messages(mgs)
