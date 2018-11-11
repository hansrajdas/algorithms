#!/usr/bin/python

# Date: 2018-11-11
#
# Description:
# Find mirror image of a given binary tree.
#
# Approach:
# Scan tree from root to leaf recursively and while moving up swap left and
# right subtrees.
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

  def inorder(self, root):
    if root:
      self.inorder(root.left)
      print root.data,
      self.inorder(root.right)

  def find_mirror(self, root):
    """Converts a given tree to it's mirror image."""
    if not root:
      return None

    self.find_mirror(root.left)
    self.find_mirror(root.right)

    # Swap left and right sub trees while moving up from leaf to root
    root.left, root.right = root.right, root.left

def main():
  t = Tree()
  t.root = Node(1)
  t.root.left = Node(2)
  t.root.right = Node(3)
  t.root.left.left = Node(4)
  t.root.right.right = Node(5)
  t.root.left.right = Node(6)
  t.root.right.left = Node(7)

  print 'Inorder traversal of tree: '
  t.inorder(t.root)  # 4 2 6 1 7 3 5

  t.find_mirror(t.root)
  
  print '\nMirror image of above tree: '
  t.inorder(t.root)  # 5 3 7 1 6 2 4


if __name__ == '__main__':
  main()
