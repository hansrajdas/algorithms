#!/usr/bin/python

# Date: 2019-01-02
#
# Description:
# Given an array A[] consisting 0s, 1s and 2s, write a function that sorts A[]
# in single iteration. The functions should put all 0s first, then all 1s and
# all 2s in last.
#
# Approach:
# Approach used is called Dutch National Flag Algorithm, or 3-way Partitioning.
# Take 3 pointers low, mid and high and scan array using mid until mid <= high.
# - 0 to low will have 0s
# - low to mid will have 1s
# - mid to high will be variable - Would shrink later on
# - high to n - 1 will have 2s
# 
# Reference:
# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
#
# Complexity:
# O(n)

def sort_0_1_and_2(a):
  """Sorts an array having 0s, 1s and 2s in ascending order."""
  low = 0
  mid = 0
  high = len(a) - 1

  while mid <= high:
    if a[mid] == 0:
      a[low], a[mid] = a[mid], a[low]
      low += 1
      mid += 1
    elif a[mid] == 1:
      mid += 1
    elif a[mid] == 2:
      a[mid], a[high] = a[high], a[mid]
      high -= 1
    else:
      print 'Invalid input array!'
      return None
  return a

assert sort_0_1_and_2([0, 1, 2]) == [0, 1, 2]
assert sort_0_1_and_2([0, 0, 1, 1, 2, 2]) == [0, 0, 1, 1, 2, 2]
assert sort_0_1_and_2([0, 1, 2, 0, 1, 2]) == [0, 0, 1, 1, 2, 2]
assert sort_0_1_and_2([2, 1, 2, 0, 0, 1, 0, 1]) == [0, 0, 0, 1, 1, 1, 2, 2]
