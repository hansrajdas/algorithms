#!/usr/bin/python

# Date: 2018-08-07
#
# Description:
# Write an algorithm to print all ways of arranging eight queens on an 8x8 chess
# board so that none of them share the same row, column or diagonal. In this
# case diagonal means all diagonals, not just the two that bisect the board.
#
# Approach:
#
# Complexity:
# O(8^3)

GRID_SIZE = 8

def checkValid(columns, row1, col1):
  for row2 in range(0, row1):  # Loop from 0 to row1
    col2 = columns[row2]
    if col1 == col2:
      return False

    # Check if intersecting at diagonals.
    columnDifference = abs(col1 - col2)
    rowDifference = row1 - row2
    if rowDifference == columnDifference:
      return False
  return True

def placeQueens(row, columns, results):
  if row == GRID_SIZE:  # Found valid placement for 8 queens.
    results.append(columns[:])  # Make deep copy and append to results.
  else:
    for col in range(GRID_SIZE):
      if checkValid(columns, row, col):
        columns[row] = col  # Valid position, place queen at this row, col.
        placeQueens(row + 1, columns, results)

def printQueenPositions(columns):
  print '*****************************'
  for idx in range(len(columns)):
    print 'row={row}, col={col}'.format(row=idx, col=columns[idx])

def main():
  results = []
  # Indicates coordinates where queens are placed.
  # Index represents row and value represents column.
  # So columns[row] = col, indicates queen is placed at (row, col) coordinate.
  columns = [0 for i in range(GRID_SIZE)]

  placeQueens(0, columns, results)

  for positions in results:
    printQueenPositions(positions)
  print 'Total number of solutions: {count}'.format(count=len(results))


if __name__ == '__main__':
  main()

# Output:
# ...
# ...
# Total number of solutions: 92
