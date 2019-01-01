#!/usr/bin/python

# Date: 2019-01-01
#
# Description:
# Given a Binary Tree and a positive integer k, print all nodes that are
# distance k from a leaf node.
#
# Approach:
# The idea is to traverse the tree. Keep storing all ancestors till we hit a
# leaf node. When we reach a leaf node, we print the ancestor at distance k. We
# also need to keep track of nodes that are already printed as output. For that
# we use a boolean array visited[].
#
# Reference:
# https://www.geeksforgeeks.org/print-nodes-distance-k-leaf-node/
#
# Complexity:
# O(N) Time and space


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def height(root):
  if root is None:
    return 0
  return 1 + max(height(root.left), height(root.right))


def nodes_with_k_distance_from_leaf_utils(root, k, path, visited, path_len):
  if root is None:
    return None

  path[path_len] = root.data
  path_len += 1

  # Print data only if:
  # 1. It is a leaf node
  # 2. path_len for this iteration is more than k, suppose if k is more than
  # height of tree, nothing should be printed
  # 3. Node is not already visited
  if (root.left is None and root.right is None and
      path_len - k - 1 >= 0 and
      not visited[path_len - k - 1]):
    print path[path_len - k - 1],
    visited[path_len - k - 1] = True

  nodes_with_k_distance_from_leaf_utils(root.left, k, path, visited, path_len)
  nodes_with_k_distance_from_leaf_utils(root.right, k, path, visited, path_len)


def nodes_with_k_distance_from_leaf(root, k):
  h = height(root)
  path = {i: None for i in range(h)}
  visited = {i: False for i in range(h)}
  nodes_with_k_distance_from_leaf_utils(root, k, path, visited, 0)


def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)

  root.left.left = Node(4)
  root.left.right = Node(5)

  root.right.left = Node(6)
  root.right.right = Node(7)

  root.right.left.right = Node(8)

  nodes_with_k_distance_from_leaf(root, 2)  # 1 3


if __name__ == '__main__':
  main()
