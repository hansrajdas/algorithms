#!/usr/bin/python

"""
Date: 2018-09-08

Description:
Implement bubble sort.

Approach:
Compares adjacent elements and pushes to it's extreme end. While
sorting in ascending order largest element reaches at last place after first
iteration of outer loop. For descending smallest reaches to the last place.

Complexity:
O(n^2)
"""

def bubble_sort_ascending(A):
    for i in range(len(A)):
        swap_flag = False;
        for j in range(0, len(A) - 1 - i, 1):
            if (A[j] > A[j + 1]):
                A[j], A[j + 1] = A[j + 1], A[j]
                swap_flag = True;

        if not swap_flag:
            break

def bubble_sort_descending(A):
    for i in range(len(A)):
        swap_flag = False;
        for j in range(0, len(A) - 1 - i, 1):
            if (A[j] < A[j + 1]):
                A[j], A[j + 1] = A[j + 1], A[j]
                swap_flag = True;

        if not swap_flag:
            break

def sort(A):
    B = A[:]
    bubble_sort_ascending(A)
    bubble_sort_descending(B)
    return (A, B)


assert sort([5, 4, 3, 2, 1, 10, 28, 7, 6]) == ([1, 2, 3, 4, 5, 6, 7, 10, 28], [28, 10, 7, 6, 5, 4, 3, 2, 1])
assert sort([3, 4, 5, 2, 1]) == ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
assert sort([3, 4, 5, 2, 1, 6]) == ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1])
assert sort([]) == ([], [])
assert sort([1]) == ([1], [1])
assert sort([2, 1]) == ([1, 2], [2, 1])
