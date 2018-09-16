#!/usr/bin/python

# Date: 2018-09-16
#
# Description:
# Implement linked list in python and perform basic operations.
#
# Reference:
# https://stackoverflow.com/questions/280243/python-linked-list
# https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/


class Node:
    def __init__(self, data):
        self.data = data  # Contains data
        self.next = None  # Contains reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_at_start(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link the new node to the 'previous' node.
        self.head = new_node  # Set the current node to the new one.

    def add_node_at_end(self, data):
      new_node = Node(data)
      if self.head is None:
        self.head = new_node
        return None

      node = self.head
      while node.next:
        node = node.next
      node.next = new_node

    def list_print(self):
        node = self.head  # Cant point to ll!
        while node:
            print node.data
            node = node.next


ll = LinkedList()
ll.add_node_at_start(1)
ll.add_node_at_start(2)
ll.add_node_at_start(3)
ll.add_node_at_end(4)

ll.list_print()


# Output:
# -------
# 3
# 2
# 1
# 4
