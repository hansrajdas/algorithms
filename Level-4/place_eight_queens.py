#!/usr/bin/python

# Date: 2018-08-07
#
# Description:
# Write an algorithm to print all ways of arranging eight queens on an 8x8 chess
# board so that none of them share the same row, column or diagonal. In this
# case diagonal means all diagonals, not just the two that bisect the board.
#
# Approach:
# Recursively checked all valid positions row wise. Like initially queen is
# placed at 8th row and checked on which column it can be placed from 1 to 8,
# once a valid column is found it moved to next row (7th row) and again checks
# on which column we can place queen with previous queen already placed at row 8
# some column. So when row count reaches 8, we are done with placing 8 queens on
# chessboard.
#
# Complexity:
# O(GRID_SIZE^3), GRID_SIZE = 8 for chessboard.

GRID_SIZE = 8

def checkValid(columns, row1, col1):
  """Checks whether can queen be placed at row1, col1.

  Some queens are already placed (on lesser indexed row, r < row1) on the board
  having positions in columns. It checks if a new queen is placed at row1, col1
  it is safe or not.

  Args:
    columns: List of size 8 having positions of queens already placed.
      Indexes of list represent row and value represent column.
      Like columns[r] = c represents row r and column c.
    row1: Current row where queen is attempted to be placed, if valid.
    col1: Current column where queen is attempted to be placed, if valid.
  """
  # Queens are placed in rows 0 to row1 - 1 so ran ran this loop from 0 to
  # row1 - 1.
  for row2 in range(row1):
    col2 = columns[row2]
    if col1 == col2:
      return False

    # Check if intersecting at diagonals. In difference in row and column is
    # same both boxes are diagonal to each other.
    columnDifference = abs(col1 - col2)
    rowDifference = row1 - row2  # As row2 < row1 so abs not required.
    if rowDifference == columnDifference:
      return False
  return True

def placeQueens(row, columns, results):
  """Updated results list to have all valid 8 queen positions on the board.

  Such that none attach each other.

  Args:
    row: Current row where queen will be placed.
    columns: List having 8 column positions of queen, index represents row.
    results: List of list having all valid 8 queen placement on the board.
  """
  if row == GRID_SIZE:  # Found valid placement for 8 queens.
    results.append(columns[:])  # Make deep copy and append to results.
  else:
    for col in range(GRID_SIZE):
      if checkValid(columns, row, col):
        columns[row] = col  # Valid position, place queen at this row, col.
        placeQueens(row + 1, columns, results)

def printQueenPositions(columns):
  print ('*****************************')
  for idx in range(len(columns)):
    print ('row={row}, col={col}'.format(row=idx, col=columns[idx]))

def main():
  results = []
  # Indicates coordinates where queens are placed.
  # Index represents row and value represents column.
  # So columns[row] = col, indicates queen is placed at (row, col) coordinate.
  columns = [0 for i in range(GRID_SIZE)]

  placeQueens(0, columns, results)

  for positions in results:
    printQueenPositions(positions)
  print ('Total number of solutions: {count}'.format(count=len(results)))


if __name__ == '__main__':
  main()

# Output:
# ...
# ...
# Total number of solutions: 92
