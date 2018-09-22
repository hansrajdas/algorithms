#!/usr/bin/python

# Date: 2018-09-22
#
# Description:
# Given a matrix, print that in clockwise spiral form.
#
# Approach:
# Use 4 loops to print matrix elements in all 4 directions. Keep incrementing
# start index and decrement end index when one cycle completes.
# When only one row and column needs to be traversed, check that case - should
# be traversed only once.
#
# Complexity:
# O(M*N) M = Rows, N = Columns


def print_matrix_in_spiral(mat):
  row_end = len(mat) - 1
  col_end = len(mat[0]) - 1
  row_start = 0
  col_start = 0
  
  while row_start <= row_end and col_start <= col_end:
    # Left to right
    for c in range(col_start, col_end + 1):
      # print 'left to right'
      print mat[row_start][c]
      
    # Top to down
    for r in range(row_start + 1, row_end + 1):
      # print 'top to down'
      print mat[r][col_end]
      
    # Right to left
    # If there is only row left, that is already covered by left to right
    # traversal
    if row_start < row_end:
      for c in range(col_end - 1, col_start - 1, -1):
        print mat[row_end][c]
      
    # Down to top
    # If there is only one column left, that is already covered by top to down
    # traversal
    if col_start < col_end:
      for r in range(row_end - 1, row_start, -1):
        # print 'down to top'
        print mat[r][col_start]
      
    row_start += 1
    row_end -= 1
    col_start += 1
    col_end -= 1


def main():
  matrix = [
    [1, 2, 3, 13, 23],
    [4, 5, 6, 16, 26],
    [7, 8, 9, 19, 29],
  ]
  print_matrix_in_spiral(matrix)


if __name__ == '__main__':
  main()

# Output:
# --------------
# 1
# 2
# 3
# 13
# 23
# 26
# 29
# 19
# 9
# 8
# 7
# 4
# 5
# 6
# 16
