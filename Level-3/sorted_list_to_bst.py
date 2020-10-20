#!/usr/bin/python

# Date: 2020-10-20
#
# Description:
# Given a sorted(increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.
#
# Approach:
# Use divide and conquer array and populate tree nodes
# - Insert into the tree the middle element of the array
# - Insert(into the left subtree) the left subarray elements
# - Insert(into the right subtree) the right subarray elements
#
# Complexity:
# O(N)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_inorder(root):
    if root:
        tree_inorder(root.left)
        print(root.data, end=' ')
        tree_inorder(root.right)

def sorted_list_to_bst_utils(A, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    node = Node(A[mid])
    node.left = sorted_list_to_bst_utils(A, start, mid - 1)
    node.right = sorted_list_to_bst_utils(A, mid + 1, end)
    return node


def sorted_list_to_bst(A):
    return sorted_list_to_bst_utils(A, 0, len(A) - 1)

def main():
    root = sorted_list_to_bst([1, 2, 3])
    tree_inorder(root)  # 1 2 3
    print()

    root = sorted_list_to_bst([1, 2, 3, 4, 5])
    tree_inorder(root)  # 1 2 3 4 5
    print()

main()
