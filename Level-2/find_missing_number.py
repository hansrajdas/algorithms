#!/usr/bin/python

# Date: 2020-11-29
#
# Description:
# Given an array with all the numbers from 1 to N appearing exactly once, except
# for one number that is missing. Find the missing number.
#
# Approach:
# - Take sum of all numbers in array
# - Subtract above sum from n*(n + 1) // 2
# - Above approach works but in some programming language, we might face
#   overflow issue with sum taken so we can use alternative approach using XOR
#
# Alternative approach - takes XOR of all numbers in array and then further
# XORs with all numbers from 1 to N to nullify all non missing number.
#
# Complexity:
# O(N)

def find_missing_number(A):
    N = len(A) + 1  # Range of numbers is from 1 to N
    array_sum = sum(A)
    expected_sum = N * (N + 1) // 2
    return expected_sum - array_sum

def find_missing_number_using_xor(A):
    """
    Alternative approach - takes XOR of all numbers in array and then further
    XORs with all numbers from 1 to N to nullify all non missing number.
    """
    N = len(A) + 1  # Range of numbers is from 1 to N
    missing_number = 0
    for n in A:
        missing_number ^= n

    i = 1
    while i <= N:
        missing_number ^= i
        i += 1
    return missing_number

assert find_missing_number([3, 1, 2, 4]) == 5
assert find_missing_number([1]) == 2
assert find_missing_number([1, 2, 3, 4, 5, 6]) == 7

assert find_missing_number_using_xor([3, 1, 2, 4]) == 5
assert find_missing_number_using_xor([1]) == 2
assert find_missing_number_using_xor([1, 2, 3, 4, 5, 6]) == 7
