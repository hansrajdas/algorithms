#!/usr/bin/python

# Date: 2019-01-27
#
# Description:
# Find kth smallest number from an unsorted array.
#
# Approach:
# Quick sort approach is used. The idea is, not to do complete quicksort, but
# stop at the point where pivot itself is k’th smallest element. Also, not to
# recur for both left and right sides of pivot, but recur for one of them
# according to the position of pivot.
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


def partition(A, l, r):
  """
  Picks the last element from array - A[r] and places it to correct position(
  with respect to ascending order) and returns index of that position.
  """
  pivot = A[r]
  i = l  # Elements smaller than pivot
  for j in range(l, r):
    if A[j] <= pivot:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[i], A[r] = A[r], A[i]  # Move pivot to correct position
  return i
      
def kthSmallest(A, l, r, k):
  """Returns kth smallest number in given array."""
  if k > 0 and k <= r - l + 1:  # k is in bounds of array
    pivotIdx = partition(A, l, r)
    if pivotIdx - l == k - 1:
      return A[pivotIdx]
    elif pivotIdx - l > k - 1:  # Check left sub array
      return kthSmallest(A, l, pivotIdx - 1, k)
    return kthSmallest(A, pivotIdx + 1, r, k - pivotIdx + l - 1)  # Check right sub array

  return None  # If k is out of bound return None

A = [12, 3, 5, 7, 4, 19, 26]
assert kthSmallest(A, 0, len(A) - 1, 3) == 5
assert kthSmallest(A, 0, len(A) - 1, 4) == 7
assert kthSmallest(A, 0, len(A) - 1, 7) == 26
assert kthSmallest(A, 0, len(A) - 1, 8) == None
