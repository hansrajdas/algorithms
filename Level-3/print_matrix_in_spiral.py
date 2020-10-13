#!/usr/bin/python

# Date: 2018-09-22
#
# Description:
# Given a matrix, print that in clockwise spiral form.
#
# Approach-1:
# Function name: print_matrix_in_spiral
# Use 4 loops to print matrix elements in all 4 directions. Keep incrementing
# start index and decrement end index when one cycle completes.
# When only one row and column needs to be traversed, check that case - should
# be traversed only once.
#
# Approach-2:
# Function name: print_matrix_in_spiral_simple
# Check on the number of elements processed keeping track of 4 boundaries - top,
# right, bottom, left
# This approach is simpler than above
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
      print(mat[row_start][c], end=' ')

    # Top to down
    for r in range(row_start + 1, row_end + 1):
      # print 'top to down'
      print(mat[r][col_end], end=' ')

    # Right to left
    # If there is only row left, that is already covered by left to right
    # traversal
    if row_start < row_end:
      for c in range(col_end - 1, col_start - 1, -1):
        print(mat[row_end][c], end=' ')

    # Down to top
    # If there is only one column left, that is already covered by top to down
    # traversal
    if col_start < col_end:
      for r in range(row_end - 1, row_start, -1):
        # print 'down to top'
        print(mat[r][col_start], end=' ')

    row_start += 1
    row_end -= 1
    col_start += 1
    col_end -= 1

# This approach is simpler than above, this checks of number of elements
# processed keeping track of 4 boundaries - top, right, bottom, left
def print_matrix_in_spiral_simple(M):
    res = []
    rows = len(M)
    cols = len(M[0])
    size = rows * cols
    top = 0
    left = 0
    right = cols - 1
    bottom = rows - 1

    while len(res) < size:
        # Left to right
        for i in range(left, right + 1):
            if len(res) < size:
                res.append(M[top][i])
        top += 1

        # Top to bottom
        for i in range(top, bottom + 1):
            if len(res) < size:
                res.append(M[i][right])
        right -= 1

        # Right to left
        for i in range(right, left - 1, -1):
            if len(res) < size:
                res.append(M[bottom][i])
        bottom -= 1

        # Bottom to top
        for i in range(bottom, top - 1, -1):
            if len(res) < size:
                res.append(M[i][left])
        left += 1
    return res


def main():
  matrix = [
    [1, 2, 3, 13, 23],
    [4, 5, 6, 16, 26],
    [7, 8, 9, 19, 29],
  ]
  print_matrix_in_spiral(matrix)
  print()

  spiral = print_matrix_in_spiral_simple(matrix)
  print(spiral)


if __name__ == '__main__':
  main()

# Output:
# ------
# 1 2 3 13 23 26 29 19 9 8 7 4 5 6 16
# [1, 2, 3, 13, 23, 26, 29, 19, 9, 8, 7, 4, 5, 6, 16]
