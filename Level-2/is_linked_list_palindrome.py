#!/usr/bin/python

# Date: 2018-09-19
#
# Description:
# Implement a function to check if a linked list is a palindrome.
#
# Approach:
# 1. Push all first half elements to stack.
# 2. Pop each element from stack and compare it with elements in second half
#    of linked list in sequence.
#
# Complexity:
# O(n) time and space


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
            print ('%d->' % node.data),
            node = node.next

        print ('None')

    def is_linked_list_palindrome(self):
      """Checks if a linked list is palindrome or not."""
      slow = self.head
      fast = self.head
      stack = []
      while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

      # If list had odd number of elements, we don't have to compare the middle
      # element.
      if fast:
        slow = slow.next

      # Compare stack elements and second half of linked list.
      while stack:
        if slow.data != stack.pop():
          return False
        slow = slow.next
      return True


linked_list = LinkedList()
n = input('Enter number: ')
for d in str(n):
  linked_list.add_node_at_end(int(d))

linked_list.list_print()

if linked_list.is_linked_list_palindrome():
  print ('YES')
else:
  print ('NO')


# Output:
# -------
# Enter number: 123243454
# 1-> 2-> 3-> 2-> 4-> 3-> 4-> 5-> 4-> None
# NO

# Enter number: 1331
# 1-> 3-> 3-> 1-> None
# YES

# Enter number: 131
# 1-> 3-> 1-> None
# YES

# Enter number: 1
# 1-> None
# YES

# Enter number: 12
# 1-> 2-> None
# NO

# Enter number: 10
# 1-> 0-> None
# NO

# Enter number: 101
# 1-> 0-> 1-> None
# YES
