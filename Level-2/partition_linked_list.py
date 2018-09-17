#!/usr/bin/python

# Date: 2018-09-17
#
# Description:
# There is a linked list given and a value x, partition a linked list such that
# all element less x appear before all elements greater than x.
# X should be on right partition.
#
# Like, if linked list is:
# 3->5->8->5->10->2->1 and x = 5
#
# Resultant linked list should be:
# 3->2->1->5->8->5->10
#
# Approach:
# Maintain 2 linked list 'BEFORE' and 'AFTER'. Traverse given linked list, if
# value at current node is less than x insert this node at end of 'BEFORE'
# linked list otherwise at end of 'AFTER' linked list.
# At the end, merge both linked lists.
#
# Complexity:
# O(n)


class Node:
    def __init__(self, data):
        self.data = data  # Contains data
        self.next = None  # Contains reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None

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

    def partition(self, x):
      before_start = None
      before_end = None
      after_start = None
      after_end = None
      
      node = self.head
      while node:
        if node.data < x:  # Insert at end of before linked list.
          if before_start is None:
            before_start = node
            before_end = node
          else:
            before_end.next = node
            before_end = node
        else:
          if after_start is None:
            after_start = node
            after_end = node
          else:
            after_end.next = node
            after_end = node
        node = node.next

      after_end.next = None
      if before_start is None:
        self.head = after_start
        return None

      # Merge before and after linked list.
      before_end.next = after_start
      self.head = before_start


linked_list = LinkedList()
linked_list.add_node_at_end(3)
linked_list.add_node_at_end(5)
linked_list.add_node_at_end(8)
linked_list.add_node_at_end(5)
linked_list.add_node_at_end(10)
linked_list.add_node_at_end(2)
linked_list.add_node_at_end(1)

linked_list.list_print()

linked_list.partition(5)

print ('\nLinked list partitioned with respect to 5')
linked_list.list_print()


# Output:
# -------
# 3
# 5
# 8
# 5
# 10
# 2
# 1

# Linked list partitioned with respect to 5
# 3
# 2
# 1
# 5
# 8
# 5
# 10
