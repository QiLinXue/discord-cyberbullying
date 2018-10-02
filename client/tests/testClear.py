import unittest
from client.functions.clear import getRange

class TestClear(unittest.TestCase):

    def test_range(self):
        # -3 = Out of Bounds
        # -2 = Text not Numbers
        # -1 = No Parameters
        self.assertEqual(getRange("!clear 99"), 100)
        self.assertEqual(getRange("!clear 100"), -3)
        self.assertEqual(getRange("!clear 1"), 2)
        self.assertEqual(getRange("!clear 0"), -3)
        self.assertEqual(getRange("!clear -1"), -3)
        self.assertEqual(getRange("!clear Trump"), -2)
        self.assertEqual(getRange("!clear"), -1)
        self.assertEqual(getRange("!clear 2.5"), -2)
        