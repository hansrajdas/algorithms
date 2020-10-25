#!/usr/bin/python

# Date: 2020-10-25
#
# Description:
# T1 and T2 are two very large binary trees, with T1 much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of T1.
#
# A tree T2 is a subtree of T1 if there exists a node nin T1 such that the
# subtree of n is identical to T2. That is, if you cut odd that tree at node
# n, the two trees would be identical.
#
# Approach:
# Preorder is one the traversals which can be used find if 2 trees are same or
# not. But it has small edge case which needs to handled like below:
# T1: 2        T2: 2
#    /              \
#   1                1
# In above case both tree will have same preorder traversal sequence(2 -> 1)
# but trees are not same. To handle this scenario we can have some NULL char(
# like X) to indicate NULL while comparing.
#
# Complexity:
# n = Number of nodes in larger tree(T1)
# m = Number of nodes in smaller tree(T2)
# O(n + m) time and space

class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

def preorder(root, order):
    if root is None:
        order.append('X')
        return
    order.append(root.k)
    preorder(root.left, order)
    preorder(root.right, order)

def check_subtree(large, small):
    if small is None:
        return True
    if large is None:
        return False

    order = []
    preorder(small, order)
    small_preorder = ''.join(str(i) for i in order)

    order = []
    preorder(large, order)
    large_preorder = ''.join(str(i) for i in order)

    return small_preorder in large_preorder


def main():
    # Case 1
    large = Node(10)
    large.left = Node(5)
    large.right = Node(20)

    large.left.left = Node(3)
    large.left.right = Node(7)

    small = Node(5)
    small.left = Node(3)
    small.right = Node(7)

    assert check_subtree(large, small) == True

    # Case 2
    large = Node(10)
    large.left = Node(5)
    large.right = Node(20)

    large.left.left = Node(3)
    large.left.right = Node(7)

    small = Node(5)
    small.left = Node(3)
    small.right = Node(7)
    small.left.left = Node(20)

    assert check_subtree(large, small) == False

main()
