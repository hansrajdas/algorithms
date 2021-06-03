#!/usr/bin/python

# Date: 2020-12-07
#
# Description:
# Find k smallest numbers from an unsorted array.
#
# Approach:
# Quick sort approach is used. The idea is, not to do complete quicksort, but
# stop at the point where pivot itself is k’th smallest element. All elements
# from 0 to pivot will be k smallest numbers. Also, not to recur for both left
# and right sides of pivot, but recur for one of them according to the position
# of pivot.
#
# Note:
# For k largest numbers, we can find (n-k) smallest num - which is
# same as k largest.
#
# Reference:
# Method 4: https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
#
# Heap method is also given at above link which solves problem in
# O(k + (n-k)logk) complexity in worst case.
#
# Complexity:
# Average case - O(N)
# Worst case - O(N^2)


def partition(A, left, right):
  """
  Picks the last element from array - A[right] and places it to correct
  position(with respect to ascending order) and returns index of that position.
  """
  pivot = A[right]
  i = left  # Elements smaller than pivot
  for j in range(left, right + 1):
    if A[j] < pivot:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[i], A[right] = A[right], A[i]  # Move pivot to correct position
  return i
      
def select(A, left, right, k):
    """Returns k smallest numbers in given array."""
    if left == right:
        return A[:left + 1]
    pivot_idx = partition(A, left, right)
    if pivot_idx == k:
        return A[:k + 1]
    elif pivot_idx > k:
        return select(A, left, pivot_idx - 1, k)
    return select(A, pivot_idx + 1, right, k)

def kthSmallest(A, k):
    """Returns k smallest numbers in given array."""
    if k >= len(A):
        return None
    return select(A, 0, len(A) - 1, k)

A = [12, 3, 5, 7, 4, 19, 26]
assert kthSmallest(A, 2) == [3, 4, 5]  # may not always be sorted
assert kthSmallest(A, 3) == [3, 4, 5, 7]
assert kthSmallest(A, 6) == [3, 4, 5, 7, 12, 19, 26]
assert kthSmallest(A, 7) == None
