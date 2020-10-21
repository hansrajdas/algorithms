#!/usr/bin/python

# Date: 2020-10-21
#
# Description:
# Given a binary tree, design an algorithm which creates a linked list of all
# the nodes in each depth(for d level we will have d linked lists)
#
# Approach:
# Do tree level order traversal and add all nodes at a specific level to a
# new linked list
#
# Complexity:
# O(N) Time and space

import collections

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        p = self.head
        while p:
            print(p.data, end=' ')
            p = p.next

    def add_end(self, data):
        if self.head is None:
            self.head = LinkedListNode(data)
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = LinkedListNode(data)

def get_list_of_depths(root):
    if root is None:
        return []
    Q = collections.deque([root])
    res = []

    while Q:
        count = len(Q)
        linked_list = LinkedList()
        while count:
            count -= 1
            node = Q.popleft()
            linked_list.add_end(node.data)
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        res.append(linked_list)
    return res

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    for linked_list in get_list_of_depths(root):
        linked_list.traverse()
        print()

main()
