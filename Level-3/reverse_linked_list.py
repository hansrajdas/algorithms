#!/usr/bin/python

# Date: 2018-09-16
#
# Description:
# Reverse a linked list.
#
# Approach:
# Take 3 pointers to keep track of previous, current and next node in linked
# list. Loop until current is not null and reverse pointers.
# After loop update head with previous
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
      print current.data
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
    nxt = None

    while current:
      nxt = current.next
      current.next = previous
      previous = current
      current = nxt
    self.head = previous

def main():
  linked_list = LinkedList()

  linked_list.insert_at_end(1)
  linked_list.insert_at_end(2)
  linked_list.insert_at_end(3)
  linked_list.insert_at_end(4)
  linked_list.insert_at_end(5)
  linked_list.traverse()

  linked_list.reverse()
  print ('\nReversed linked list')
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
