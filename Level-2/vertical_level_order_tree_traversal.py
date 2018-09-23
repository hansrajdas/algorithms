#!/usr/bin/python

# Date: 2018-
#
# Description:
# WAP to print binary tree in vertical level order. If graph is:
#              5
#             / \
#            4   6
#
# It should print 4, 5, 6
#
# Approach: 
# Do any tree traversal and populate a hashmap having key as distance from root
# and value as list of values which are that distance apart from root.
# For left side -1 is used, for right +1 used.
#
# Other approaches:
# 1. Does without space, but has worse complexity
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
#
# 2. Uses BFS queuing approach
# https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/
#
# Complexity:
# O(N) time and space, N is number of nodes in tree. In this complexity
# analysis dictionary is considered to have O(1) complexity for all operations.


import collections


class Node:
  def __init__(self, k):
    self.k = k
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def insert(self, root, k):
    if root is None:
      return Node(k)

    if root.k > k:
      root.left = self.insert(root.left, k)
    elif root.k < k:
      root.right = self.insert(root.right, k)
    else:
      print 'Duplicates not allowed in BST'
      return root

    return root

  def inorder(self, root):
    if root:
      self.inorder(root.left)
      print root.k
      self.inorder(root.right)

  def vertical_level_order_util(self, root, level_map, level):
    if root is None:
      return None
    self.vertical_level_order_util(root.left, level_map, level - 1)
    self.vertical_level_order_util(root.right, level_map, level + 1)
    level_map[level].append(root.k)

  def vertical_level_order(self):
    """Prints tree elements on basis of vertical order."""
    level_order = collections.defaultdict(list)
    self.vertical_level_order_util(self.root, level_order, 0)

    for k in sorted(level_order.keys()):
      print 'Level: %d, Values: %s' % (k, level_order[k])


def main():
  bst = BST()
  items = [5, 10, 2, 3, 8, 12, 16]
  for i in items:
    bst.root = bst.insert(bst.root, i)

  print 'Inorder traversal...'
  bst.inorder(bst.root)

  print '\nVertical level order traversal...'
  bst.vertical_level_order()


if __name__ == '__main__':
  main()


# Output:
# -----------
# Inorder traversal...
# 2
# 3
# 5
# 8
# 10
# 12
# 16
# 
# Vertical level order traversal...
# Level: -1, Values: [2]
# Level: 0, Values: [3, 8, 5]
# Level: 1, Values: [10]
# Level: 2, Values: [12]
# Level: 3, Values: [16]
