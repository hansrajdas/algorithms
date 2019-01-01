#!/usr/bin/python

# Date: 2019-01-01
#
# Description:
# Find diameter(or max width) of a tree. The diameter of a tree is the number of
# nodes on the longest path between two leaves in the tree.
#
# Approach:
# Diameter of a tree can be calculated by only using the height function,
# because the diameter of a tree is nothing but maximum value of (left_height + right_height + 1)
# for each node. So we need to calculate this value (left_height + right_height + 1)
# for each node and update the result.
#
# Reference:
# https://www.geeksforgeeks.org/diameter-of-a-binary-tree-in-on-a-new-method/
#
# Complexity:
# O(N) Time

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def height(root, diameter):
  """
  Updates diameter list of one element with diameter of tree. It does not
  returns diameter, it returns height of tree.
  """
  if root is None:
    return 0
  hLeft = height(root.left, diameter)
  hRight = height(root.right, diameter)
  diameter[0] = max(diameter[0], 1 + hLeft + hRight)
  return 1 + max(hLeft, hRight)

def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)

  root.left.left = Node(7)
  root.left.right = Node(6)

  root.right.left = Node(5)
  root.right.right = Node(4)
  diameter = [0]  # To make diameter mutable
  # Above tree is
  #       1
  #   2       3
  # 7    6 5      4
  h = height(root, diameter)
  print 'Diameter: %d' % diameter[0]  # Diameter: 5


if __name__ == '__main__':
  main()
