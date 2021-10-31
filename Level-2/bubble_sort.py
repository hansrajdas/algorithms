#!/usr/bin/python

# Date: 2018-09-08
#
# Description:
# Implement bubble sort.
#
# Approach:
# Compares adjacent elements and pushes to it's required extreme. While
# sorting in ascending order largest element reaches at last place after first
# iteration of outer loop. Vice versa for descending.
#
# Complexity:
# O(n^2) time and O(1) space
# n = number of elements


def bubble_sort_ascending(A):
    """Sorts list of element in ascending order."""
    for i in range(len(A)):
        swap_flag = False;
        for j in range(0, len(A) - 1 - i, 1):
            if (A[j] > A[j + 1]):
                A[j], A[j + 1] = A[j + 1], A[j]
                swap_flag = True;

        if not swap_flag:
            break

def bubble_sort_descending(A):
    """Sorts list of elements in descending order."""
    i = 0
    while i < len(A):
        j = 1
        has_swap = False
        while j < len(A) - i:
            if A[j - 1] < A[j]:
                has_swap = True
                A[j - 1], A[j] = A[j], A[j - 1]
            j += 1
        i += 1
        if not has_swap:
            break

def sort(A):
    B = A[:]
    bubble_sort_ascending(A)
    bubble_sort_descending(B)
    return (A, B)

# Test
assert sort([3, 4, 5, 2, 1]) == ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
assert sort([3, 4, 5, 2, 1, 6]) == ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1])
assert sort([]) == ([], [])
assert sort([1]) == ([1], [1])
assert sort([2, 1]) == ([1, 2], [2, 1])
