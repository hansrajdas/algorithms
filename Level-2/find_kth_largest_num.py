#!/usr/bin/python

# Date: 2019-01-27
#
# Description:
# Find kth largest number from an unsorted array.
#
# Approach:
# Create a min heap of size K - A[0 to K-1] and iterate over elements from A[k]
# to A[n-1] if A[idx] is more than current heap root, replace root with A[idx]
# and run heapify method again. At the end A[0] will have kth largest element.
#
# Note: For Kth smallest element we need to create max heap and follow similar
# approach.
#
# Complexity:
# O(k + (n-k)logk)
#
# There is another method also to solve this problem, it uses variant of quick
# sort - Has an average case complexity of O(N) but worst case comes out to be
# O(N^2). Implemented here for kth smallest:
# https://github.com/hansrajdas/algorithms/blob/master/Level-3/find_kth_smallest_num.py

def min_heapify(A, n, idx):
  smallest_idx = idx
  left = 2*idx + 1
  right = 2*idx + 2
  if left < n and A[smallest_idx] > A[left]:
    smallest_idx = left
  if right < n and A[smallest_idx] > A[right]:
    smallest_idx = right
    
  if smallest_idx != idx:
    A[smallest_idx], A[idx] = A[idx], A[smallest_idx]
    min_heapify(A, n, smallest_idx)
    
def findKthLargest(nums, k):
  """
  :type nums: List[int]
  :type k: int
  :rtype: int
  """
  # Heapify first k elements
  for idx in range(int(k/2), -1, -1):
    min_heapify(nums, k, idx)
    
  for idx in range(k, len(nums)):
    if nums[0] < nums[idx]:
      nums[0] = nums[idx]
      min_heapify(nums, k, 0)
  return nums[0]

assert findKthLargest([1, 2, 3, 4, 5], 2) == 4
assert findKthLargest([5, 4, 1, 2, 3], 2) == 4
assert findKthLargest([5, 4, 1, 2, 3], 1) == 5
