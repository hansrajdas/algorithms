#!/usr/bin/python

# Date: 2020-10-31
#
# Description:
# Imagine you are reading in a stream of integers. Periodically, you wish to be
# able to look up the rank of a number x (the number of values less than or
# equal to x). Implement the data structures and algorithms to support these
# operations. That is, implement the method track(int x), which is called when
# each number is generated, and the method getRankOfNumber(int x), which
# returns the number of values less than or equal to x (not including x
# itself).
# EXAMPLE
# Stream (in order of appearance) : 5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(1) = 0
# getRankOfNumber(3) = 1
# getRankOfNumber(4) = 3
#
# Implementation:
# Requirement is just to store the elements in sorted order and return index of
# the item whose rank is required but as items are generated periodically,
# using an array would be costly as shifting would be required to insert new
# element at correct(to maintain sorted order) place.
#
# So to overcome this problem we can use binary search tree and store
# additional info(count of an element as we can have duplicates) with data.
# We can track and update count if duplicate element is inserted again using
# below approach while inserting in BST:
# - Insert in BST as usual but if we see a duplicate, increment count var in
#   in that node by 1
#
# While fetching rank we just do an inorder traversal and keep on adding count
# to the rank for each node traversed. Once we find the required node, we stop
# further traversal.
#
# Complexity:
# Insert: O(log(n)), find rank: O(log(n)) 
#/

class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None
        self.count = 1

class BST:
    def __init__(self):
        self.root = None

    def track(self, root, k):
        if root is None:
            return Node(k)
        if root.k > k:
            root.left = self.track(root.left, k)
        elif root.k < k:
            root.right = self.track(root.right, k)
        else:
            root.count += 1
        return root

    def traverse(self, root):
        if root:
            self.traverse(root.left)
            print('%d(%d)' % (root.k, root.count))
            self.traverse(root.right)

    def get_rank_of_number(self, root, k):
        self.rank = -1
        def _get_rank(root, k):
            if root:
                status = _get_rank(root.left, k)
                if status is not None:
                    return True
                self.rank += root.count
                if root.k == k:
                    return True
                return _get_rank(root.right, k)
        rank_found = _get_rank(root, k)
        if rank_found is None:
            return -1
        return self.rank

def main():
    bst = BST()

    for i in [5, 1, 4, 4, 5, 9, 7, 13, 3]:
        bst.root = bst.track(bst.root, i)
    bst.traverse(bst.root)

    for r in [1, 3, 4, 5, 13]:
        print('Rank of %d is: %d' % (r, bst.get_rank_of_number(bst.root, r)))

    for r in [0, 2, 6, 10, 14, 15]:
        print('Rank of %d is: %d' % (r, bst.get_rank_of_number(bst.root, r)))


main()
