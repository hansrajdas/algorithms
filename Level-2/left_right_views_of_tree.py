#!/usr/bin/python

# Date: 2018-11-12
#
# Description:
# - Print all elements visible while looking from left side of the tree.
# - Print all elements visible while looking from right side of the tree.
#
# Approach:
# We can keep track of level of a node by passing a parameter to all recursive
# calls. The idea is to keep track of maximum level also. Whenever we see a node
# whose level is more than maximum level so far, we print the node because this
# is the first node in its level.
#
# For left view, we traverse left sub tree before right and for right view we
# traverse the right sub tree before left.
#
# Note:
# To track max level we should use mutable data type(like list of 1 element) so
# that is globally updated across all recursive calls.
#
# Complexity:
# O(N)

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def left_view_util(root, level, max_level):
  if not root:
    return None

  if level > max_level[0]:
    print root.data
    max_level[0] = level

  left_view_util(root.left, level + 1, max_level)
  left_view_util(root.right, level + 1, max_level)

def left_view(root):
  print 'Left view: '
  max_level = [0]  # Need a mutable datatype so using list with 1 element
  return left_view_util(root, 1, max_level)

def right_view_util(root, level, max_level):
  if not root:
    return None

  if level > max_level[0]:
    print root.data
    max_level[0] = level

  right_view_util(root.right, level + 1, max_level)
  right_view_util(root.left, level + 1, max_level)

def right_view(root):
  print 'Right view: '
  max_level = [0]  # Need a mutable datatype so using list with 1 element
  return right_view_util(root, 1, max_level)


def main():
  # TC - 1
  root = Node(12)
  root.left = Node(10)
  root.right = Node(20)
  root.right.left = Node(25)
  root.right.right = Node(40)

  left_view(root)  # 12 10 25
  right_view(root)  # 12 20 40

  # TC - 2
  root = Node(12)
  root.left = Node(10)
  root.right = Node(20)
  root.right.right = Node(30)
  root.right.right.right = Node(40)

  left_view(root)  # 12 10 30 40
  right_view(root)  # 12 20 30 40


if __name__ == '__main__':
  main()
