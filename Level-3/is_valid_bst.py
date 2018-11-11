#!/usr/bin/python

# Date: 2018-11-11
#
# Description:
# Check if a given BST is valid or not.
#
# Approach:
# We can't just compare 3 values root.data, left.data and right.data as it may
# be possible that tree's root is 10 and somewhere down in left sub tree there
# is node having data = 5, left.data = 3 and right.data = 20 which is not
# correct as 10 is the root of this tree and no node can have value more than 10
# in left subtree.
#
# So to handle this problem, we can start scanning tree from root to leaf and
# keep track of range of values possible in child nodes. For left subtree we can
# limit max range and for right we have min range. If any node falls beyond this
# range, BST is not valid.
#
# Reference:
# https://www.youtube.com/watch?v=MILxfAbIhrE
#
# Complexity:
# O(N)

import sys

class Node:
  """Initialises a new tree node."""
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BST:
  """Manages BST."""
  def __init__(self):
    """Initialises a new BST."""
    self.root = None

  def insert(self, root, data):
    if not root:
      return Node(data)
    elif data < root.data:
      root.left = self.insert(root.left, data)
    elif data > root.data:
      root.right = self.insert(root.right, data)
    else:
      print 'Duplicate node - %d' % data
    return root

  def inorder(self, root):
    if root:
      self.inorder(root.left)
      print root.data
      self.inorder(root.right)

  def is_valid_bst(self, root, _min, _max):
    """Checks if this BST is valid."""
    if not root:
      return True
    if root.data < _min or root.data > _max:
      return False
    return (self.is_valid_bst(root.left, _min, root.data) and
            self.is_valid_bst(root.right, root.data, _max))


def main():
  # Valid BST
  valid = BST()
  valid.root = valid.insert(valid.root, 10)
  valid.root = valid.insert(valid.root, 5)
  valid.root = valid.insert(valid.root, 20)
  valid.root = valid.insert(valid.root, 4)
  valid.root = valid.insert(valid.root, 7)
  valid.root = valid.insert(valid.root, 15)
  valid.root = valid.insert(valid.root, 25)
  valid.root = valid.insert(valid.root, 30)

  valid.inorder(valid.root)
  print valid.is_valid_bst(valid.root, -sys.maxint, sys.maxint)  # True

  # Invalid BST
  invalid = BST()
  invalid.root = Node(10)
  invalid.root.left = Node(5)
  invalid.root.right = Node(20)
  invalid.root.left.left = Node(3)
  # This value is not correct, all nodes in left sub tree should be less than
  # root - 10
  invalid.root.left.right = Node(12)

  print valid.is_valid_bst(invalid.root, -sys.maxint, sys.maxint)  # False


if __name__ == '__main__':
  main()
