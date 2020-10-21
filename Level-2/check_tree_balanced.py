#!/usr/bin/python

# Date: 2020-10-22
#
# Description:
# Implement a function to check if a binary tree is balanced. A balanced tree
# is defined to be a tree such that the heights of the two subtrees of any node
# never differ by more than one.
#
# Approach:
# Take height of left subtree and right subtree for each node and if difference
# in heights is more than 1 for any node, tree is not balanced.
#
# Complexity:
# O(N) Time

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_tree_balanced_utils(root):
    if root is None:
        return 0
    height_left = check_tree_balanced_utils(root.left)
    height_right = check_tree_balanced_utils(root.right)
    if abs(height_left - height_right) > 1:
        return False
    return 1 + max(height_left, height_right)

def check_tree_balanced(root):
    check = check_tree_balanced_utils(root)
    if check is False:
        return False
    return True

def main():
    root = Node(1)
    assert check_tree_balanced(root) == True

    root = Node(1)
    root.left = Node(2)
    assert check_tree_balanced(root) == True

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    assert check_tree_balanced(root) == False

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.right = Node(4)
    assert check_tree_balanced(root) == True

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.right = Node(4)
    root.right.right = Node(5)
    assert check_tree_balanced(root) == True

main()
