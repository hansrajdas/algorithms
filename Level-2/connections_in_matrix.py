#!/usr/bin/python

# Date: 2018-09-26
#
# Description:
# Given a MxN matrix having values 0 or 1. 1 indicates the matrix position
# available for establishing the connection and 0 indicates the matrix position
# NOT available for establishing the connection.
#
# We need to connect the available adjacent positions vertically, horizontally
# and diagonally and count the number of distinct connections established.
#
# Approach:
# Scan matrix from 0, 0 to last row, last col and check if current cell is 1.
# If current cell is one check for right, below, both lower diagonals.
# Increment count if these are also one. Checking this way would ensure that
# connection is counted only once for a set of 1s.
#
# Complexity:
# O(m*n)

def get_connections(m, n, matrix):
  count = 0
  for row in range(0, m):
    for col in range(0, n):
      if matrix[row][col]:
        if col < n - 1 and matrix[row][col + 1]:
          count += 1
        if row < m - 1 and matrix[row + 1][col]:
          count += 1
        if row < m - 1 and col < n - 1 and matrix[row + 1][col + 1]:
          count += 1
        if row < m - 1 and col > 0 and matrix[row + 1][col - 1]:
          count += 1
  return count


def main():
  matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 0, 1],
  ]
  print 'Connections: %d' % get_connections(3, 4, matrix)  # 8

  matrix = [[1, 1, 1]]
  print 'Connections: %d' % get_connections(1, 3, matrix)  # 2

  matrix = [
    [1],
    [0],
    [1],
  ]
  print 'Connections: %d' % get_connections(3, 1, matrix)  # 0

  matrix = [[1]]
  print 'Connections: %d' % get_connections(1, 1, matrix)  # 0

  matrix = [
    [1, 1],
    [0, 1],
  ]
  print 'Connections: %d' % get_connections(2, 2, matrix)  # 3


if __name__ == '__main__':
  main()
