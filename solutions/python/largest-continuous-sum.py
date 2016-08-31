"""solution to the largest-continuous-sum problem"""
import unittest
from functools import reduce

def largest_continuous_sum_one(arr):
    """ returns the largest continous sub sequence in the given list of numbers. """
    largest = 0
    queue = []
    for num in arr:
        queue.append(num)
        if len(queue) > 1:
            curr_sum = reduce(lambda x, y: x + y, queue)
            curr_sum = curr_sum if curr_sum > num else num
            if largest < curr_sum:
                largest = curr_sum

    return largest



def largest_continous_sum_two(arr):
    if len(arr) == 0: # handle an edge case
        return None
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum=max(current_sum+num, num)
        max_sum=max(current_sum, max_sum)
    return max_sum


# Unit testing
class largest_continous_sum_test(unittest.TestCase):

    def setUp(self):
        self.arrOne = [1,2,3,4,5]
        self.arrTwo = [4,5,1,-1000]

    def test_largest_continuous_sum_one(self):
        self.assertEqual(
            largest_continuous_sum_one( self.arrOne ), 15
        )
        self.assertEqual(
            largest_continuous_sum_one( self.arrTwo ), 10
        )

    def test_largest_continous_sum_two(self):
        self.assertEqual(
            largest_continous_sum_two( self.arrOne ) , 15
        )
        self.assertEqual(
            largest_continous_sum_two( self.arrTwo ), 10
        )

if __name__ == '__main__':
    unittest.main()
