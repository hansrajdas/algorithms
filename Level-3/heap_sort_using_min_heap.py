#!/usr/bin/python

"""
Date: 2020-08-25

Description:
Transform an array to min heap and sort in descending order. Min heap has
smallest element at 0th index always. In sorting we can copy 0th index
element to last index and run min-heapify again to have next min at 0th
index.
So min heap is used to sort array in descending order and max heap can be
used to sort array in ascending order.

Complexity:
Building heap has O(n)
Sorting takes O(n*log(n))
"""

def min_heapify(A, n, i):
    left = (i << 1) + 1
    right = (i << 1) + 2
    min_idx = i
    
    # Select min b/w left and right child if current(i) is not minimum then
    # swap. Compared with left child fist because heap should always be left
    # filled.
    if left < n and A[min_idx] > A[left]:
        min_idx = left
    if right < n and A[min_idx] > A[right]:
        min_idx = right

    # If current index element is not smallest than it's left and right child
    # then swap current index element with smaller element.
    if min_idx != i:
        A[min_idx], A[i] = A[i], A[min_idx]
        min_heapify(A, n, min_idx)

def heap_sort(A):
    # Building min heap. Building min heap has total complexity of O(n).
    # Refer: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
    # This loop is run from n/2 down to 0 with an assumption that lower level
    # elements (from n/2+1 to n) in heap is already heapfied.
    for i in range(len(A) // 2, -1, -1):
        min_heapify(A, len(A), i)

    # Sort in descending order
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]  # Swap first and last element
        min_heapify(A, i, 0)  # Min heapify w.r.t first element

    return A  # This return is not required. A is sorted inplace, for testing returned

assert heap_sort([4, 5, 1, 3, 9]) == [9, 5, 4, 3, 1]
assert heap_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert heap_sort([4, 5, 1, 3, 9, 3]) == [9, 5, 4, 3, 3, 1]
