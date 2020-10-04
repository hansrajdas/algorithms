#!/usr/bin/python

# Date: 2020-10-04
#
# Description:
# Determine whether a given set can be partitioned into two subsets such that
# the sum of elements in both subsets is same.
#
# Approach:
# - If sum of all elements in list comes out to be odd, then it is not possible
#   to partition list in 2 subsets having same sum
# - Use recursion to check all combinations, at each element we will have 2
#   conditions whether to take this element or not.
#
# Complexity:
# O(2^n)

def _subset_with_equal_sum(A, idx, current_sum, target):
    if current_sum == target:
        return True
    if idx == len(A):
        return False
    return (
        _subset_with_equal_sum(A, idx + 1, current_sum + A[idx], target) or  # Include current element
        _subset_with_equal_sum(A, idx + 1, current_sum, target))  # Ignore current element

def subset_with_equal_sum(A):
    if sum(A) % 2:
        return False
    return _subset_with_equal_sum(A, 0, 0, sum(A) // 2)


assert subset_with_equal_sum([3, 1, 1, 2, 2, 1]) == True  # 3,1,1 == 2,2,1
assert subset_with_equal_sum([3, 1, 1, 2, 2, 10]) == False
assert subset_with_equal_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == True
assert subset_with_equal_sum([1, 2, 3, 4, 5, 6, 7]) == True
assert subset_with_equal_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == True
assert subset_with_equal_sum([1, 10, 5, 21, 4]) == False
assert subset_with_equal_sum([1, 10, 5, 21, 4, 1]) == True
