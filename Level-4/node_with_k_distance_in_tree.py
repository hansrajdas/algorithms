#!/usr/bin/python

# Date: 2018-12-31
#
# Description:
# Given a binary tree, a target node in the binary tree, and an integer value k,
# print all the nodes that are at distance k from the given target node.
#
# Approach:
# Nodes with distance K from target node can be divided in 2 categories
# - Nodes below the target node, this can be found using a recursive function
#   and decrementing k, when k reaches 0 we have to print the node.
# - Next category of nodes will be those who are ancestors(not present in
#   subtree rooted with target node). For these nodes we must go through all
#   ancestors. For every ancestor, we find its distance from target node, let
#   the distance be d, now we go to other subtree(if target was found in left
#   subtree, then we go to right subtree and vice versa) of the ancestor and
#   find all nodes at k-d distance from the ancestor.
# 
# Reference:
# https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
#
# Complexity:
# O(N) Time

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def print_k_distance_nodes_below(root, k):
  """Prints all nodes which are k distance from root."""
  if root is None:
    return

  if not k:  # If k = 0, we have reached k(original) distance down, print data
    print root.data
    return

  print_k_distance_nodes_below(root.left, k - 1)
  print_k_distance_nodes_below(root.right, k - 1)

def print_k_distance_nodes(root, target, k):
  if root is None:
    return -1

  if root is target:
    print_k_distance_nodes_below(target, k)
    return 0

  dl = print_k_distance_nodes(root.left, target, k)
  # Check if target was found in left subtree
  if dl != -1:
    # dl is distance from root's left to target so adding 1 while comparing.
    if dl + 1 == k:
      print root.data
    else:
      # Go to right subtree and print all nodes which are k-dl-2 distance away.
      # Right child is 2 nodes away from left child.
      print_k_distance_nodes_below(root.right, k - dl - 2)
    return dl + 1

  dr = print_k_distance_nodes(root.right, target, k)
  # Check if target was found in right subtree
  if dr != -1:
    if dr + 1 == k:
      print root.data
    else:
      print_k_distance_nodes_below(root.left, k - dr - 2)
    return dr + 1

  return -1

def main():
  root = Node(20)
  root.left = Node(8)
  root.left.left = Node(4)
  root.left.right = Node(12)
  root.left.right.left = Node(10)
  root.left.right.right = Node(14)

  root.right = Node(22)

  print 'TC-1'
  print_k_distance_nodes(root, root.left, 2)  # 10 14 22

  print '\nTC-2'
  print_k_distance_nodes(root, root.left.right.right, 3)  # 4 20
 

if __name__ == '__main__':
  main()
