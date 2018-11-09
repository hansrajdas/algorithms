#!/usr/bin/python

# Date: 2018-11-09
#
# Description:
# Implementation of LRU cache.
# LRU is least recently used. LRU cache discards cache entries which are not
# accessed in recent times that is which is least recently used.
#
# Approach:
# This can be implemented using a dictionary which keeps reference to keys that
# are cached. And a doubly linked list which keeps cached values based on how
# recently they are accessed.
#
# When we access a cached entry, it is deleted from doubly linked list and moved
# to head.
# When DLL is full(reached cache limit) we remove en entry from DLL tail and
# delete from dictionary also to indicate this entry is no longer cached.
#
# DLL requirement arises from the fact we require insert at head and remove from
# tail as fast as possible.
#
# NOTE:
# This is a sample code NOT a running one. Just to get an idea of implementation
# details.


class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
		self.back = None


class DoublyLinkedList:
	def __init__():
		self.head = None
		self.tail = None
		self.size = 0

	def insertAtHead(key, value):
		node = Node(key, value)
    ...
    self.size += 1
		return newNode

	def removeFromTail(self):
		...
    return tailNode

  def removeFromQ(self, key):
    ...
    return node
	
	def getLen(self):
		return self.size


class LRUCache:
	def __init__(self, size):
		self.cache = {}
		self.Q = DoublyLinkedList()
		self.size = size

  def put(self, key, value):
	  if key in self.cache:
		  self.Q.removeFromQ(key)

	  if self.Q.len == size:
		  node = self.Q.removeFromTail()
		  del self.cache[node.key]
	  node = self.Q.insertAtHead(key, value)
	  self.cache[key] = node

  def get(self, key):
    if key not in self.cache:
      return None
    node = removeFromQ(key)
    node = insertAtHead(node.key, node.value)
    self.cache[key] = node
    return node.value


c = LRUCache(10)
c.put(k, v)
