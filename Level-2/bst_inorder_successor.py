#!/usr/bin/python

# Date: 2020-10-22
#
# Description:
# Write an algorithm to find the next node(i.e., inorder successor) of a given
# node in a binary search tree. We can assume that each node has link to its
# parent.
#
# Approach:
# - If given node has a right subtree then take smallest from right subtree
# - Otherwise keep on checking parent node, break when first greater than given
#   is found
#
# Complexity:
# O(h) time, h is height of tree

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

def get_smallest(node):
    while node.left:
        node = node.left
    return node.data

def get_inorder_successor_no_right_child(node):
    parent = node.parent
    while parent and parent.data < node.data:
        parent = parent.parent
    return parent.data if parent else None

def get_inorder_successor(node):
    if node.right is None:
        return get_inorder_successor_no_right_child(node)
    return get_smallest(node.right)

def main():
    root = Node(10)

    root.left = Node(5, root)
    root.right = Node(20, root)

    root.left.left = Node(3, root.left)
    root.left.left.left = Node(2, root.left.left)
    root.left.left.right = Node(4, root.left.left)

    root.right.right = Node(25, root.right)

    assert get_inorder_successor(root) == 20  # (10)
    assert get_inorder_successor(root.left) == 10  # (5)
    assert get_inorder_successor(root.right) == 25  # (20)
    assert get_inorder_successor(root.left.left.right) == 5  # (4)

main()
