chat_filter = ["FUCK","BITCH","ASS","FUCKING","CUNT","DESPACITO","IDIOT","PATHETIC"] # Vocabulary

def run(phrase):
    for word in phrase.split(" "): 
        if word.upper() in chat_filter:
            return True

    return False
