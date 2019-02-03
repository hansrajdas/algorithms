#!/usr/bin/python

# Date: 2019-02-03
#
# Description:
# Given an array, print the Next Greater Element (NGE) for every element. The
# Next greater Element for an element x is the first greater element on the
# right side of x in array. Elements for which no greater element exist,
# consider next greater element as -1
#
# Approach:
# 1. Scan array from last to first element so that when we arrive at a certain
# index his next greater element will be already in stack and we can directly
# get this element while at the same index.
#
# 2. After reaching a certain index we will pop the stack till we get the
# greater element on top from the current element and that element will be the
# answer for current element. If stack gets empty while doing the pop operation
# then the answer would be -1.
#
# Reference:
# https://www.geeksforgeeks.org/next-greater-element-in-same-order-as-input/
#
# Complexity:
# O(N) time and space

def print_next_greater_element(arr):
  stack = []
  nge = [-1 for _ in range(len(arr))]  # To store next greater element

  for i in range(len(arr) - 1, -1, -1):  # i = n - 1 to 0
    # Pop until we find greater element at stack top than current element which
    # would be NGE for current element as we are scanning array from last.
    while stack and stack[-1] < arr[i]:
      stack.pop()

    if stack:
      nge[i] = stack.pop()
    else:
      nge[i] = -1  # Not required as we have initialised nge with all -1s

    # Push current element to stack
    stack.append(arr[i])

  # Print element and its NGE in array
  print 'Elements and its NGE:'
  for i in range(len(arr)):
    print '%d -> %d' % (arr[i], nge[i])


print_next_greater_element([11, 13, 21, 3])
# 11 -> 13
# 13 -> 21
# 21 -> -1
# 3 -> -1

print_next_greater_element([11, 13, 14, 15, 20])
# 11 -> 13
# 13 -> 14
# 14 -> 15
# 15 -> 20
# 20 -> -1

print_next_greater_element([5, 4, 3, 2, 1])
# 5 -> -1
# 4 -> -1
# 3 -> -1
# 2 -> -1
# 1 -> -1
