f_input = open("data/baddies.txt","r")
baddies = f_input.readlines()
f_input.close()

baddies = [x.strip() for x in baddies]

def run(phrase):
    for word in phrase.split(" "):
        if word.lower() in baddies:
            return True

    return False
