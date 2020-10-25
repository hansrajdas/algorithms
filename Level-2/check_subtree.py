#!/usr/bin/python

# Date: 2020-10-24
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
# Traverse along larger tree T1(using any tree traversal method) and check if
# we find a node n which is same as T2's root. If yes the check if subtree of
# T1 rooted with n is same is same as tree T2.
#
# Complexity:
# n = Number of nodes in larger tree(T1)
# m = Number of nodes in smaller tree(T2)
# O(n + km), k = Number of occurrences of T2's root in T1
# O(logn(n) + log(m))

class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

def check_subtree_utils(large, small):
    if large is None or small is None:
        return large is small
    if large.k != small.k:
        return False
    return (check_subtree_utils(large.left, small.left) and
            check_subtree_utils(large.right, small.right))

def check_subtree(large, small):
    if small is None:
        return True
    if large is None:
        return False
    if large.k == small.k and check_subtree_utils(large, small):
        return True
    return check_subtree(large.left, small) or check_subtree(large.right, small)


def main():
    large = Node(10)
    large.left = Node(5)
    large.right = Node(20)

    large.left.left = Node(3)
    large.left.right = Node(7)

    small = Node(5)
    small.left = Node(3)
    small.right = Node(7)

    assert check_subtree(large, small) == True

main()
