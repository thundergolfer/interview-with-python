import unittest

def euclids_algorithm(a, b):
    """ Calculate the Greatest Common Divisor of a and b. """
    if 0 in [a,b]: return False # You can never divide by 0, so this should fail
    while b:
        a, b = b, a%b
    return a


# Unit testing
class euclids_algorithm_tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_euclids_one(self):
        self.assertEqual( euclids_algorithm( 24, 30 ),  6 )
        self.assertEqual( euclids_algorithm( 1,  10 ),  1 )
        self.assertEqual( euclids_algorithm( 0,  1000), False  )
        self.assertEqual( euclids_algorithm( 300, 300), 300)


if __name__ == '__main__':
    unittest.main()
