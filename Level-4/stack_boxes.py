#!/usr/bin/python

# Date: 2018-08-09
#
# Description:
# You have a stack of n boxes, with heights h, width w and depths d. The boxes
# cannot be rotated and can only be stacked on top of one another if each box
# in the stack is strictly larger than the box above it in height, width and
# depth. Implement a method to compute the height of the tallest possible stack.
# The height of a stack is the sum of the heights of each box.
#
# Approach:
#
# Complexity:
# O(2^n)

import collections

Box = collections.namedtuple('Box', ['height', 'width', 'depth'])

def sortHeightWise(box):
  return box.height

def canBeAbove(lower, above):
  """Can box 'above' be stored above 'lower'."""
  if (lower.height > above.height and lower.width > above.width and
    lower.depth > above.depth):
    return True
  return False
  
def stackMaxHeight(boxes, bottom, offset, stackMap):
  """Creates stack of boxes having max height.

  Recursively checks each possibility i.e max height can be achieved by using
  current box or without using current box.

  Args:
    boxes: List of namedtuples with height, width and depth of boxes.
    bottom: Namedtuple, Current bottom box used.
    offset: Integer, Index which indicates how far have we traversed in boxes
      list.
    stackMap: Dictionary with keys from 0 to n - 1, n = number of boxes and
      value as max height achieved by using bottom box bas boxes[key].
      stackMap[i] represents the tallest stack with box i at the bottom.
  """
  if offset == len(boxes):  # Base case
    return 0

  newBottom = boxes[offset]
  heightWithBottom = 0
  if bottom is None or canBeAbove(bottom, newBottom):
    if not stackMap[offset]:
      stackMap[offset] = stackMaxHeight(boxes, newBottom, offset + 1, stackMap)
      stackMap[offset] += newBottom.height
    heightWithBottom = stackMap[offset]

  # Check height without current box (at index offset of boxes i.e newBottom)
  heightWithoutBottom = stackMaxHeight(boxes, bottom, offset + 1, stackMap)

  return max(heightWithBottom, heightWithoutBottom)

def createStack(boxes):
  """Creates stack of boxes having max height.
  
  Args:
    boxes: List of namedtuples with height, width and depth of boxes.
  """
  boxes.sort(reverse=True, key=sortHeightWise)
  stackMap = {i: 0 for i in range(len(boxes))}
  return stackMaxHeight(boxes, None, 0, stackMap)

def main():
  boxes = []
  n = input('Enter number of boxes: ')
  for i in xrange (n):
    print '\n'
    h = input('Enter height of box[%d]:' % i)
    w = input('Enter width of box[%d]:' % i)
    d = input('Enter depth of box[%d]:' % i)
    boxes.append(Box(h, w, d))

  print '\nMax height achieved: {height}'.format(height=createStack(boxes))

if __name__ == '__main__':
  main()
