#!/usr/bin/python

# Date: 2020-11-22
#
# Description:
# Write a function that adds two numbers. We should not use + or any other
# arithmetic operator.
#
# Approach:
# Use binary addition, take LSB of boths numbers and add, if resulted is set
# bit then set the respective bit position in result. Also, take care of carry
# bit in each addition.
#
# Alternative approach(add_numbers_alternative) is to add 2 numbers using XOR
# operation without considering carry bits, then in next step add all carry
# bits to the above result. Refer book for more explanation on this approach.
#
# Complexity:
# O(logN), N is the number of bits required to represent given numbers


def add_2_bits(x, y, c):
    if x and y:
        if c:
            return 1, 1
        else:
            return 0, 1
    elif x ^ y:
        if c:
            return 0, 1
        else:
            return 1, 0
    return c, 0

def add_numbers(a, b):
    s = 0
    bit_position = 0
    carry = 0
    while a or b:
        a_lsb = a & 1
        b_lsb = b & 1
        bit_sum, carry = add_2_bits(a_lsb, b_lsb, carry)
        if bit_sum:
            s |= 1 << bit_position
        bit_position += 1
        a >>= 1
        b >>= 1
    if carry:
        s |= 1 << bit_position
    return s

def add_numbers_alternative(a, b):
    if not b:
        return a
    _sum = a ^ b
    carry = (a & b) << 1
    return add_numbers_alternative(_sum, carry)


assert add_numbers(0, 1) == 1
assert add_numbers(1, 1) == 2
assert add_numbers(5, 10) == 15
assert add_numbers(1010, 225) == 1235

assert add_numbers_alternative(0, 1) == 1
assert add_numbers_alternative(1, 1) == 2
assert add_numbers_alternative(5, 10) == 15
assert add_numbers_alternative(1010, 225) == 1235
