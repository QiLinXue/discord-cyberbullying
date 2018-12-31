from textblob import TextBlob

f_input = open("data/baddies-basic.txt","r")
baddiesBasic = f_input.readlines()
f_input.close()

f_input = open("data/baddies-full.txt","r")
baddiesFull = f_input.readlines()
f_input.close()

baddiesBasic = [x.strip() for x in baddiesBasic]
baddiesFull = [x.strip() for x in baddiesFull]

def polarity(phrase):
    '''
    Determines the phrase's polarity

    Parameters
    ----------
    phrase: str
        the phrase to check for profanity

    Returns
    -------
    float
        any float bounded by -1 and 1
        -1 is the most negative
        1 is the most positive
    ''' 
    return TextBlob(phrase).sentiment.polarity

def swears(phrase,baddies):
    '''
    Checks if a word is in the swear list

    Parameters
    ----------
    phrase: str
        the phrase to check for profanity
    baddies: str[]
        the list of bad words

    Returns
    -------
    int
        0 if there are no bad words
        1 if there are bad words
    '''
    for word in phrase.split():
        if word.lower() in baddies:
            return 1

    return 0
