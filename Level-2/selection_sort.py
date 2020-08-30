#!/usr/bin/python

# Date: 2018-09-08
#
# Description:
# Implement selection sort.
#
# Approach:
# Finds index of minimum(when sorting in ascending) element from the remaining
# array and swap it with element at the end of sorted sub-array.
# While sorting in ascending order minimum element reaches at first place after
# first iteration of outer loop.
#
# Complexity:
# O(n^2)


def selection_sort_ascending(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]  # Swap min with sorted sub-array.

def selection_sort_descending(A):
    for i in range(len(A)):
        max_idx = i
        for j in range(i + 1, len(A)):
            if A[max_idx] < A[j]:
                max_idx = j
        A[max_idx], A[i] = A[i], A[max_idx]

def sort(A):
    B = A[:]
    selection_sort_ascending(A)
    selection_sort_descending(B)
    return (A, B)

assert sort([3, 4, 5, 2, 1]) == ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
assert sort([3, 4, 5, 2, 1, 6]) == ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1])
assert sort([]) == ([], [])
assert sort([1]) == ([1], [1])
assert sort([2, 1]) == ([1, 2], [2, 1])
