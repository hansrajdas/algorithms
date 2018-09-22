#!/usr/bin/python

# Date: 2018-09-22
#
# Description:
# Given a number N, form a matrix having numbers from 1 to N*N in spiral form.
# N = 3
# 123
# 894
# 765
#
# N = 4
# 01 02 03 04
# 12 13 14 05
# 11 16 15 06
# 10 09 08 07
#
# Approach:
# We know that sequence of direction will be:
# 1. Left to right: row constant, col increasing
# 2. Top to down: row decreasing, col constant
# 3. Right to left: row constant, col decreasing
# 4. Down to top: row decreasing, col constant
#
# So using above fact we can take 2 list indicating row/col directions and
# compute new row, col. If row/col is not valid, we can use next direction.
#
# Complexity:
# O(N^2)


def is_invalid(m, r, c, n):
  """Checks if new row, col selected if valid or not.
  
  Either row or col is out of bound or again landing on used cell.
  """
  return r < 0 or c < 0 or r >= n or c >= n or m[r][c] != 0

def create_spiral_matrix(n):
  """Creates a matrix having values from 1 to n^2 in spiral direction."""
  matrix = []
  row = 0
  col = 0
  # Row direction sequence:
  # 0 means row will be constant when going from left to right
  # 1 means row will be increasing when going from top to down
  # -1 means row will be decreasing - when moving from down to up
  dr = [0, 1, 0, -1]
  dc = [1, 0, -1, 0]  # Column direction sequence
  val = 0
  direction = 0  # 0 to 3, indicating 4 directions
  
  # Create empty matrix
  for r in range(n):
    matrix.append([0] * n)
    
  while val < n * n:
    val += 1
    matrix[row][col] = val
    row += dr[direction]
    col += dc[direction]
    
    # If new row, col is invalid(out of bound or already used), revert previous
    # row, col and change direction.
    if is_invalid(matrix, row, col, n):
      row -= dr[direction]
      col -= dc[direction]
      direction = (direction + 1) % 4
      row += dr[direction]
      col += dc[direction]
      
  return matrix
    

def main():
  n = input('Enter N: ')
  matrix = create_spiral_matrix(n)
  for row in matrix:
    print row


if __name__ == '__main__':
  main()


# Output:
# ----------------
# Enter N: 2
# [1, 2]
# [4, 3]

# Enter N: 3
# [1, 2, 3]
# [8, 9, 4]
# [7, 6, 5]

# Enter N: 7
# [1, 2, 3, 4, 5, 6, 7]
# [24, 25, 26, 27, 28, 29, 8]
# [23, 40, 41, 42, 43, 30, 9]
# [22, 39, 48, 49, 44, 31, 10]
# [21, 38, 47, 46, 45, 32, 11]
# [20, 37, 36, 35, 34, 33, 12]
# [19, 18, 17, 16, 15, 14, 13]

# Enter N: 5
# [1, 2, 3, 4, 5]
# [16, 17, 18, 19, 6]
# [15, 24, 25, 20, 7]
# [14, 23, 22, 21, 8]
# [13, 12, 11, 10, 9]
