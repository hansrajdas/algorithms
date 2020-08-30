#!/usr/bin/python

# Date: 2018-09-08
#
# Description:
# Implement insertion sort.
#
# Approach:
# Scans from right in sorted sub-array and inserts current element at correct
# place by shifting all the elements to right.
#
# Complexity:
# O(n^2)


def insertion_sort_increasing(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key  # Insert current element at correct place.

def insertion_sort_descending(A):
    for i in range(1, len(A)):  # Fisrt element is sorted in itself
        element = A[i]
        j = i
        while j and A[j - 1] < element:
            A[j] = A[j - 1]
            j -= 1
        A[j] = element

def sort(A):
    B = A[:]
    insertion_sort_increasing(A)
    insertion_sort_descending(B)
    return (A, B)

assert sort([3, 4, 5, 2, 1]) == ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
assert sort([3, 4, 5, 2, 1, 6]) == ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1])
assert sort([]) == ([], [])
assert sort([1]) == ([1], [1])
assert sort([2, 1]) == ([1, 2], [2, 1])
