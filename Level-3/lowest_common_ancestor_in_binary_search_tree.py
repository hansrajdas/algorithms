#!/usr/bin/python

# Date: 2018-09-21
#
# Description:
# Find lowest common ancestor of given 2 nodes in binary search tree.
#
# Assumption:
# Both nodes given n1 and n2 must be present in binary search tree.
#
# Approach:
# If both n1 and n2 are smaller than current root, search in left sub tree and
# if both are greater than current root, search in right sub tree otherwise(
# n1 < current-root.key < n2 or n1 > current-root.key > n2) current root must
# be LCA of given nodes as this is a binary tree.
#
# Complexity:
# O(logn) Time


class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self):
    self.root = None

  def find_lca_util(self, root, n1, n2):
    if root is None:
      return None

    if root.key > n1 and root.key > n2:
      return self.find_lca_util(root.left, n1, n2)
    elif root.key < n1 and root.key < n2:
      return self.find_lca_util(root.right, n1, n2)

    return root

  def find_lca(self, n1, n2):
    return self.find_lca_util(self.root, n1, n2)

def main():
  tree = BinaryTree()
  tree.root = Node(10)
  tree.root.left = Node(5)
  tree.root.right = Node(20)

  tree.root.left.left = Node(3)
  tree.root.left.right = Node(7)

  lca = tree.find_lca(3, 7)
  if lca:
    print 'Found, key: %d, id: %d' % (lca.key, id(lca))
  else:
    print 'One of the 2 nodes not found in tree'


if __name__ == '__main__':
  main()


# Output:
# ----------------------------------
# Found, key: 5, id: 140026634771560
