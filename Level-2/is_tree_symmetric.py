#!/usr/bin/python

# Date: 2018-11-11
#
# Description:
# Check if a tree is symmetric/self mirror image or not.
#
# Approach:
# - Scan tree from root to leaf and recursively compare data at left sub tree
#   with right sub tree
# - If one side is None other should also be None
#
# Complexity:
# O(N)

class Node:
  """Initialises a new tree node."""
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def is_tree_symmetric_utils(self, left, right):
    if (not left) or (not right):
      # If one part is None other should also be None for symmetric tree
      return left == right

    if left and right and left.data == right.data:
      return (self.is_tree_symmetric_utils(left.left, right.right) and 
              self.is_tree_symmetric_utils(left.right, right.left))

    return False

  def is_tree_symmetric(self):
    """Checks if this tree is mirror image/symmetric or not."""
    if not self.root:
      return True
    return self.is_tree_symmetric_utils(self.root.left, self.root.right)

def main():
  ## Case 1
  t = Tree()
  t.root = Node(10)
  t.root.left = Node(5)
  t.root.right = Node(5)
  t.root.left.left = Node(1)
  t.root.right.right = Node(1)
  t.root.left.right = Node(2)
  t.root.right.left = Node(2)

  print t.is_tree_symmetric()  # True

  ## Case 2
  t = Tree()
  t.root = Node(10)
  t.root.left = Node(5)
  t.root.right = Node(5)
  t.root.left.left = Node(1)
  t.root.right.right = Node(1)
  t.root.left.right = Node(2)

  print t.is_tree_symmetric()  # False

if __name__ == '__main__':
  main()
