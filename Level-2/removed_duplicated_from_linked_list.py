#!/usr/bin/python

# Date: 2018-09-16
#
# Description:
# Remove duplicates from a singly linked list.
#
# Approach:
# Use a map/set to keep track of elements are seen before and they appear again
# delete from linked list.
#
# Note: To do this problem without space, we can traverse with 2 pointers and
# nested, it will require O(n^2) time.
#
# Complexity:
# O(n) time, O(n) space


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

  def remove_duplicates(self):
    """Removes duplicate from a linked list."""
    values = set()
    current = self.head
    while current:
      if current.data in values:
        prev.next = current.next
      else:
        values.add(current.data)
        prev = current
      current = current.next

def main():
  linked_list = LinkedList()

  linked_list.insert_at_end(1)
  linked_list.insert_at_end(1)
  linked_list.insert_at_end(2)
  linked_list.insert_at_end(3)
  linked_list.insert_at_end(2)
  linked_list.insert_at_end(4)
  linked_list.insert_at_end(1)
  linked_list.insert_at_end(5)
  linked_list.insert_at_end(5)

  linked_list.traverse()

  print ('\nDuplicates removed:')
  linked_list.remove_duplicates()
  linked_list.traverse()

if __name__ == '__main__':
  main()


# Output:
# -------------
# 1
# 1
# 2
# 3
# 2
# 4
# 1
# 5
# 5

# Duplicates removed:
# 1
# 2
# 3
# 4
# 5
