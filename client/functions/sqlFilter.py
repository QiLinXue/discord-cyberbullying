from server.functions import badWords

def run(phrase):
    baddies = badWords.fetch()

    for word in phrase.split(" "):
        if word.lower() in baddies:
            return 1

    return 0
