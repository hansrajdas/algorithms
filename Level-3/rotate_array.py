#!/usr/bin/python

# Date: 2018-11-17
#
# Description:
# Rotate an array left/right by d number of rotations.
#
# Approach:
# For left rotation:
# 1. Consider array as 2 subarrays of length 0 to d - 1 and d to n - 1 
# 2. Reverse A[0 to d - 1]
# 3. Reverse A[d to n - 1]
# 4. Now reverse whole array A[0 to n - 1]
#
# For right rotation do steps 2, 3 and 4 in reverse order
#
# Complexity:
# O(N)
#
# Reference:
# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

def reverse_array(A, start, end):
  """Reverses subarray from start index to end index."""
  s = start
  e = end
  while s < e:
    t = A[s]
    A[s] = A[e]
    A[e] = t
    s += 1
    e -= 1

def left_rotate(A, d):
  """Rotates array A left by d number of times."""
  if not A:
    return A

  n = len(A)
  d = d % n  # If d > n, get the effective number of left rotations

  # 1. Reverse first half of array: 0 to d - 1
  # 2. Reverse second half of array: d to n - 1
  # 3. Reverse whole array
  reverse_array(A, 0, d - 1)
  reverse_array(A, d, n - 1)
  reverse_array(A, 0, n - 1)

  return A

def right_rotate(A, d):
  """Rotates array A right by d number of times."""
  if not A:
    return A

  n = len(A)
  d = d % n  # If d > n, get the effective number of right rotations

  # 1. Reverse whole array
  # 2. Reverse second half of array: d to n - 1
  # 3. Reverse first half of array: 0 to d - 1
  reverse_array(A, 0, n - 1)
  reverse_array(A, d, n - 1)
  reverse_array(A, 0, d - 1)

  return A


# Test cases
assert left_rotate([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
assert left_rotate([1, 2, 3, 4, 5], 1) == [2, 3, 4, 5, 1]
assert left_rotate([1, 2, 3, 4, 5], 11) == [2, 3, 4, 5, 1]  # Effectively 1 left rotate.
assert left_rotate([], 0) == []
assert left_rotate([1], 100) == [1]

assert right_rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert right_rotate([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
assert right_rotate([1, 2, 3, 4, 5], 11) == [5, 1, 2, 3, 4]  # Effectively 1 left rotate.
assert right_rotate([], 0) == []
assert right_rotate([1], 100) == [1]
