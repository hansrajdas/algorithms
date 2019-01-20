#!/usr/bin/python2.7

# Date: 2019-01-20
#
# Description:
# Given a singly linked list, write a function to swap elements pairwise.
# For example, if the linked list is 1->2->3->4->5->6->7 then the function
# should change it to 2->1->4->3->6->5->7
#
# Approach:
# Take 3 pointers prev, current and next to track nodes and alter pointers such
# nodes gets swapped and prev.next points to next.next
#
# Reference:
# https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list-by-changing-links/
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

  def print_list(self):
    p = self.head
    while p:
      print p.data,
      p = p.next

  def insert_at_end(self, data):
    node = Node(data)
    if not self.head:
      self.head = node
      return
    p = self.head
    while p.next:
      p = p.next
    p.next = node

  def pairwise_swap(self):
    """Alters the linked list with adjacent linked list elements swapped."""
    if self.head is None or self.head.next is None:
      return
    new_head = self.head.next
    prev = self.head
    current = self.head.next
    while True:
      nxt = current.next
      current.next = prev
      if nxt is None or nxt.next is None:
        prev.next = nxt
        break
      prev.next = nxt.next
      prev = nxt
      current = nxt.next
    self.head = new_head

def main():
  linked_list = LinkedList()
  for i in range(10):
    linked_list.insert_at_end(i)
  linked_list.print_list()  # 0 1 2 3 4 5 6 7 8 9

  print '\nAfter swapping adjacent elements:'
  linked_list.pairwise_swap()
  linked_list.print_list()  # 1 0 3 2 5 4 7 6 9 8

  print '\n****************'
  linked_list = LinkedList()
  for i in range(5):
    linked_list.insert_at_end(i)
  linked_list.print_list()  # 0 1 2 3 4

  print '\nAfter swapping adjacent elements:'
  linked_list.pairwise_swap()
  linked_list.print_list()  # 1 0 3 2 4

if __name__ == '__main__':
  main()
