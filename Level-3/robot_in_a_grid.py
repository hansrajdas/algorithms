#!/usr/bin/python

# Date: 2018-07-28
#
# Description:
# Imagine a robot sitting on the upper left corner of grid with r rows and c
# columns. The robot can only move in 2 directions right and down, but certain
# are "off limits" such that robot cannot step on them. Design an algorithm to
# find a path for the robot from the top left to the bottom right.
#
# Approach:
# Backtracking technique is used. To find a path from the origin, we just work
# backwards. Starting from the last cell, we try to find a path to each of its
# adjacent cells and recurse till starting point.
#
# Complexity:
# O(rc) where r = rows, c = columns
# Without using cache it will be 2^(r+c)


def getPath(maze, row, col, path, cache):
  """Creates and returns path from 0, 0 to row - 1, col - 1 if possible.
  
  Args:
    maze: Matrix grid in which 1 represents positions where robot can go and 0
      represents "off limits" where robot can't go.
    row: Current row position.
    col: Current column position.
    path: List of tuples having positions of robot.
    cache: Dictionary to store status of already traversed cell.
  """
  # Base case: Reached a point where can't go back further or this position of
  # maze if "off limits".
  if row < 0 or col < 0 or not maze[row][col]:
    return False

  position = (row, col)
  # If already visited this cell.
  if position in cache:
    return cache[position]
  
  status = False
  reachedOrigin = not (row | col)  # At row = col = 0.
  # If there is a path from start to my current location, add my location.
  if (reachedOrigin or getPath(maze, row - 1, col, path, cache) or
      getPath(maze, row, col - 1, path, cache)):
    status = True
    path.append(position)  # Save path in case of success or reached 0, 0.

  cache[position] = status  # Save position and status in cache.
  return status

def robotInAGrid(maze):
  if not maze:
    return None
  row = len(maze) - 1
  col = len(maze[0]) - 1
  path = []
  cache = {}
  if getPath(maze, row, col, path, cache):
    return path
  return None

def main():
  maze_1 = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 1, 1],
  ]
  maze_2 = [
    [1, 0, 1],
    [0, 0, 1],
    [1, 1, 0],
    [0, 0, 1],
  ]
  maze_3 = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1],
  ]
  mazes = [maze_1, maze_2, maze_3]
  for maze in mazes:
    path = robotInAGrid(maze)
    if path:
      print('Path form top-left to bottom-right is:', '=>'.join(map(str, path)))
    else:
      print('Path from top-left to bottom-right does *NOT* exist')

if __name__ == '__main__':
  main()

# Output:
# Path form top-left to bottom-right is: (0, 0)=>(0, 1)=>(1, 1)=>(2, 1)=>(2, 2)
# Path from top-left to bottom-right does *NOT* exist
# Path form top-left to bottom-right is: (0, 0)=>(0, 1)=>(0, 2)=>(1, 2)=>(2, 2)=>(3, 2)
