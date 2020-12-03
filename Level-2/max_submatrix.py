#!/usr/bin/python

# Date: 2020-12-03
#
# Description:
# Given an NxN matrix of positive and negative integers, write ode to find the
# submatrix with the largest possible sum.
#
# Approach:
# Brute force approach, consider all possible submatrices. This will require
# 4 nested loops resulting in N^4 complexity and another N^2 to find sum of
# elements in that submtrix.
#
# Complexity:
# O(N^6)

class SubMatrix:
    def __init__(self, r1, c1, r2, c2, _sum):
        self.r1 = r1
        self.c1 = c1
        self.r2 = r2
        self.c2 = c2
        self.sum = _sum

def get_sum(M, r1, c1, r2, c2):
    _sum = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            _sum += M[r][c]
    return _sum

def get_max_submatrix(M):
    if not M:
        return None
    if not isinstance(M, list):
        return None
    if not isinstance(M[0], list):
        M = [M]
    s = None
    rows = len(M)
    cols = len(M[0])
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    temp_sum = get_sum(M, r1, c1, r2, c2)
                    if not s or s.sum < temp_sum:
                        s = SubMatrix(r1, c1, r2, c2, temp_sum)
    return s

def main():
    M = [
    ]
    R = get_max_submatrix(M)
    if R is not None:
        print(R.r1, R.c1, R.r2, R.c2, R.sum)

    M = [
        [1]
    ]
    R = get_max_submatrix(M)
    if R is not None:
        print('start: (%d, %d), end: (%d, %d), sum: %d' % (R.r1, R.c1, R.r2, R.c2, R.sum))

    M = [
        [-1, 2, 3],
        [-1, -2, -3],
        [-3, 2, -1]
    ]
    R = get_max_submatrix(M)
    if R is not None:
        print('start: (%d, %d), end: (%d, %d), sum: %d' % (R.r1, R.c1, R.r2, R.c2, R.sum))

if __name__ == '__main__':
    main()
