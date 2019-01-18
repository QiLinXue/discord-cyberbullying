from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import pickle

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

def inittt():
    train = [
        ('I love this sandwich.', 'pos'),
        ('this is an amazing place!', 'pos'),
        ('I feel very good about these beers.', 'pos'),
        ('this is my best work.', 'pos'),
        ("what an awesome view", 'pos'),
        ('I do not like this restaurant', 'neg'),
        ('I am tired of this stuff.', 'neg'),
        ("I can't deal with this", 'neg'),
        ('he is my sworn enemy!', 'neg'),
        ('my boss is horrible.', 'neg')
    ]
    cl = NaiveBayesClassifier(train)
    qClassifier_f = open('classifier/qClassifier.pickle','wb')
    pickle.dump(cl,qClassifier_f)
    qClassifier_f.close()

def qClassifier_classify(phrase):
    qClassifier_f = open('classifier/qClassifier.pickle','rb')
    qClassifier = pickle.load(qClassifier_f)
    qClassifier_f.close()
    return qClassifier.prob_classify(phrase).prob("neg")

def qClassifier_train(phrase,sentiment):
    qClassifier_f = open('classifier/qClassifier.pickle','rb')
    qClassifier = pickle.load(qClassifier_f)
    qClassifier_f.close()

    new_Data = [(phrase, sentiment)]
    qClassifier.update(new_Data)

    qClassifier_f = open('classifier/qClassifier.pickle','wb')
    pickle.dump(qClassifier,qClassifier_f)
    qClassifier_f.close()

# print(qClassifier_classify("My lords are stupid"))
# qClassifier_train("My lords are stupid","neg")
# print(qClassifier_classify("My lords are stupid"))

# b = open('classifier/qClassifier.pickle','rb')
# cl = pickle.load(b)
# b.close()
# print(cl.classify("This is an amazing library!"))
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
