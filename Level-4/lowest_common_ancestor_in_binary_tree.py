#!/usr/bin/python

# Date: 2018-09-21
#
# Description:
# Find lowest common ancestor of given 2 nodes in binary tree.
#
# Approach:
# Recursively checked all left and right sub trees if both nodes are present or
# not. There may be cases when one of the node is descendant of other so we
# will try to find descendant node in sub tree rooted with parent node.
# For example, we are trying to find LCA(1, 2) and suppose 2 is left child of 1
# after finding 1 in LCA recursion function we will search for 2 in sub tree
# rooted with 1.
#
# Complexity:
# O(n) Time


class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self):
    self.root = None

  def find_lca_util(self, root, n1, n2, found):
    """Finds LCA of n1 and n2 in sub tree rooted with root.

    Also updates found dictionary to indicate which node is found.
    """
    if root is None:
      return None

    if root.key == n1:
      found[n1] = True
      return root
    if root.key == n2:
      found[n2] = True
      return root

    lca_left = self.find_lca_util(root.left, n1, n2, found)
    lca_right = self.find_lca_util(root.right, n1, n2, found)

    if lca_left and lca_right:
      return root
    elif lca_left is None:
      return lca_right
    else:
      return lca_left

  def find(self, root, k):
    """Searches a key in binary tree rooted with root."""
    if root is None:
      return False
    elif root.key == k or self.find(root.left, k) or self.find(root.right, k):
      return True
    else:
      return False

  def find_lca(self, n1, n2):
    """Finds and returns LCA for n1 and n2."""
    found = {n1: False, n2: False}
    lca = self.find_lca_util(self.root, n1, n2, found)

    # 3 Cases:
    # --------
    # 1. Both n1 and n2 found
    # 2. n1 is found, search for n2 in sub tree rooted with lca
    # 3. n2 is found, search for n1 in sub tree rooted with lca
    #
    # Cases 2 and 3 handle situations like n1 or n2 is in sub tree rooted with
    # n2 or n1 respectively. This situation is not handled in utils function so
    # taking care here.
    if (found[n1] and found[n2] or
      found[n1] and self.find(lca, n2) or
      found[n2] and self.find(lca, n1)):
      return lca

    return None

def main():
  tree = BinaryTree()
  tree.root = Node(1)
  tree.root.left = Node(2)
  tree.root.right = Node(3)

  tree.root.left.left = Node(4)
  tree.root.left.right = Node(5)

  lca = tree.find_lca(3, 5)
  if lca:
    print 'Found, key: %d, id: %d' % (lca.key, id(lca))
  else:
    print 'One of the 2 nodes not found in tree'


if __name__ == '__main__':
  main()


# Output:
# ----------------------------------
# Found, key: 1, id: 140390977940656
