import unittest
from client.functions.clear import getRange

class TestClear(unittest.TestCase):
    '''
    Test to see if the clear function works so it can delete messages
    '''
    def test_range(self):
        # -2 = Out of Bounds
        # -1 = Text not Numbers
        self.assertEqual(getRange("!clear 99"), 100)
        self.assertEqual(getRange("!clear 100"), -2)
        self.assertEqual(getRange("!clear 1"), 2)
        self.assertEqual(getRange("!clear 0"), -2)
        self.assertEqual(getRange("!clear -1"), -2)
        self.assertEqual(getRange("!clear Trump"), -1)
        self.assertEqual(getRange("!clear 2.5"), -1)
        