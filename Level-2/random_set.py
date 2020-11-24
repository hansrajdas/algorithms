#!/usr/bin/python

# Date: 2020-11-24
#
# Description:
# Write a method to randomly generate a set of m integers from an array of size
# n. Each element must have equal probability of being chosen.
#
# Approach:
# - Copy first elements from original(A) list to resultant(B) list
# - Traverse remaining elements using index i and generate random number from
#   0 to i, if random number comes out to be less than m then replace element
#   at random index in B[rand] with A[i]
#
# There can several ways to do this
#
# Complexity:
# O(N)

import random

def generate_random_set(A, m):
    n = len(A)
    if m >= n:
        return None
    B = []
    for i in range(m):
        B.append(A[i])

    for i in range(m, n):
        rand = random.randint(0, i)
        if rand < m:
            B[rand] = A[i]
    return B

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    print(generate_random_set(A, 3))
    print(generate_random_set(A, 4))
    print(generate_random_set(A, 5))
