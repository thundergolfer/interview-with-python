import unittest

def binary_search_one(lst, item):
    first = 0
    last  = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

def binary_search_two( item, lst, lo, hi):
    """ This binary search is recursive and also returns the index of the item. """
    if len(lst) == 0: return -1
    if hi < lo: return -1    # no more numbers to search
    mid = (lo + hi) // 2        # midpoint in array
    if item == lst[mid]:
        return mid
    elif item < lst[mid]:
        return binary_search_two(item, lst, lo, mid -1)     # try left side
    else:
        return binary_search_two(item, lst, mid + 1, hi)    # try right side

# Unit Testing
class Test_Bin_Search(unittest.TestCase):

    def setUp(self):
        pass

    def test_binary_search_one(self):
        self.assertEqual(
            binary_search_one([1,2,3,4,5,6,7,8,9], 4), True
        )
        self.assertEqual( binary_search_one([], 0), False)
        self.assertEqual(
            binary_search_one([1,2,3,4,5,6,7,8,9], 10), False
        )

    def test_binary_search_two(self):
        lst = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(
            binary_search_two(4, lst, 0, len(lst)-1), 3 # index
        )
        self.assertEqual( binary_search_two(0,[], 0, 0), -1) # how does it handle empty list?
        self.assertEqual(
            binary_search_two(10, lst, 0, len(lst)-1), -1
        )

if __name__ == '__main__':
    unittest.main()
