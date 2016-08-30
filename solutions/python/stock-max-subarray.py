import unittest
import math # for infinity, floor, ceiling

def find_max_crossing_subarray( A, low, mid, high ):
    """
    A Divide and Conquer strategy can split an array and find
    the max subarray of those two arrays by spliting those etc. etc. but it
    cannot find if there a subarray that crosses the boundary between the splits is
    the greatest subarray.

    This algorithm supplements the divide and conquer strategy and completes in linear time.
    """

    left_total = -math.inf # negative infinity
    total = 0
    for i in range(mid, low, -1): # descending for-loop
        total += A[i]
        if total > left_total:  # has including this new price, i, improved the total return?
            left_total = total  # yes, so update total and
            max_left = i        # update left boundary
    right_total = -math.inf
    total = 0
    for j in range(mid+1, high): # do the same for right side
        total += A[j]
        if total > right_total:
            right_total = total
            max_right = i
    return max_left, max_right, left_total + right_total

def find_max_subarray( A, low, high ):
    """
    Given an array/list of closing prices, find the
    sublist/subarray which gives the highest difference between
    the buy price (left) and the sell price (right)
    """
    if high == low:
        return low, high, A[low] # base case: only 1 element
    mid = math.floor( (low+high) / 2 )
    left_low, left_high, left_sum = find_max_subarray( A, low, mid ) # recursive call
    right_low, right_high, right_sum = find_max_subarray( A, mid+1, high) # recursive call right side
    cross_low, cross_high, cross_sum = find_max_subarray( A, low, mid, high ) # non-recursive linear time supplement function

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum # we are returning tuples. python is flexible like this :)
