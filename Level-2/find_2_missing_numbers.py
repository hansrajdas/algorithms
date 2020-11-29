#!/usr/bin/python

# Date: 2020-11-29
#
# Description:
# Given an array with all numbers from 1 to N appearing exactly once, except
# for two numbers which are missing. Find missing numbers.
#
# Approach:
# - Find sum of array and subtract this from actual sum of numbers from 1 to n,
#   this will us sum of missing numbers, that is: x + y = s
# - Then we can perform step one again but now with sum of squares of each
#   number, this gives us x^2 + y^2 = t
# - Now, we can solve these equation and get x and y. This will become a
#   quadratic equation below:
#   >>> y = s - x
#   >>> x^2 + (s - x)^2 = t
#   >>> 2x^2 - 2sx + s^2 - t = 0
#
# So using, x = [-b +- sqrt(b^2 - 4ac)] / 2a
# where, in this case:
# a = 2
# b = -2s
# c = s^2 - t
#
# Complexity:
# O(N)

import math

def solve_quadratic_equation(r1, r2):
    """
    ax^2 + bx + c = 0
    x = [-b +- sqrt(b^2 - 4ac)] / 2a

    In this case, we has to b +  not b - as - will give negative result.
    """
    # Referring 2x^2 - 2sx + s^2 - t = 0
    a = 2
    b = -2 * r1
    c = r1 * r1 - r2

    part1 = -b
    part2 = math.sqrt(b * b - 4 * a * c)
    part3 = 2 * a

    num1 = int((part1 + part2) // part3)
    return num1, r1 - num1

def get_missing_numbers(A):
    N = len(A) + 2  # Number ranges from 1 to N
    array_sum = sum(A)
    seq_sum = N * (N + 1) // 2
    missing_nums_sum = seq_sum - array_sum  # This is x + y

    # Sum of squares of array numbers
    array_sum_of_squares = 0
    for n in A:
        array_sum_of_squares += n * n

    # Sum of squares from 1 to N
    seq_sum_of_squares = 0
    i = 1
    while i <= N:
        seq_sum_of_squares += i * i
        i += 1
    missing_nums_square_sum =  seq_sum_of_squares - array_sum_of_squares

    return solve_quadratic_equation(missing_nums_sum, missing_nums_square_sum)

assert get_missing_numbers([2, 1, 5]) == (4, 3)
assert get_missing_numbers([1, 2, 3, 4, 5, 6, 7, 8]) == (10, 9)
