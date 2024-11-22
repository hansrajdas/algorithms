#!/usr/bin/python

"""
Date: 2020-02-14

Description
-----------
Write an iterative program to do postorder traversal of binary tree.

Approach
--------
Hacky method is used to manipulate preoder traversal, then reverse the result.

NOTE
----
Actual postoder iterative is bit complex than pre and inorder

Complexity
----------
O(N) Time and Space
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def postorder(root):
    pass  # TODO

def postorder_hacky(root):
    if root is None:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.data)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]


def main():
  root = Node(10)
  root.left = Node(5)
  root.left.left = Node(3)
  root.left.right = Node(8)

  root.right = Node(15)
  root.right.left = Node(12)
  root.right.right = Node(18)

  assert postorder_hacky(root) == [3, 8, 5, 12, 18, 15, 10]


if __name__ == '__main__':
  main()
