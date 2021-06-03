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
# Note:
# For kth largest number, we can find (n-k)th smallest num - which is
# same as kth largest.
#
# Reference:
# Method 4: https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
#
# Heap method is also given at above link which solves problem in
# O(k + (n-k)logk) complexity in worst case: Level-2/find_kth_largest_num.py
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
  for j in range(l, r + 1):
    if A[j] < pivot:
      A[i], A[j] = A[j], A[i]
      i += 1
  A[i], A[r] = A[r], A[i]  # Move pivot to correct position
  return i

def select(A, left, right, k):
    if left == right:
        return A[left]
    pivot_idx = partition(A, left, right)
    if pivot_idx == k:
        return A[k]
    elif pivot_idx > k:
        return select(A, left, pivot_idx - 1, k)  # Check left sub array
    return select(A, pivot_idx + 1, right, k)  # Check right sub array

def kthSmallest(A, k):
    """Returns kth(0 to len(A) - 1) smallest number in given array."""
    if k >= len(A):
        return None
    return select(A, 0, len(A) - 1, k)


A = [12, 3, 5, 7, 4, 19, 26]
sorted_nums = sorted(A)
assert kthSmallest(A, 0) == sorted_nums[0]
assert kthSmallest(A, 2) == sorted_nums[2]
assert kthSmallest(A, 3) == sorted_nums[3]
assert kthSmallest(A, 6) == sorted_nums[6]
assert kthSmallest(A, 7) == None
