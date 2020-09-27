#!/usr/bin/python

# Date: 2019-01-31
#
# Description:
# Given a BST and a number k, find the kth smallest number from BST.
# For example if below is the BST given,
# For k = 1, value = 4
# For k = 2, value = 5
# For k = 3, value = 6
# For k > 3, Raise exception
#              5
#             / \
#            4   6
#
# Approach:
# Take k as mutable parameter(list with one item) in function. Perform inorder
# traversal for BST and whenever we are processing an element decrement the value
# of k and check if it has reached 0, if yes, we have found the value, return
# that value. Take care of this in parent functions return also so that correct
# value gets returned instead of last value from function call stack.
#
# Complexity:
# O(k)

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def inorder(self, root):
    if root:
      self.inorder(root.left)
      print(root.key, end=' ')
      self.inorder(root.right)

  def kth_smallest(self, root, k):
    self.k = k
    def inorder(root):
        if root:
          val = inorder(root.left)
          if val is not None:
            return val
          self.k -= 1
          if not self.k:
            return root.key
          return inorder(root.right)
    return inorder(root)

def main():
  bst = BST()
  bst.root = Node(5)
  bst.root.left = Node(4)
  bst.root.right = Node(6)

  print('Inorder traversal:', end=' ')
  bst.inorder(bst.root)  # 4 5 6

  value = bst.kth_smallest(bst.root, 3)
  if value:
    print('\nKth smallest(k = %d) element is: %d' % (3, value))  # 6
  else:
    print('Value of k is larger than the number of nodes in BST')

  value = bst.kth_smallest(bst.root, 4)
  if value:
    print('\nKth smallest(k = %d) element is: %d' % (4, value))
  else:
    print('Value of k is larger than the number of nodes in BST')  # This executed


if __name__ == '__main__':
  main()
