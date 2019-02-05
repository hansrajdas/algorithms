#!/usr/bin/python

# Date: 2019-02-05
#
# Description:
# Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
# The left and right pointers in nodes are to be used as previous and next
# pointers respectively in converted DLL. The order of nodes in DLL must be same
# as Inorder of the given Binary Tree. For example, if tree is:
#              5
#             / \
#            4   6
#
# DLL should have elements(inorder of BT): 4, 5, 6
#
# Approach:
# We traverse the tree in inorder fashion. We add nodes at the beginning of
# current linked list and update head of the list using pointer to head pointer.
# Since we insert at the beginning, we need to process leaves in reverse order.
# For reverse order, we first traverse the right subtree before the left subtree
# .i.e. do a reverse inorder traversal.
#
# Reference:
# https://www.geeksforgeeks.org/convert-a-given-binary-tree-to-doubly-linked-list-set-4/
#
# Complexity:
# O(N) time

class Node:
  """Binary tree or doubly linked list node."""
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def BTtoDLL(root, head):
  """Converts a binary tree with given root pointer to doubly linked list."""
  if not root:
    return root

  BTtoDLL(root.right, head)
  root.right = head[0]
  if head[0]:
    head[0].left = root
  head[0] = root
  BTtoDLL(root.left, head)


def inorder(root):
  if root:
    inorder(root.left)
    print root.data,
    inorder(root.right)


def print_dll(head):
  print '\nDLL traversal, forward:',
  p = head
  while p:
    print p.data,
    p = p.right

  print '\nDLL traversal, backward:',
  # Move pointer to end
  p = head
  while p and p.right:
    p = p.right

  # Traverse from back
  while p:
    print p.data,
    p = p.left


## TC - 1
root = None
head = [None]  # Make head mutable

print 'Inorder traversal:',
inorder(root)
BTtoDLL(root, head)
print_dll(head[0])

## TC - 2
root = Node(1)
head = [None]

print '\n\nInorder traversal:',
inorder(root)  # 1
BTtoDLL(root, head)
print_dll(head[0])  # forward: 1, backward: 1

## TC - 3
#   1
#  /
# 2
root = Node(1)
root.left = Node(2)
head = [None]

print '\n\nInorder traversal:',
inorder(root)  # 2 1
BTtoDLL(root, head)
print_dll(head[0])  # forward: 2 1, backward: 1 2

## TC - 4
#   1
#  / \
# 2   3
root = Node(1)
root.left = Node(2)
root.right = Node(3)
head = [None]

print '\n\nInorder traversal:',
inorder(root)  # 2 1 3
BTtoDLL(root, head)
print_dll(head[0])  # forward: 2 1 3, backward: 3 1 2
