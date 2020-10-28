#!/usr/bin/python

# Date: 2018-08-05
#
# Description:
# Implement the "paint fill" function that one might see on many image editing
# programs. That is, given a screen (represented by a two-dimensional array of
# colors), a point and a new color, fill in the surrounding area (having same
# color) until the color changes from original color.
# In other words, screen is clicked at pixel where its BLUE and we have selected
# new color as RED then all the surrounding area having BLUE color should be
# changed with RED.
#
# Approach:
# Let clicked at pixel r, c and has color BLUE and we want to update with RED.
# Recursively checked the adjacent pixels up, down, left and right if it has
# BLUE then updated with RED otherwise left as it was.
#
# Can also be solved using breadth first search where each pixel would be a node
# and row - 1, row + 1, col - 1 and col + 1 will be edges.
#
# Complexity:
# O(2^r * 2^c), r and c are rows and columns of matrix.

import enum

class Colors(enum.Enum):
  GREEN = 'GREEN'
  BLACK = 'BLACK'
  BLUE = 'BLUE'
  RED = 'RED'

def paintFillWithNewColorDFS(screen, row, col, oldColor, newColor):
  """Updates the screen matrix with new colors in the surrounding area.
  
  Args:
    screen: Matrix having screen colors at each pixel.
    row: Clicked row index.
    col: Clicked column index.
    oldColor: Old color at pixel where clicked.
    newColor: New color.
  """
  if row < 0 or col < 0 or row >= len(screen) or col >= len(screen[0]):
    return False

  if screen[row][col] == oldColor:
    screen[row][col] = newColor
    paintFillWithNewColorDFS(screen, row - 1, col, oldColor, newColor)
    paintFillWithNewColorDFS(screen, row + 1, col, oldColor, newColor)
    paintFillWithNewColorDFS(screen, row, col - 1, oldColor, newColor)
    paintFillWithNewColorDFS(screen, row, col + 1, oldColor, newColor)
  return True

def paintFillWithNewColorBFS(screen, row, col, oldColor, newColor):
    Q = collections.deque()
    Q.append((row, col))
    while Q:
        row, col = Q.popleft()
        if row < 0 or col < 0 or row >= len(screen) or col >= len(screen[0]):
            continue
        if screen[row][col] == oldColor:
            screen[row][col] = newColor
            Q.append((row - 1, col))
            Q.append((row + 1, col))
            Q.append((row, col - 1))
            Q.append((row, col + 1))


def paintFill(screen, row, col, newColor):
  """Fills the surrounding area(having common color) with new color.
  
    If new color and existing color (where clicked row, col) are same, no update
    is required.

  Args:
    screen: Matrix having screen colors at each pixel.
    row: Clicked row index.
    col: Clicked column index.
    newColor: New color.
  """
  if screen[row][col] == newColor:
    return False
  paintFillWithNewColorDFS(screen, row, col, screen[row][col], newColor)
  # paintFillWithNewColorBFS(screen, row, col, screen[row][col], newColor)

def main():
  # 3x2 screen, filled with few colors
  screen = [
    [Colors.BLUE.value, Colors.BLUE.value],
    [Colors.BLUE.value, Colors.BLACK.value],
    [Colors.BLUE.value, Colors.BLACK.value],
  ]

  # Row and col index which is clicked, new color = RED.
  row = 0
  col = 0
  paintFill(screen, row, col, Colors.RED.value)
  
  print('********* Updated matrix **********')
  for rowIdx in range(len(screen)):
    print(screen[rowIdx])

if __name__ == '__main__':
  main()

# Output:
# ********* Updated matrix **********
# ['RED', 'RED']
# ['RED', 'BLACK']
# ['RED', 'BLACK']
