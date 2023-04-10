#!/usr/bin/python

# Date: 2018-11-24
#
# Description:
# Write an iterative program to do inorder traversal of binary tree.
#
# Motivation:
# Recursive programs may cause stack overflow if recursion depth reaches a
# certain limit.
#
# Approach:
# Take a stack and push all nodes traversing left nodes once we reach leaf print
# that node and traverse right sub tree till node.
# 
# Reference:
# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
#
# Complexity:
# O(N) Time and Space

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inorder(root):
  stack = []
  current = root

  while True:
    if current is not None:  # Traverse whole left sub tree
      stack.append(current)
      current = current.left
    else:
      if not stack:  # current is None and stack is empty - BREAK
        break
      else:
        current = stack.pop()
        print(current.data, end=' ')
        current = current.right  # We are done with left and root, traverse right sub tree
  print()
        
# Above implementation also works but this is simpler than above function
def inorder_simple(root):
    node = root
    stack = []
    while True:
        while node:
            stack.append(node)
            node = node.left

        if not stack:
            break
        node = stack.pop()
        print(node.data, end=' ')

        node = node.right
    print()

def inorder_simple2(root):
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.data, end=' ')
        node = node.right
    print()

def main():
  root = Node(10)
  root.left = Node(5)
  root.left.left = Node(3)
  root.left.right = Node(8)

  root.right = Node(15)
  root.right.left = Node(12)
  root.right.right = Node(18)

  inorder(root)  # 3 5 8 10 12 15 18
  inorder_simple(root)  # 3 5 8 10 12 15 18
  inorder_simple2(root)  # 3 5 8 10 12 15 18

if __name__ == '__main__':
  main()
