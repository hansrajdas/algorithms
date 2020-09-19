# Date: 2020-09-19
#
# Description:
# Given a sorted array and an integer X, find floor and ceil of X from array.
# For example:
# A = [3, 4, 7, 8, 10], X = 5 so floor of 5 would be 4 and ceil would be 7
#
# Approach:
# First check for corner cases that is:
# - If X is smaller than first element in array
# - If X is larger than last element in array
# - If above 2 don't meet do a binary search and check if we are able to find
#   same number as X in array or we are able to find a condition a[m] < X and
#   a[m + 1] > X
#
# Complexity:
# O(logn)

def get_floor_ceil(A, x):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if A[mid] == x:
            return (A[mid], A[mid])
        if mid < len(A) - 1 and A[mid] < x and A[mid + 1] > x:
            return (A[mid + 1], A[mid])
        if A[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return (A[0], None) if A[0] > x else (None, A[-1])

assert get_floor_ceil([1, 2, 3, 4, 5], 4) == (4, 4)
assert get_floor_ceil([1, 2, 5, 8, 10, 15, 18], 12) == (15, 10)
assert get_floor_ceil([1, 2, 5, 8, 10, 15, 18], 20) == (None, 18)
assert get_floor_ceil([1, 2, 5, 8, 10, 15, 18], -20) == (1, None)
