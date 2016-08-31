import unittest

def solve_heads_tails_one( numheads, numlegs ):
    ns = 'No Solutions!'
    for i in range(numheads+1): # Using a loop to iterate all possible solutions
        j = numheads - i
        if 2*i+4*j == numlegs:
            return i, j
    return ns, ns

def solve_heads_tails_two( numheads, numlegs ):
    raise NotImplementedError # nothing yet, somebody add something!


# Unit Testing
class solve_heads_tails_tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_solve_heads_tails_one(self):
        self.assertEqual(
            solve_heads_tails_one(35, 94), (23, 12)
        )


if __name__ == '__main__':
    unittest.main()
