def run(phrase,baddies):
    for word in phrase.split(" "):
        if word.lower() in baddies:
            return 1

    return 0
