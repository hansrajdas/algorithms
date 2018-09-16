#!/usr/bin/python

# Date: 2018-09-16
#
# Description:
# Delete a node of a singly linked list, given only access to that node.
#
# Approach:
# As we don't have access to head, we can't go back or so. We can copy the data
# from next node to this and delete the next node.
#
# Note: If reference to last node is given then we can't follow this approach.
#
# Complexity:
# O(1)


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

  def delete_node(self, node):
    """
    Deletes given node from linked list.

    Args:
      node: Reference of node to be deleted.
    """
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next

def main():
  linked_list = LinkedList()

  linked_list.insert_at_end(1)
  linked_list.insert_at_end(2)
  linked_list.insert_at_end(3)
  linked_list.insert_at_end(4)
  linked_list.insert_at_end(5)

  linked_list.traverse()

  print ('\nRemoving third node')
  linked_list.delete_node(linked_list.head.next.next)
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

# Removing third node
# 1
# 2
# 4
# 5
