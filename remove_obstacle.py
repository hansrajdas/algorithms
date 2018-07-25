#!/usr/bin/python

# Date: 2018-07-25
#
# Description:
# You are in charge of preparing a recently purchased lot for one of amazon's
# new building. The lot is covered with trenches and has a single obstacle that
# needs to be taken down before the foundation can be prepared for the building.
# The demolition robot must remove the obstacle before progress can be made on
# the building.
# Write an algorithm to determine the minimum distance required for the
# demolition robot to remove the obstacle.
#
# Assumptions:
# 1. The lot is flat, except for trenches, and can be represented as a 2-D grid.
# 2. The demolition robot must start from top left corner of the lot, which is
#    always flat and can move one block up, down, right or left at a time.
# 3. The demolition robot cannot enter trenches and cannot leave the lot.
# 4. The flat areas are represented as 1, areas with trenches as 0 and
#    obstacle by 9.
#
# Output:
# Return an integer representing the minimum distance traversed to remove the
# obstacle else return -1.
#
# Approach:
# Sum of row_idx + column_idx where 9 is found will given minimum distance.
#
# Complexity:
# O(M*N)

def removeObstacle(numRows, numColumns, lot):
  if numRows < 1 or numColumns > 1000 or numColumns < 1:
    return -1
  for row in range(numRows):
    for col in range(numColumns):
      if lot[row][col] == 9:
        return row + col
  return -1

print '##### Edge cases ######'
print 'Output: ', removeObstacle(1, 1, [[9]])
print 'Output: ', removeObstacle(0, 0, [[]])

print '\n##### Input: 1 ######'
m = 3
n = 3
l = [
      [1, 0, 0],
      [1, 0, 0],
      [1, 9, 1]
    ]
print 'Output: ', removeObstacle(m, n, l)

print '\n##### Input: 2 ######'
m = 5
n = 4
l = [
      [1, 1, 1, 1],
      [0, 1, 1, 1],
      [0, 1, 0, 1],
      [1, 1, 9, 1],
      [0, 0, 1, 1]
    ]
print 'Output: ', removeObstacle(m, n, l)

# Output:
##### Edge cases ######
# Output:  0
# Output:  -1
# 
##### Input: 1 ######
# Output:  3

##### Input: 2 ######
# Output:  5
