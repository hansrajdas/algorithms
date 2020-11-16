#!/usr/bin/python

# Date: 2020-11-16
#
# Description:
# Given an array of integers, write a method to find indices m and n such that
# if you sorted elements m through n, the entire array would be sorted.
# Minimize n - m(that is, find the smallest such sequence).
#
# EXAMPLE
# Input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# Output: (3, 9)
#
# Approach:
# 1. Scan from left and find index till left array is sorted
# 2. Scan from end and find index till right part is sorted
# 3. Find min element in remaining array(leaving left part sorted) - min
# 4. Find max element in remaining array(leaving right part sorted) - max
# 5. Check index in left sorted array elements more than min - start
# 6. Check index in right sorted array elements less than max - end
# 7. Return start, end
#
# Complexity:
# O(N)


def get_sorted_prefix_index(A):
    i = 0
    while i < len(A) - 1:
        if A[i] > A[i + 1]:
            return i
        i += 1
    return i

def get_sorted_postfix_index(A):
    i = len(A) - 1
    while i > 0:
        if A[i] < A[i - 1]:
            return i
        i -= 1
    return i

def get_sub_sort_indices(A):
    if not A:
        return None
    sorted_prefix = get_sorted_prefix_index(A)

    if sorted_prefix == len(A) - 1:  # Already sorted
        return None

    sorted_postfix = get_sorted_postfix_index(A)

    _min = min(A[sorted_prefix + 1:])
    _max = max(A[:sorted_postfix])

    i = 0
    while i < sorted_prefix:
        if A[i] > _min:
            start = i
            break
        i += 1

    i = len(A) - 1
    while i >= 0:
        if A[i] < _max:
            end = i
            break
        i -= 1
    return start, end

assert get_sub_sort_indices([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]) == (3, 9)
assert get_sub_sort_indices([1, 2, 4, 7, 10, 11]) == None
assert get_sub_sort_indices([1, 2, 4, 7, 10, 3]) == (2, 5)
