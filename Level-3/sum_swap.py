#!/usr/bin/python

# Date: 2020-11-20
#
# Description:
# Given two arrays of integers, find a pair of values(one value from each array)
# that you can swap to give the two arrays the same sum.
#
# EXAMPLE
# Input: [4, 1, 2, 1, 1, 2] and [3, 6, 3, 3]
# Output: {1, 3} or {4, 6}
#
# Approach:
# We can use mathematical to know what it takes to have 2 arrays same sum.
# Let's say we move a from array A to B and b from B to A, then to have sum:
# sum_A - a + b = sum_B + a - b which solves to:
#
# a - b = (sum_A - sum_b) / 2, means we must pairs whose difference if half
# of the array's sum difference
#
# Complexity:
# O(len_A + len_B)


def sum_swap(A, B):
    sum_A = sum(A)
    sum_B = sum(B)

    diff = sum_A - sum_B

    if diff % 2:
        return 'Diff is odd, cannot have same sum'
    half_diff = diff // 2
    set_B = set(B)
    for n in A:
        if n - half_diff in set_B:
            return n, n - half_diff
    return 'No element can be swapped to make same sum'

def main():
    print(sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))
    print(sum_swap([3, 6, 3, 3], [3, 6, 3, 3]))

if __name__ == '__main__':
    main()
