f_input = open("data/baddies-basic.txt","r")
baddies_basic = f_input.readlines()
f_input.close()

f_input = open("data/baddies-full.txt","r")
baddies_full = f_input.readlines()
f_input.close()

baddies_basic = [x.strip() for x in baddies_basic]
baddies_full = [x.strip() for x in baddies_full]

def run(phrase):
    for word in phrase.split(" "):
        if word.lower() in baddies_basic:
            return 1
        elif word.lower() in baddies_full:
            return 0.5

    return 0
