import unittest
from client.functions.simpleFilter import run, chat_filter

class TestSimpleFilter(unittest.TestCase):

    def test_range(self):
        # True = Contains Swear Word
        self.assertTrue(run("You're a fucking idiot"))
        self.assertTrue(run("I like PATHETIC people"))
        self.assertTrue(run(" ".join(chat_filter)))
        self.assertTrue(run("YOU cUnT"))

        # False = Doesn't Contain Swear Word
        self.assertFalse(run("I have many assets"))
        self.assertFalse(run("\s")) # pylint: disable=W1401