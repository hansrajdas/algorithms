#!/usr/bin/python

# Date: 2018-09-20
#
# Description:
# Given 2 linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined on reference, not
# value.
#
# Approach:
# Check last nodes of both linked lists, if they have same reference, then only
# they can have a intersection point otherwise not.
# Advance longer list by difference in number of nodes in both list. Now
# iterate over both lists and keep comparing references of nodes from both
# lists.
#
# Complexity:
# O(m + n), m and n are lengths of 2 linked lists.


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
        node = self.head
        while node:
            print ('(data: %d id: %d)->' % (node.data, id(node))),
            node = node.next
        print ('None')

    def length(self):
      node = self.head
      count = 0
      while node:
        count += 1
        node = node.next
      return count

    def get_tail(self):
      node = self.head
      while node.next:
        node = node.next
      return node

    def linked_list_intersecting_node(self, other_list):
      # If both linked list has common last node only then these 2 linked list
      # can be intersecting otherwise that's not possible.
      if not (self.get_tail() is other_list.get_tail()):
        return None

      self_len = self.length()
      other_len = other_list.length()
      if self.length() > other_list.length():
        longer_list = self.head
        shorter_list = other_list.head
        diff_count = self_len - other_len
      else:
        longer_list = other_list.head
        shorter_list = self.head
        diff_count = other_len - self_len

      # Move longer list ahead by difference between 2 linked list nodes.
      count = diff_count
      while count:
        longer_list = longer_list.next
        count -= 1

      # Now both linked list has same length from current position to tail
      # node. So can just iterate over both linked list and compare their
      # references.
      # This can also be 'while longer_list:' as both have same length now.
      while shorter_list:
        if shorter_list is longer_list:
          return shorter_list
        shorter_list = shorter_list.next
        longer_list = longer_list.next


# Driver
linked_list_1 = LinkedList()
linked_list_1.head = Node(1)
linked_list_1.head.next = Node(2)
linked_list_1.head.next.next = Node(3)
linked_list_1.head.next.next.next = Node(4)
linked_list_1.head.next.next.next.next = Node(5)
linked_list_1.list_print()

linked_list_2 = LinkedList()
linked_list_2.head = Node(10)
linked_list_2.head.next = Node(20)
linked_list_2.head.next.next = linked_list_1.head.next.next
linked_list_2.list_print()

common = linked_list_1.linked_list_intersecting_node(linked_list_2)
if common:
  print ('\nIntersecting node is: (data: %d, id: %d)' % (
    common.data, id(common)))
else:
  print ('\nBoth linked list not intersecting each other')


# Output:
# ----------------------
# (data: 1 id: 140700106383800)-> (data: 2 id: 140700106383872)-> (data: 3 id: 140700106383944)-> (data: 4 id: 140700106384016)-> (data: 5 id: 140700106384088)-> None
# (data: 10 id: 140700106384232)-> (data: 20 id: 140700106384304)-> (data: 3 id: 140700106383944)-> (data: 4 id: 140700106384016)-> (data: 5 id: 140700106384088)-> None
#
# Intersecting node is: (data: 3, id: 140700106383944)
