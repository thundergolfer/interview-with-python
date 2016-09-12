import unittest

def mergesort_one(lst, show_trace=True):
    if show_trace: print("Splitting ", lst)
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        mergesort_one(left_half)
        mergesort_one(right_half)
        print("Merging ",left_half , right_half)
        i=0
        j=0
        k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k]=left_half[i]
                i=i+1
            else:
                lst[k]=right_half[j]
                j=j+1
            k=k+1

        while i < len(left_half):
            lst[k]=left_half[i]
            i=i+1
            k=k+1

        while j < len(right_half):
            lst[k]=right_half[j]
            j=j+1
            k=k+1
    return lst

def mergesort_two(lst):
    result = []
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left = mergesort_two(lst[:mid])
    right = mergesort_two(lst[mid:])
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]  # one of these will be empty so
    result += right[j:] # we don't need to sort anymore
    return result

# Unit Tests
class Test_Mergesort(unittest.TestCase):
    def setUp(self):
        pass

    def test_mergesort_one(self):
        self.assertEqual(
            mergesort_one([1,5,6,8,9,2,3,4,7]), [1,2,3,4,5,6,7,8,9]
        )
        self.assertEqual(
            mergesort_one([1,2,3,3,4,4,3,3,2,1]), [1,1,2,2,3,3,3,3,4,4]
        )

    def test_mergesort_two(self):
        self.assertEqual(
            mergesort_two([1,5,6,8,9,2,3,4,7]), [1,2,3,4,5,6,7,8,9]
        )
        self.assertEqual( mergesort_two([1]), [1] ) # edge case
        self.assertEqual( mergesort_two([]), [] )   # edge case
        self.assertEqual( mergesort_two([1,2,3,4,5]), [1,2,3,4,5] ) # already sorted case

if __name__ == '__main__':
    unittest.main()
