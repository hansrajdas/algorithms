#!/usr/bin/python

# Date: 2020-12-21
#
# Description:
# Given a string b and an array of smaller strings T, design a method to search
# b for each small string in T.
#
# Approach:
# - Store all smaller strings in trie
# - Search all prefix of bigger string in above trie and keep on adding to list
#   which all prefix, we have found
#
# Complexity:
# O(kt + bk)
# b = Length of bigger string
# t = Number of smaller strings in T
# k = Length of longest string in T

class TrieNode:
    def __init__(self):
        self.children = {}
        self.indexes = []

    def insert_string(self, string, index):
        self.indexes.append(index)
        if len(string) == 0:
            self.children['EOW'] = None  # Mark end of word
            return None
        c = string[0]
        if c in self.children:
            child = self.children[c]
        else:
            child = TrieNode()
            self.children[c] = child
        child.insert_string(string[1:], index + 1)

    def get_child(self, c):
        return self.children.get(c)

    def terminates(self):
        return 'EOW' in self.children

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, s, index):
        self.root.insert_string(s, index)

    def get_root(self):
        return self.root

def create_tree_from_string(smalls, max_len):
    tree = Trie()
    for s in smalls:
        if len(s) <= max_len:
            tree.insert_string(s, 0)
    return tree

def find_string_at_location(root, big, start):
    strings = []
    index = start
    while index < len(big):
        root = root.get_child(big[index])
        if root is None:
            break
        if root.terminates():
            strings.append(big[start:index + 1])
        index += 1
    return strings

def insert_into_hash_map(lookup, strings, index):
    for s in strings:
        if s not in lookup:
            lookup[s] = []
        lookup[s].append(index)

def search_all(big, smalls):
    lookup = {}
    max_len = len(big)
    tree = create_tree_from_string(smalls, max_len)
    root = tree.get_root()
    for i in range(max_len):
        strings = find_string_at_location(root, big, i)
        insert_into_hash_map(lookup, strings, i)
    return lookup

def main():
    b = 'mississippi'
    T = ['is', 'ppi', 'hi', 'sis', 'i', 'ssippi']

    print(search_all(b, T))

if __name__ == '__main__':
    main()
