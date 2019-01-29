#!/usr/bin/python

# Date: 2018-11-23
#
# Description:
# Knight in original chess game can reach to any cell from any other cell.
# Here we have slightly restricted the moves possible by knight, it can only
# move to 6 other neighboring boxes from current - UL, UR, R, LR, LL and L
# priority wise.
# You are given starting coordinates(i, j) of knight and end, task is the
# minimum number of moves required to move from starting position to end
# position with path. If path is not possible, print 'Impossible'
#
# For further details, please check detailed problem description here:
# https://www.hackerrank.com/challenges/red-knights-shortest-path/problem
#
# Approach:
# BFS can be used to find the shortest path from source to destination.
# - A NxN matrix is used to store number of moves from source to that position.
# - Coordinates of source is set to 0 and other positions with -1 to indicate
#   it's reachable with infinite moves and will be updated as we uncover that
#   cell.
# - Another NxN matrix is used to store the paths from source.
# - Queue is always used to simulate BFS so here also it used to store
#   coordinates and looped until it is non empty
#
# Complexity:
# O(N^2) Time
# O(N^2) Space

import collections

moves = [
    ('UL', -2, -1),
    ('UR', -2, 1),
    ('R', 0, 2),
    ('LR', 2, 1),
    ('LL', 2, -1),
    ('L', 0, -2),
]

def printShortestPath(n, i_start, j_start, i_end, j_end):
    distance = [[-1 for _ in range(n)] for _ in range(n)]  # All are non reachable
    paths = [[[] for _ in range(n)] for _ in range(n)]  # Store paths from source
    distance[i_start][j_start] = 0  # Starting position is reachable with 0 moves
    Q = collections.deque([(i_start, j_start)])
    while len(Q):
        i, j = Q.popleft()
        if i == i_end and j == j_end:
            print distance[i][j]
            print ' '.join(paths[i][j])
            return None
        for direction, delta_i, delta_j in moves:
            new_i = i + delta_i
            new_j = j + delta_j
            # If new position is within board limits and not traversed then
            # traverse new position.
            if 0 <= new_i < n and 0 <= new_j < n and distance[new_i][new_j] == -1:
                distance[new_i][new_j] = distance[i][j] + 1
                paths[new_i][new_j] = paths[i][j] + [direction]
                Q.append((new_i, new_j))
    print 'Impossible'


# Test
printShortestPath(7, 6, 6, 0, 1)  # 4 UL UL UL L
printShortestPath(6, 5, 1, 0, 5)  # Impossible
printShortestPath(7, 0, 3, 4, 3)  # 2 LR LL
