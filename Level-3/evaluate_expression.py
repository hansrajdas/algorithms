#!/usr/bin/python

# Date: 2020-11-22
#
# Description:
# Given an arithmetic equation consisting of positive integers, +, -, * and /
# (no parentheses), compute the result.
#
# EXAMPLE
# Input: 2*3+5/6*3+15
# Output: 23.5
#
# Approach:
# Use 2 stacks - one for numbers and other for operators. In arithematic * and
# / has more priority over + and - so whenever we see * or / at top of stack
# and + or - comes in, we will evaluate stack tops and push result back to
# number stack
#
# Complexity:
# O(N) time and space

import enum

class Operator(enum.Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    BLANK = ' '

def compute(sequence):
    number_stack = []
    operator_stack = []
    i = 0
    while i < len(sequence):
        n = get_next_number(sequence, i)
        number_stack.append(n)
        i += len(n)
        if i >= len(sequence):
            break

        n = get_next_number(sequence, i)
        op = get_next_operator(sequence, i)
        collapse_top(number_stack, operator_stack, op)
        operator_stack.append(op)
        i += 1
    collapse_top(number_stack, operator_stack, Operator.BLANK)
    return number_stack.pop()

def get_next_number(sequence, i):
    j = i
    num = []
    while j < len(sequence) and sequence[j].isdigit():
        num.append(sequence[j])
        j += 1
    return ''.join(num)

def get_next_operator(sequence, i):
    if i < len(sequence):
        return sequence[i]
    return Operator.BLANK

def collapse_top(number_stack, operator_stack, op):
    while len(operator_stack) > 0 and len(number_stack) > 1:
        if priority(operator_stack[-1]) >= priority(op):
            right = float(number_stack.pop())
            left = float(number_stack.pop())
            res = apply_op(left, right, operator_stack.pop())
            number_stack.append(res)
        else:
            break

def apply_op(left, right, op):
    if op == Operator.SUBTRACT.value:
        return left - right
    if op == Operator.ADD.value:
        return left + right
    if op == Operator.MULTIPLY.value:
        return left * right
    return left / right

def priority(op):
    if op == Operator.MULTIPLY.value or op == Operator.DIVIDE.value:
        return 2
    if op == Operator.ADD.value or op == Operator.SUBTRACT.value:
        return 1
    return 0

assert compute('2*3+5/6*3+15') == 23.5
assert compute('2-6-7*8/2+5') == -27
# assert compute('2 - 6 - 7 * 8 / 2 + 5') == -27  # Spaces not handled
