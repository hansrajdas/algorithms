#!/usr/bin/python

# Date: 2018-09-18
#
# Description:
# Two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1's digit is at
# the head of the list. Write a function that adds the two numbers and returns
# the sum as a linked list. Example:
#
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295
# Output: 2 -> 1 -> 9. That is, 912
#
# Approach:
# As numbers are stored in reverse order we can scan the two linked lists and
# add corresponding digits to end of another list. If there is carry we have to
# take care of that in next digits that will be added.
#
# Complexity:
# O(n), where n = length of larger list.


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
            print ('%d ->' % node.data),
            node = node.next
        print ('None')

    def sum_linked_list_nodes(self, list_1, list_2):
      """
      Adds digits of 2 linked list from head to tail and appends at end of
      another list.

      Args:
        list_1: Reference to first linked list.
        list_2: Reference to second linked list.
      """
      l1 = list_1.head
      l2 = list_2.head
      carry = 0
      while l1 or l2 or carry:
        value = carry
        if l1:
          value += l1.data
          l1 = l1.next
        if l2:
          value += l2.data
          l2 = l2.next

        carry = 1 if value > 9 else 0
        self.add_node_at_end(value % 10)


# Driver
num_1 = input('Enter first number: ')
linked_list_1 = LinkedList()
for d in str(num_1):
  linked_list_1.add_node_at_start(int(d))

linked_list_1.list_print()

num_2 = input('Enter second number: ')
linked_list_2 = LinkedList()
for d in str(num_2):
  linked_list_2.add_node_at_start(int(d))

linked_list_2.list_print()

print ('\nLinked list after sum:')
linked_list_result = LinkedList()
linked_list_result.sum_linked_list_nodes(linked_list_1, linked_list_2)
linked_list_result.list_print()


# Output:
# -------
# Enter first number: 617
# 7 -> 1 -> 6 -> None
# Enter second number: 295
# 5 -> 9 -> 2 -> None
#
# Linked list after sum:
# 2 -> 1 -> 9 -> None


# Enter first number: 897
# 7 -> 9 -> 8 -> None
# Enter second number: 586
# 6 -> 8 -> 5 -> None
#
# Linked list after sum:
# 3 -> 8 -> 4 -> 1 -> None


# Enter first number: 123
# 3 -> 2 -> 1 -> None
# Enter second number: 456
# 6 -> 5 -> 4 -> None
#
# Linked list after sum:
# 9 -> 7 -> 5 -> None


# Enter first number: 123
# 3 -> 2 -> 1 -> None
# Enter second number: 45
# 5 -> 4 -> None
#
# Linked list after sum:
# 8 -> 6 -> 1 -> None
