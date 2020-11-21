#!/usr/bin/python

# Date: 2020-11-21
#
# Description:
# Find all pairs of integers within an array which sum to a specific value.
#
# Approach:
# Use hash map to store and check if complement of a number n(target - n) is
# present in array or not.
#
# Complexity:
# O(N) time and space

def pairs_with_sum_single_iteration(A, target):
    """Prints duplicates also like for [2, 2, 2] will print [2, 2] twice. """
    print(A, target, end=' => ')
    m = {}
    for n in A:
        check = target - n
        if check in m and m[check] > 0:
            print(n, check, end=', ')
        else:
            m[n] = m.get(n, 0) + 1
    print()

def pairs_with_sum(A, target):
    print(A, target, end=' => ')
    m = {}
    for n in A:
        if n not in m:
            m[n] = 0
        m[n] += 1

    for n in A:
        check = target - n
        m[n] -= 1
        if check in m and m[check] > 0:
            print(n, check, end=', ')
            m[check] -= 1
        else:
            m[n] += 1
    print()

pairs_with_sum_single_iteration([2, 2, 2], 4)
pairs_with_sum_single_iteration([2, 2, 2, 2], 4)
pairs_with_sum_single_iteration([2, 2, 2, 2], 3)
pairs_with_sum_single_iteration([2, 3, 1, 5, 6, 3, 4], 6)
pairs_with_sum_single_iteration([-3, -2, -4, -1], -4)
