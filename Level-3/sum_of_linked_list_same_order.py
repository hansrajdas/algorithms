#!/usr/bin/python

# Date: 2018-09-18
#
# Description:
# Two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in forward order, such that the 1's digit is at
# the tail of the list. Write a function that adds the two numbers and returns
# the sum as a linked list in forward order. For example:
#
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295
# Output: 9 -> 1 -> 2. That is, 912.
# 
#
# Approach:
# Add padding 0's at starting of list which is shorter. Use recursive approach
# to reach at end of each list, keep adding corresponding digits and track
# carry also.
# If sum of most significant digits also return a carry then handle this also,
# insert 1 to start of list again.
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

    def length(self):
      node = self.head
      count = 0
      while node:
        count += 1
        node = node.next
      return count

    def add_padding(self, count):
      """Pads linked list with given number of 0's."""
      for i in range(count):
        node = Node(0)
        node.next = self.head
        self.head = node

    def sum_linked_list_util(self, head_1, head_2):
      """
      Adds digits of 2 linked list with *SAME* length. Stores the result digits
      at starting of third list.

      Args:
        head_1: Reference to head of first linked list.
        head_2: Reference to head second linked list.
      """
      if (not head_1) and (not head_2):
        return 0

      carry = self.sum_linked_list_util(head_1.next, head_2.next)

      value = carry + head_1.data + head_2.data
      self.add_node_at_start(value % 10)
      return value/10

    def sum_linked_list_nodes(self, list_1, list_2):
      """
      Adds digit of 2 linked list from head to tail and appends at start of
      another list.

      Args:
        list_1: Reference to first linked list.
        list_2: Reference to second linked list.
      """
      len_1 = list_1.length()
      len_2 = list_2.length()
      if len_1 > len_2:
        list_2.add_padding(len_1 - len_2)
        print ('\nAdding padding 0s to list 2:')
        list_2.list_print()
      elif len_1 < len_2:
        list_1.add_padding(len_2 - len_1)
        print ('\nAdding padding 0s to list 1:')
        list_1.list_print()

      if self.sum_linked_list_util(list_1.head, list_2.head):
        # If there is a carry after adding most significant digits also.
        self.add_node_at_start(1)

# Driver
num_1 = input('Enter first number: ')
linked_list_1 = LinkedList()
for d in str(num_1):
  linked_list_1.add_node_at_end(int(d))

linked_list_1.list_print()

num_2 = input('Enter second number: ')
linked_list_2 = LinkedList()
for d in str(num_2):
  linked_list_2.add_node_at_end(int(d))

linked_list_2.list_print()

linked_list_result = LinkedList()
linked_list_result.sum_linked_list_nodes(linked_list_1, linked_list_2)
print ('\nLinked list after sum:')
linked_list_result.list_print()


# Output:
# -------
# Enter first number: 617
# 6 -> 1 -> 7 -> None
# Enter second number: 295
# 2 -> 9 -> 5 -> None
# 
# Linked list after sum:
# 9 -> 1 -> 2 -> None


# Enter first number: 99
# 9 -> 9 -> None
# Enter second number: 999
# 9 -> 9 -> 9 -> None
# 
# Adding padding 0s to list 1:
# 0 -> 9 -> 9 -> None
# 
# Linked list after sum:
# 1 -> 0 -> 9 -> 8 -> None
