#!/usr/bin/python

# Date: 2018-11-24
#
# Description:
# Write an iterative program to do preorder traversal of binary tree.
#
# Approach:
# Push root to stack and run loop until stack is not empty:
# - Pop last node from stack and print it
# - If current has right node, push it
# - If current has left node, push it
# 
# Reference:
# https://www.geeksforgeeks.org/iterative-preorder-traversal/
#
# Complexity:
# O(N) Time and Space

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preOrder(root):
  if not root:
    return None

  stack = [root]
  while stack:
    current = stack.pop()
    print current.data,  # print current node, then traverse lower tree

    # In preorder sequence is root(printed above), left then right so we push
    # right first then left as stack is LIFO
    if current.right:
      stack.append(current.right)

    if current.left:
      stack.append(current.left)

def main():
  root = Node(10)
  root.left = Node(5)
  root.left.left = Node(3)
  root.left.right = Node(8)

  root.right = Node(15)
  root.right.left = Node(12)
  root.right.right = Node(18)

  preOrder(root)  # 10 5 3 8 15 12 18

if __name__ == '__main__':
  main()
