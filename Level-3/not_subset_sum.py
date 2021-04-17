#!/usr/bin/python

# Date: 2020-04-17
#
# Description:
# Given a sorted array (sorted in non-decreasing order) of positive numbers,
# find the smallest positive integer value that cannot be represented as sum
# of elements of any subset of given set.
#
# Approach:
#
# Reference:
# https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/
#
# Complexity:
# O(N)


def findSmallest(arr):
    ans = 1
    for n in arr:
        if n > ans:
            return ans
        ans += n
    return ans

assert findSmallest([1, 3, 6, 10, 11, 15]) == 2
assert findSmallest([1, 1, 1, 1]) == 5
assert findSmallest([1, 1, 3, 4]) == 10
assert findSmallest([1, 2, 5, 10, 20, 40]) == 4
assert findSmallest([1, 2, 3, 4, 5, 6]) == 22
