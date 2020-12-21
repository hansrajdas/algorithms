#!/usr/bin/python

# Date: 2020-12-21
#
# Description:
# Given a string b and an array of smaller strings T, design a method to search
# b for each small string in T.
#
# Approach:
# - Build a trie and store all suffixes of bigger string in it - takes O(b^2)
# - Search for all smaller strings in trie, save all indexes that match
#
# Complexity:
# O(b^2 + kt)
# b = Length of bigger string
# t = Number of smaller strings in T
# k = Length of longest string in T

class TrieNode:
    def __init__(self):
        self.children = {}  # Char to TrieNode
        self.indexes = []

    def insert_string(self, s, index):
        self.indexes.append(index)
        if len(s) == 0:
            return
        value = s[0]
        if value in self.children:
            child = self.children[value]
        else:
            child = TrieNode()
            self.children[value] = child
        child.insert_string(s[1:], index + 1)

    def search(self, s):
        if len(s) == 0:
            return self.indexes
        value = s[0]
        if value in self.children:
            child = self.children[value]
            return child.search(s[1:])
        return []
 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, s, index):
        self.root.insert_string(s, index)

    def search(self, s):
        return self.root.search(s)
    
def create_trie_from_string(s):
    trie = Trie()
    for i in range(len(s)):
        suffix = s[i:]
        trie.insert_string(suffix, i)
    return trie

def substract_value(locations, delta):
    for i in range(len(locations)):
        locations[i] = locations[i] - delta

def search_all(big, smalls):
    lookup = {}  # string to locations
    tree = create_trie_from_string(big)

    for small in smalls:
        locations = tree.search(small)
        substract_value(locations, len(small))
        lookup[small] = locations
    return lookup

def main():
    b = 'mississippi'
    T = ['is', 'ppi', 'hi', 'sis', 'i', 'ssippi']

    print(search_all(b, T))

if __name__ == '__main__':
    main()
