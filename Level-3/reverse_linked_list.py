#!/usr/bin/python

# Date: 2018-09-16
#
# Description:
# Reverse a linked list.
#
# Approach:
# Take 3 pointers to keep track of previous, current and next node in linked
# list. Loop until current is not null and reverse pointers.
# After loop update head with previous.
#
# Reference:
# https://medium.com/outco/reversing-a-linked-list-easy-as-1-2-3-560fbffe2088
#
# Another simple way of reversing linked list is to process each node and keep
# on inserting at another head, explained here: https://leetcode.com/problems/reverse-nodes-in-k-group/solution/
#
# Complexity:
# O(n)


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def traverse(self):
    current = self.head
    while current:
      print(current.data, end=' ')
      current = current.next

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return None

    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  def reverse(self):
    """Reverses a linked list."""
    previous = None
    current = self.head
    nxt = self.head

    while current:
      nxt = nxt.next
      current.next = previous
      previous = current
      current = nxt
    self.head = previous

  def reverse_list_using_insert_at_head(self, head, k):
      """
      This is simple way of reversing linked list - process each node and keep
      on inserting at another head.
      Explained here(premium): https://leetcode.com/problems/reverse-nodes-in-k-group/solution/
      """
      # Reverse k nodes of the given linked list.
      # This function assumes that the list contains 
      # atleast k nodes.
      new_head = None
      ptr = head
      while k:
          next_node = ptr.next
          
          # Insert the node pointed to by "ptr"
          # at the beginning of the reversed list
          ptr.next = new_head
          new_head = ptr
          ptr = next_node
          k -= 1
      return new_head


def main():
  linked_list = LinkedList()
  linked_list.insert_at_end(1)
  linked_list.insert_at_end(2)
  linked_list.insert_at_end(3)
  linked_list.insert_at_end(4)
  linked_list.insert_at_end(5)
  linked_list.traverse()

  linked_list.reverse()
  print('\nReversed linked list', end=' ')
  linked_list.traverse()

  print()
  linked_list = LinkedList()
  linked_list.insert_at_end(1)
  linked_list.insert_at_end(2)
  linked_list.insert_at_end(3)
  linked_list.insert_at_end(4)
  linked_list.insert_at_end(5)
  linked_list.traverse()

  rev_head = linked_list.reverse_list_using_insert_at_head(linked_list.head, 5)
  print('\nReversing by insert at head', end=' ')
  linked_list.head = rev_head
  linked_list.traverse()


if __name__ == '__main__':
  main()


# Output:
# -------------
# 1
# 2
# 3
# 4
# 5

# Reversed linked list
# 5
# 4
# 3
# 2
# 1
