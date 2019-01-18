import unittest
from client.classifiers.classifiers import run, baddiesBasic

class TestClassifiers(unittest.TestCase):
    '''
    Tests to see if the classifier works
    '''
    def test_range(self):
        # 1 = Contains Swear Word
        self.assertEqual(run("You're a fucking idiot",baddiesBasic),1)
        self.assertEqual(run("I like PATHETIC people",baddiesBasic),1)
        self.assertEqual(run(" ".join(baddiesBasic),baddiesBasic),1)
        self.assertEqual(run("YOU cUnT",baddiesBasic),1)

        # 0 = Doesn't Contain Swear Word
        self.assertEqual(run("I have many assets",baddiesBasic),0)
        self.assertEqual(run("\s",baddiesBasic),0) # pylint: disable=W1401
