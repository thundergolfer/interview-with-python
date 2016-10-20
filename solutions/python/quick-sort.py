from random import randint
import unittest
from math import ceil

def quickSort(lst):
    # List of 0 or 1 items is already sorted
    if len(lst) <= 1:
        return lst
    else:
        # Pivot can be chosen randomly
        pivotIndex = randint(0, len(lst)-1)
        pivot = lst[pivotIndex]
        # Elements lower than and greater than pivot
        lesser, greater = [], []

        for index in range(len(lst)):
            # Don't do anything if you're at the pivot
            if index == pivotIndex:
                pass
            else:
                # Sort elements into < pivot and >= pivot
                el = lst[index]
                if el < pivot:
                    lesser.append(el)
                else:
                    greater.append(el)

        # Sort lesser and greater, concatenate results
        return quickSort(lesser) + [pivot] + quickSort(greater)


def quickSort_two(lst):
    """
    This algorithm is intuitive, but does not map closely to the lower-level
    Java and C++ implementations of quickSort.
    """

    if len(lst) <= 1:
        return lst
    pivotIndx = len(lst) - 1 # put pivot at end
    pivot = lst[pivotIndx]
    # Elems lower than and greater than pivot
    lesser, equal, greater = [], [], []
    for i in range(len(lst)):
        if i == pivot:
            equal.append(x)
        elif i < pivot:
            less.append(x)
        elif i > pivot:
            greater.append(x)
    return quickSort_two(less) + equal + quickSort_two(greater) # just use + to join lists

# def quickSort_three(lst):
#     def quickSort_partition(lst, low, high ):
#         pivot = lst[ceil(low + (high-low)/2)]
#         i, j = low, high
#         while i <= j:
#             # If the curr value from the left list is smaller then the pivot
#             # elem then get the next element from the left list
#             while lst[i] < pivot:
#                 i += 1
#             # If the current value from the right list is larger than the pivot
#             # elem then get the next element from the right list
#             while lst[high] > pivot:
#                 high -= 1
#
#             # If we have found a value in the left list which is larger than
#             # the pivot element and if we have found a vluae int the right list
#             # which is smaller than the pivot element then we exchange the values.
#             if i <= high:
#                 exchange(lst, i, high)
#                 i += 1
#                 high += 1
#         if low < j:
#             quickSort_partition(lst, low, j)
#         if i < high:
#             quickSort_partition(lst, i, high)
#         return lst
#
#     def exchange(lst, i, j):
#         temp = lst[i]
#         lst[i] = lst[j]
#         lst[j] = temp
#         return lst
#     # Algorthim body
#     if len(lst) <= 1:
#         return lst
#     quickSort_partition(lst, 0, len(lst) - 1)
#


class Test_QuickSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_quickSort_one(self):
        self.assertEqual(
            quickSort([1,4,3,5,9,8,2,6,7]), [1,2,3,4,5,6,7,8,9]
        )
        self.assertEqual( quickSort([]), [] )
        self.assertEqual( quickSort([2]), [2])
        self.assertEqual( quickSort([1,2,3,4,5,6]), [1,2,3,4,5,6])

    def test_quickSort_two(self):
        pass

    # def test_quickSort_three(self):
    #     self.assertEqual(
    #         quickSort_three([1,2,3,4,5]), [1,2,3,4,5]
    #     )



if __name__ == '__main__':
    unittest.main()
