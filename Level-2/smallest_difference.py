#!/usr/bin/python

# Date: 2020-11-13
#
# Description:
# Given 2 arrays of integers, compute the pair of values(one value in each
# array) with the smallest difference. Return the difference.
#
# Approach:
# Sort both arrays and walk through elements of each array, increment pointer
# of array having smaller elements.
#
# Complexity:
# O(Alog(A) + Blog(B))


def get_smallest_difference(A, B):
    if not (A and B):
        return -1
    A.sort()
    B.sort()

    i = 0
    j = 0
    diff = float('inf')
    while i < len(A) and j < len(B):
        diff = min(diff, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return diff

assert get_smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]) == 3
assert get_smallest_difference([], [23, 127, 235, 19, 8]) == -1
assert get_smallest_difference([1, 3, 5, 7], [2, 4, 6, 8]) == 1
assert get_smallest_difference([1, 3, 5, 7], [1, 2, 4, 6, 8]) == 0
