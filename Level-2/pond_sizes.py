#!/usr/bin/python

# Date: 2020-11-17
#
# Description:
# You have an integer matrix representing a plot of land, where the value at
# that location represent the height above sea level. A valiue of zero indicates
# water. A pond is a region of water connected vertically, horizontally or
# diagonally. The size of the pond is the total number of connected water cells.
# Write a method to compute the sizes of all ponds in the matrix.
#
# EXAMPLE
# Input:
# 0 2 1 0
# 0 1 0 1
# 1 1 0 1
# 0 1 0 1
#
# Output: 2, 4, 1
#
# Approach:
# Idea is to do BFS on the adjacent cells if water is found
# - Scan whole matrix checking which cell has water, if found add this to a
#   queue and do BFS in adjacent cells checking if other water is found
# - Keep on incrementing count if as we found more waters
# - To keep track of if same cell is not visited again, we can mark water with
#   with -1 and check while checking again
#
# Complexity:
# O(rows * cols)

import collections

adjacents = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
]

def is_valid_pond(M, r, c):
    return r >= 0 and c >= 0 and r < len(M) and c < len(M[0]) and M[r][c] == 0

def get_pond_sizes(M):
    rows = len(M)
    cols = len(M[0])

    res = []
    for r in range(rows):
        for c in range(cols):
            if M[r][c]:
                continue
            count = 1
            M[r][c] = -1
            row = r
            col = c
            Q = collections.deque([(row, col)])
            while Q:
                row, col = Q.popleft()
                for r_offset, c_offset in adjacents:
                    if is_valid_pond(M, row + r_offset, col + c_offset):
                        M[row + r_offset][col + c_offset] = -1
                        Q.append((row + r_offset, col + c_offset))
                        count += 1
            res.append(count)
    return res

def main():
    M = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
    ]
    print(get_pond_sizes(M))

if __name__ == '__main__':
    main()
