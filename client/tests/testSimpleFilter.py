import unittest
from client.functions.simpleFilter import run, baddies_basic,baddies_full

class TestSimpleFilter(unittest.TestCase):

    def test_range(self):
        # 1 = Contains Swear Word
        self.assertEqual(run("You're a fucking idiot"),1)
        self.assertEqual(run("I like PATHETIC people"),1)
        self.assertEqual(run(" ".join(baddies_basic)),1)
        self.assertEqual(run("YOU cUnT"),1)

        # 0.5 = Might contain swear word
        self.assertEqual(run("you ArSe"),0.5)
        self.assertEqual(run(" ".join(baddies_full)),0.5)
        self.assertEqual(run("ur a f.u.c.k boy"),0.5)
        self.assertEqual(run("you wanna doggystyle me"),0.5)

        # 0 = Doesn't Contain Swear Word
        self.assertEqual(run("I have many assets"),0)
        self.assertEqual(run("\s"),0) # pylint: disable=W1401
