#!/usr/bin/python

# Date: 2020-12-05
#
# Description:
# Given 2 arrays, one shorter (with all distinct elements) and one longer. Find
# the shortest subaraay in the longer array that contains all the elements in
# the shorter array. The items can appear in any order.
#
# EXAMPLE
# Input: [1, 5, 9] and [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
# Output: [7, 10]
#
# Approach:
# This is brute force approach, tried to check all subarrays of bigger array
# and saved which is shortest and having all elements of smaller array.
# We need to convert to set of all smaller array elements in each iteration of
# bigger subarray.
#
# Complexity:
# O(SB^2)
#
# NOTE: CTCI has optimised solution, refer the min heap based solution


def shortest_superseq(bigger, smaller):
    start = 0
    end = len(bigger) - 1
    smaller_set = set(smaller)
    for i in range(len(bigger)):
        smaller_set = set(smaller)
        if bigger[i] not in smaller_set:
            continue
        smaller_set.remove(bigger[i])
        for j in range(i + 1, len(bigger)):
            if bigger[j] in smaller_set:
                smaller_set.remove(bigger[j])
            if not smaller_set:
                if end - start > j - i:
                    start = i
                    end = j
                break
    return [start, end]
            
            


bigger = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
smaller = [1, 5, 9]
assert shortest_superseq(bigger, smaller) == [7, 10]
