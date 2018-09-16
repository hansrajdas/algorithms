#!/usr/bin/python

# Date: 2018-
#
# Description:
# Reverse a linked list.
#
# Approach:
#
# Complexity:


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

def main():
  linked_list = LinkedList()

  linked_list.insert_at_end(1)
  linked_list.insert_at_end(2)
  linked_list.insert_at_end(3)
  linked_list.insert_at_end(4)
  linked_list.insert_at_end(5)

  linked_list.traverse()


if __name__ == '__main__':
  main()


# Output:
# -------------
