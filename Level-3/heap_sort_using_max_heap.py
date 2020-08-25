#!/usr/bin/python

# Date: 2020-08-25
#
# Description:
# Transform an array to max heap and sort in ascending order. Max heap has
# largest element at 0th index always. In sorting we can copy 0th index element
# to last and run max-heapify again to have next max at 0th index.
# So max heap is used to sort array in ascending order and min heap can be used
# to sort array in descending order.
#
# Complexity:
# Building heap has O(n)
# Sorting takes O(n*log(n))

def max_heapify(A, n, i):
    left = (i << 1) + 1
    right = (i << 1) + 2
    max_idx = i

    # Select min b/w left and right child if current(i) is not maximum then
    # swap. Compared with left child fist because heap should always be left
    # filled
    if left < n and A[max_idx] < A[left]:
        max_idx = left
    if right < n and A[max_idx] < A[right]:
        max_idx = right

    # If current index element is not largest than it's left and right child
    # then swap current index element with larger element.
    if max_idx != i:
        A[i], A[max_idx] = A[max_idx], A[i]
        max_heapify(A, n, max_idx)

def max_heap(A):
    # Building min heap. Building min heap has total complexity of O(n).
    # Refer: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
    # This loop is run from n/2 down to 0 with an assumption that lower level
    # elements (from n/2+1 to n) in heap is already heapfied.
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, len(A), i)

    # Sort in ascending order
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]  # Swap 0th with last element of heap
        max_heapify(A, i, 0)  # Max heapify w.r.t fist element

    return A

assert(max_heap([5, 4, 3, 2, 1])) == [1, 2, 3, 4, 5]
assert(max_heap([5, 4, 3, 2, 1, -10])) == [-10, 1, 2, 3, 4, 5]
assert(max_heap([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 3, 4, 5, 6, 7]
