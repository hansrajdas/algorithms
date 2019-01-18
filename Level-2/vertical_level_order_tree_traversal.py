#!/usr/bin/python

# Date: 2018-11-25
#
# Description:
# WAP to print binary tree in vertical level order. If tree is:
#              5
#             / \
#            4   6
#
# It should print 4, 5, 6
#
# Approach: 
# We can use horizontal level order traversal and keep track of horizontal
# distance in deque itself. Whenever we push a node to queue we do -1 if it has
# a left child and +1 if it has right child.
#
# Reference:
# https://www.geeksforgeeks.org/print-a-binary-tree-in-vertical-order-set-3-using-level-order-traversal/
#
# Other approaches:
# 1. Does without space, but has worse complexity of O(N^2)
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
#
# 2. Uses DFS approach, but order is not maintained.
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/
#
# Complexity:
# O(N) time and space, N is number of nodes in tree.

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

  def vertical_level_order(self):
    """Prints tree elements on basis of vertical order."""
    if not self.root:
      return None

    level_order = collections.defaultdict(list)
    hd = 0  # Horizontal distance from root
    Q = collections.deque([(self.root, hd)])
    while Q:
      tup = Q.popleft()
      current_node = tup[0]
      hd = tup[1]
      
      level_order[hd].append(current_node.k)
      if current_node.left:
        Q.append((current_node.left, hd - 1))

      if current_node.right:
        Q.append((current_node.right, hd + 1))

    # Print nodes in vertical order
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
# Level: 0, Values: [5, 3, 8]
# Level: 1, Values: [10]
# Level: 2, Values: [12]
# Level: 3, Values: [16]
