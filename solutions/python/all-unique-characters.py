# Check if a string is composed of all unique characters
# author: Matt Box
import unittest

def all_unique(string):
    
    # Optimization that assumes only 255 ASCII characters are possible (ignores possibility of unicode)
    nLetters = len(letters)
    if (nLetters > 255):
        return False
    
    letters = sorted(string)
    for i in range(nLetters - 1):
        if letters[i] == letters[i + 1]:
            return False
    return True

class Test(unittest.TestCase):
    def test_sanity(self):
        self.assertFalse(all_unique("foo"))
        self.assertTrue(all_unique("bar"))

if __name__ == '__main__':
    unittest.main()

