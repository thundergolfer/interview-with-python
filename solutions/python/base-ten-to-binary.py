# base_ten_to_binary: takes an int, returns the binary representation as a string.
# author: Matt Box
def base_ten_to_binary(num):
    # we'll push the digits into this list, least significant first    
    digits = []
    while num:
        if num & 1:
            digits.append('1')
        else:
            digits.append('0')
        num = num >> 1
    # if we got here with an empty list num was 0 to begin with
    if digits == []:
        digits = ['0']

    digits.reverse()
    return ''.join(digits)

import unittest

class Test(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(base_ten_to_binary(0), '0')
        self.assertEqual(base_ten_to_binary(1), '1')
        self.assertEqual(base_ten_to_binary(10), '1010')

if __name__ == '__main__':
    unittest.main()

