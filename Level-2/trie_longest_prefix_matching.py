#!/usr/bin/python

# Date: 2018-10-01
#
# Description:
# Given a dictionary of words and an input string, find the longest prefix of
# the string which is also a word in dictionary. For example, let the
# dictionary contains the following words:
# {are, area, base, cat, cater, children, basement}
#
# Below are some input/output examples:
# --------------------------------------
# Input String            Output
# --------------------------------------
# caterer                 cater
# basemexy                base
# child                   <Empty>
#
# Approach:
# Scan given word with matching characters in trie, if end of word is found,
# keep track of it.
# If there is mismatch between input string and trie, exit and return last
# longest matched word if any.
#
# Complexity:
# O(n), n = length of input string

ALPHABET_SIZE = 26


class TrieNode:
  """Hold data required for a single trie node."""
  def __init__(self):
    """Initializes a new trie node."""
    self.children = [None for i in range(ALPHABET_SIZE)]
    self.is_end_of_word = False


class Trie:
  """Implements trie with all basic operations."""
  def __init__(self):
    """Initializes a new trie."""
    self.root = self.get_new_node();

  def get_new_node(self):
    """Initializes a new trie node."""
    return TrieNode()

  def _char_to_array_index(self, ch):
    """Converts given character to array index of size 26 - between 0 to 25."""
    return ord(ch) - ord('a')

  def _index_to_char(self, index):
    """Converts an array index(0 to 25) to character between a to z."""
    return chr(index + ord('a'))

  def insert(self, word):
    """Inserts a new word into trie if not already present."""
    ptr = self.root
    for ch in word:
      index = self._char_to_array_index(ch)
      # If node for required character not present then create a new node.
      if not ptr.children[index]:
        ptr.children[index] = self.get_new_node()
      ptr = ptr.children[index]

    ptr.is_end_of_word = True

  def longest_prefix_matched(self, string):
    """Returns longest prefix matched in trie for a given string."""
    ptr = self.root
    longest_word_len_matched = None
    matched_chars = 0
    for ch in string:
      index = self._char_to_array_index(ch)
      # A word shorter than string found in trie, update longest word len.
      if ptr.is_end_of_word:
        longest_word_len_matched = matched_chars

      if ptr.children[index]:
        matched_chars += 1
        ptr = ptr.children[index]
      else:
        break
    
    # Check if whole string was scanned and end of word for this node was set,
    # it means whole string passed is present in trie, return actual string.
    # Otherwise if longest word match has some value then some shorter string
    # was found in trie, return that
    if ptr.is_end_of_word and len(string) == matched_chars:
      return string
    elif longest_word_len_matched:
      return string[0:longest_word_len_matched]
    else:
      return None  # No string found in trie having required prefix


def main():
  trie = Trie()

  words = ['are', 'area', 'base', 'cat', 'cater', 'children', 'basement']

  # Insert in trie
  for word in words:
    trie.insert(word)

  print trie.longest_prefix_matched('are')  # are
  print trie.longest_prefix_matched('arex')  # are
  print trie.longest_prefix_matched('caterer')  # cater
  print trie.longest_prefix_matched('basemexy')  # base
  print trie.longest_prefix_matched('child')  # None
  print trie.longest_prefix_matched('basement')  # basement
  print trie.longest_prefix_matched('xyz')  # None


if __name__ == '__main__':
  main()
