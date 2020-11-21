#!/usr/bin/python

# Date: 2020-11-21
#
# Description:
# Design and build a "least recently used" cache, which evicts the least
# recently used item. The cache should map from keys to values(allowing you to
# insert and retrieve a value associated with a particular key) and be
# initialized with a max size. When it is full, it should evict the least
# recently used item.
#
# Approach:
# - To get an item is constant time, we need a map
# - To maintain order, which item was used least recently we need a list so we
#   can use doubly linked list as we has to keep to most and least recently
#   items
# - If a key is accessed, it should be moved to head - indicate this item has
#   been accessed most recently
# - When cache is full, we will remove item from tail
#
# Complexity:
# O(1) for get, set and delete key


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class Cache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.map = {}
        self.head = None
        self.tail = None

    def get_value(self, key):
        if key not in self.map:
            return None
        item = self.map[key]
        if item != self.head:
            self.remove_from_linked_list(item)
            self.insert_at_head_of_linked_list(item)
        return item.value

    def remove_from_linked_list(self, node):
        if node is None:
            return
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        if self.tail == node:
            self.tail = node.prev
        if self.head == node:
            self.head = node.next

    def insert_at_head_of_linked_list(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def remove_key(self, key):
        item = self.map.pop(key, None)
        self.remove_from_linked_list(item)

    def set_key_value(self, key, value):
        self.remove_key(key)  # Remove if key is already present

        # If cache is full, remove from tail - least recently used
        if len(self.map) >= self.max_size and self.tail is not None:
            self.remove_key(self.tail.key)

        # Insert new item
        node = DoublyLinkedListNode(key, value)
        self.insert_at_head_of_linked_list(node)
        self.map[key] = node

def main():
    cache = Cache(5)

    for i in range(10):
        cache.set_key_value(i, i * 10)
        print(cache.get_value(i))

if __name__ == '__main__':
    main()
