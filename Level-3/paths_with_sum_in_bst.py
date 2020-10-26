#!/usr/bin/python

# Date: 2020-10-26
#
# Description:
# Given a binary tree in which each node contains an integer value(which might
# be positive or negative). Design an algorithm to count the number of paths
# that sum to a given value. The path does not need to start or end at root or
# a leaf, but it must go downwards(travelling only from parent nodes to child
# nodes).
#
# Approach:
# This is brute force approach. Consider all nodes in binary tree and count
# number of paths having given pathSum subtree rooted with that node.
#
# Complexity:
# Consider N = number of nodes in tree and d = depth of tree
# From root we will have to check N - 1 nodes below it, similarly for next
# level we has to check N - 3 nodes below it and so on... This can equated as:
# >>> (N - 1) + (N - 3) + (N - 7) + ... d times... + (N - N)
# >>> O(N * d - (1 + 3 + 7 + ... d times ... + N))
# >>> O(N * d - (2^1 - 1 + 2^2 - 1 + 2^3 - 1 .... 2^d - 1))
# >>> O(N * d - N)
# >>> O(N * d)
# >> O(NlogN) time complexity

class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

def path_with_given_sum_node(root, total_sum, current_sum):
    if root is None:
        return 0
    total_paths = 0
    current_sum += root.k
    if current_sum == total_sum:
        total_paths += 1
    total_paths += path_with_given_sum_node(root.left, total_sum, current_sum)
    total_paths += path_with_given_sum_node(root.right, total_sum, current_sum)
    return total_paths

def path_with_given_sum(root, target_sum):
    if root is None:
        return 0
    # Paths from root
    paths = path_with_given_sum_node(root, target_sum, 0)

    # Paths from left and right subtree
    left_paths = path_with_given_sum(root.left, target_sum)
    right_paths = path_with_given_sum(root.right, target_sum)
    return paths + left_paths + right_paths

def main():
    root = Node(10)

    assert path_with_given_sum(root, 10) == 1
    assert path_with_given_sum(root, 20) == 0

    root.left = Node(5)
    root.right = Node(20)

    assert path_with_given_sum(root, 10) == 1
    assert path_with_given_sum(root, 15) == 1
    assert path_with_given_sum(root, 30) == 1
    assert path_with_given_sum(root, 35) == 0
    assert path_with_given_sum(root, 30) == 1
    assert path_with_given_sum(root, 20) == 1

main()
