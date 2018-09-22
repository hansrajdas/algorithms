#!/usr/bin/python

# Date: 2018-09-16
#
# Description:
# Given a circular linked list, implement an algorithm that returns the node
# where loop begins.
#
# Approach:
# First detect if there is loop in linked list or not. To detect loop take 2
# pointers starting from head - slow and fast. Slow will run 1 steps and fast
# by 2 steps. If they meet, there is a loop otherwise not.
# Once they meet move slow pointer to head and move both fast and slow pointers
# by one. Wherever they meet again, that would be the starting node of loop.
# For proof, please refer CTCI 2.8
#
# Complexity:
# O(n), n = Total number of nodes in linked list


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

  def find_loop_begining(self):
    slow = self.head
    fast = self.head
    
    # Detect if there is a loop in linked list or not.
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      print slow.data, fast.data
      if slow is fast:  # Collision point
        break

    # If fast pointer has reached end/null, no loop in the linked list.
    if (fast is None) or (fast.next is None):
      return None
    
    slow = self.head
    while slow != fast:
      slow = slow.next
      fast = fast.next

    return slow  # or return fast, both will be at loop starting node.


def main():
  linked_list = LinkedList()
  loop_start = Node(4)

  linked_list.head = Node(1)
  linked_list.head.next = Node(2)
  linked_list.head.next.next = Node(3)
  linked_list.head.next.next.next = loop_start
  linked_list.head.next.next.next.next = Node(5)
  linked_list.head.next.next.next.next.next = Node(6)
  linked_list.head.next.next.next.next.next.next = Node(7)
  linked_list.head.next.next.next.next.next.next.next = Node(8)
  linked_list.head.next.next.next.next.next.next.next.next = Node(9)
  linked_list.head.next.next.next.next.next.next.next.next.next = Node(10)
  linked_list.head.next.next.next.next.next.next.next.next.next.next = Node(11)
  linked_list.head.next.next.next.next.next.next.next.next.next.next.next = loop_start

  # linked_list.traverse()

  loop_start = linked_list.find_loop_begining()
  if loop_start:
    print ('Loop starting node: data[%d], id[%d]' % (
      loop_start.data, id(loop_start)))
  else:
    print ('Loop not found in linked list')


if __name__ == '__main__':
  main()


# Output:
# -------------
# 2 3
# 3 5
# 4 7
# 5 9
# 6 11
# 7 5
# 8 7
# 9 9
# Loop starting node: data[4], id[140707239423080]

# Note that, fast and slow pointers collided at 9 which is k nodes before loop
# start. k is the number of nodes from linked list head to loop starting
# node(4).
