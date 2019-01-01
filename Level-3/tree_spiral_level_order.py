#!/usr/bin/python

# Date: 2019-01-01
#
# Description:
# Write a function to print spiral order traversal of a tree.
# Root -> Left to right -> Right to left and so on...
#
# Approach:
# Use 2 stacks, one for left to right and another for left to right. While
# poping elements from one stack add its children to another stack in reverse
# order.
#
# Reference:
# https://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/ - Method 2 (Iterative)
#
# Complexity:
# O(N) Time and space

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def print_spiral_order(root):
  """
  Prints tree elements in spiral order, first root, next level from left to
  right then next level from right to left and so on.
  """
  s1 = [root]
  s2 = []
  while s1 or s2:
    while s1:
      node = s1.pop()
      print node.data,
      if node.right:
        s2.append(node.right)
      if node.left:
        s2.append(node.left)

    while s2:
      node = s2.pop()
      print node.data,
      if node.left:
        s1.append(node.left)
      if node.right:
        s1.append(node.right)

def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)

  root.left.left = Node(7)
  root.left.right = Node(6)

  root.right.left = Node(5)
  root.right.right = Node(4)
  # Above tree is
  #       1
  #   2       3
  # 7    6 5      4
  print_spiral_order(root)  # 1 2 3 4 5 6 7


if __name__ == '__main__':
  main()
