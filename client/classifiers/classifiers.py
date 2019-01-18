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

'''
Text Blob Classifier
'''

def textblobClassifier_classify(phrase):
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
        1 is the most negative
        -1 is the most positive
    '''
    return -1 * TextBlob(phrase).sentiment.polarity

'''
Swear Word Classifier
'''

def swearClassifier_classify(phrase,baddies):
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

    return -1

'''
Custom Classifier
'''

def qClassifier_init():
    train = [
        ('I love this sandwich.', 'pos'),
        ('this is an amazing place!', 'pos'),
        ('I feel very good about these beers.', 'pos'),
        ('this is my best work.', 'pos'),
        ("what an awesome view", 'pos'),
        ('I do not like this restaurant', 'neg'),
        ('I am tired of this stuff.', 'neg'),
        ('he is my sworn enemy!', 'neg'),
        ('my boss is horrible.', 'neg')
    ]
    cl = NaiveBayesClassifier(train)
    qClassifier_f = open('client/classifiers/qClassifier.pickle','wb')
    pickle.dump(cl,qClassifier_f)
    qClassifier_f.close()

def qClassifier_classify(phrase):
    qClassifier_f = open('client/classifiers/qClassifier.pickle','rb')
    qClassifier = pickle.load(qClassifier_f)
    qClassifier_f.close()
    return qClassifier.prob_classify(phrase).prob("neg")

def qClassifier_train(phrase,sentiment):
    qClassifier_f = open('client/classifiers/qClassifier.pickle','rb')
    qClassifier = pickle.load(qClassifier_f)
    qClassifier_f.close()

    new_Data = [(phrase, sentiment)]
    qClassifier.update(new_Data)

    qClassifier_f = open('client/classifiers/qClassifier.pickle','wb')
    pickle.dump(qClassifier,qClassifier_f)
    qClassifier_f.close()

'''
Combined Classifier
'''

def isCyberbullying(phrase,baddiesList):
    vulgar_confidence = swearClassifier_classify(phrase,baddiesList)
    positivity_confidence = textblobClassifier_classify(phrase)
    qClassifier_confidence = qClassifier_classify(phrase)
    confidence = -999

    if positivity_confidence > 0:
        confidence = 100*positivity_confidence
        
    elif vulgar_confidence == 1 and positivity_confidence >= 0.1:
        confidence = 20

    elif vulgar_confidence == 1 and qClassifier_confidence >= 0.8:
        confidence = 100*qClassifier_confidence

    else:
        # I'm operating on the assumption that there will be more positives than false positives
        qClassifier_train(phrase,'pos')

    return confidence
