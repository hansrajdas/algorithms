#!/usr/bin/python

# Date: 2018-09-16
#
# Description:
# Find kth element from last in a singly linked list.
#
# Approach:
# Take 2 pointers p1 and p2, move p1 to kth node from beginning and p2 at head.
# Now iterate over linked list until p1 reaches end as when p1 reaches end p2
# will be k nodes behind which is kth from last.
#
# Complexity:
# O(n) Time


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

  def kth_from_last(self, k):
    """Find kth element from last."""
    p1 = self.head
    p2 = self.head

    for i in range(k):
      if not p1:
        return None
      p1 = p1.next

    # Now p1 is at kth position from head and p2 is at starting/head.
    # Iterate over linked list until p1 reaches end, when p1 will reach end, p2
    # will be at (n - k) position, which is kth from last.
    while p1:
      p1 = p1.next
      p2 = p2.next

    return p2.data

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

  k = input('Enter k: ')
  print ('%d-th element from last is: %d' % (k, linked_list.kth_from_last(k)))


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
# Enter k: 2
# 2-th element from last is: 5
