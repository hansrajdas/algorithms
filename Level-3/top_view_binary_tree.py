#!/usr/bin/python

# Date: 2018-11-25
#
# Description:
# Print top view of a binary tree.
#
# Approach: 
# Combination of vertical level order and horizontal level order traversal is
# used.
# If there is only one node in particular vertical level order print that node
# otherwise if there are multiple nodes in particular vertical level order,
# print that node which comes first in horizontal level order.
#
# To simulate above logic we require both queue and hash-map, queue is used for
# horizontal level order and hash-map is used to store horizontal distance as
# key and node as value.
#
# Reference:
# https://www.youtube.com/watch?v=c3SAvcjWb1E
# https://www.geeksforgeeks.org/print-nodes-in-the-top-view-of-binary-tree-set-3/
#
# Complexity:
# O(N) time and space


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

def top_view(root):
  mp = {}
  hd = 0  # Horizontal distance
  q = collections.deque([(root, hd)])
  while q:
    node_tuple = q.popleft()
    node = node_tuple[0]
    hd = node_tuple[1]
    if hd not in mp:  # this is the first node in level order
        # print node_tuple[0].k,
        mp[hd] = node_tuple[0].k

    if node.left:
        q.append((node.left, hd - 1))

    if node.right:
        q.append((node.right, hd + 1))

  # Print in vertical distance wise
  for k in sorted(mp.keys()):
      print mp[k]

def main():
  bst = BST()
  items = [5, 10, 2, 3, 8, 12, 16]
  for i in items:
    bst.root = bst.insert(bst.root, i)

  print 'Inorder traversal...'
  bst.inorder(bst.root)

  print '\nTop view of binary tree...'
  top_view(bst.root)


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
# Top view of binary tree...
# 2
# 5
# 10
# 12
# 16
