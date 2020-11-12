#!/usr/bin/python

# Date: 2020-11-12
#
# Description:
# Swap 2 numbers in place(without using extra variable)
#
# Approach:
# Use XOR binary operation to cancel out one number by XORing it twice.
#
# Complexity:
# O(1)


def swap_numbers(a, b):
    """Swaps two numbers without using temp variable."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a, b)

assert swap_numbers(1, 2) == (2, 1)
assert swap_numbers(100, 200) == (200, 100)
assert swap_numbers(-1, -2) == (-2, -1)
assert swap_numbers(0, 2) == (2, 0)
