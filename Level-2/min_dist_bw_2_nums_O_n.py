# Date: 2020-10-01
#
# Description:
# Given an unsorted array and 2 numbers, find the minimum distance between 2
# given numbers in array.
#
# Approach:
# - Scan array and find any of the 2 element, once found save the index and
#   break from loop.
# - Now scan array further and check if any of the 2 element appears again, if
#   it is same as at saved index, updated index to new index
# - otherwise check if min distance is less than previously saved update that
#
# Complexity:
# O(N)

def min_dist(A, n1, n2):
    _min = len(A) - 1
    for i in range(len(A)):
        if A[i] == n1 or A[i] == n2:
            first_idx = i
            break
    for i in range(first_idx + 1, len(A)):
        if A[i] == A[first_idx]:
            first_idx = i
        elif A[i] == n1 or A[i] == n2:
            _min = min(_min, i - first_idx)
            first_idx = i
    return _min
            

assert min_dist([3, 5, 2, 1, 8, 4, 3], 2, 3) == 2
assert min_dist([2, 3, 5, 1, 9, 8, 3], 2, 3) == 1
