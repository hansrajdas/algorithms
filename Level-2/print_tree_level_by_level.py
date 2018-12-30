#!/usr/bin/python

# Date: 2018-12-30
#
# Description:
# Print tree elements level by level in separate lines.
#
# Approach:
# Use queue to perform horizontal level order traversal and while printing,
# check number of nodes present in queue and print all those nodes and add to
# queue all nodes just below that level.
#
# Reference:
# https://www.geeksforgeeks.org/print-level-order-traversal-line-line/
#
# Complexity:
# O(N)

import collections

class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

def insert(root, k):
    if not root:
        return Node(k)
    elif root.k > k:
        root.left = insert(root.left, k)
    elif root.k < k:
        root.right = insert(root.right, k)
    else:
        print 'Duplicate node: ', k
        return root
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print root.k,
        inorder(root.right)

def print_tree_level_by_level(root):
    Q = collections.deque()
    Q.append(root)
    while len(Q):
        count = len(Q)
        while count:
            node = Q.popleft()
            print node.k,
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
            count -= 1
        print ''


def main():
  bst = BST()

  # Level 1
  bst.root = insert(bst.root, 5)

  # Level 2
  bst.root = insert(bst.root, 3)
  bst.root = insert(bst.root, 8)

  # Level 3
  bst.root = insert(bst.root, 4)
  bst.root = insert(bst.root, 6)
  bst.root = insert(bst.root, 10)
  bst.root = insert(bst.root, 1)

  print 'Inorder traversal: '
  inorder(bst.root)  # 1 3 4 5 6 8 10

  print '\n\nNodes level by level: '
  print_tree_level_by_level(bst.root)

if __name__ == '__main__':
  main()

# Output:
# ------------------------
# Inorder traversal:
# 1 3 4 5 6 8 10
#
# Nodes level by level:
# 5
# 3 8
# 1 4 6
