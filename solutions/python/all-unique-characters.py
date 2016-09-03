# Check if a string is composed of all unique characters
# author: Matt Box
import unittest

def all_unique(string):
    letters = sorted(string)
    for i in range(len(letters) - 1):
        if letters[i] == letters[i + 1]:
            return False
    return True

class Test(unittest.TestCase):
    def test_sanity(self):
        self.assertFalse(all_unique("foo"))
        self.assertTrue(all_unique("bar"))

if __name__ == '__main__':
    unittest.main()

