# pairs_sum_to_ten
# find pairs in a list that sum to ten
# author: Matt Box
import unittest

# 1. the easy way: quadratic time (O(n**2))
def pairs_sum_to_ten1(lst):
    pairs = []
    lst.sort()
    for left in lst:
        # check against the numbers to the right of "left":
        for right in lst[(lst.index(left) + 1):]:
            if left + right == 10:
                pairs.append((left,right))
    return pairs

# 2. the tricky way: linear time (O(n))
# (not counting the sort)
def pairs_sum_to_ten2(lst):
    pairs = []
    lst.sort()
    l_index = 0;
    r_index = len(lst) - 1
    while l_index != r_index:
        left = lst[l_index]
        right = lst[r_index]
        s = left + right
        if s == 10:
            pairs.append((left, right))
            l_index += 1
            continue
        # the sum != 10:
        if s < 10:
            l_index += 1
            continue
        # the sum is > 10:
        r_index -= 1

    return pairs

class Test(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(pairs_sum_to_ten1([2,4,6,8]),
                [(2,8), (4,6)])
        self.assertEqual(pairs_sum_to_ten2([2,4,6,8]),
                [(2,8), (4,6)])

        self.assertEqual(pairs_sum_to_ten2([2,4,5,6,8]),
                [(2,8), (4,6)])
        self.assertEqual(pairs_sum_to_ten1([2,4,5,6,8]),
                [(2,8), (4,6)])

        self.assertEqual(pairs_sum_to_ten1([-10,-5,0,5,10,15,20]),
                [(-10,20), (-5,15), (0,10)])
        self.assertEqual(pairs_sum_to_ten2([-10,-5,0,5,10,15,20]),
                [(-10,20), (-5,15), (0,10)])

if __name__ == '__main__':
    unittest.main()

