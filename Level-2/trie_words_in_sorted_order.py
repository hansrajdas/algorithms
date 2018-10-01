#!/usr/bin/python

# Date: 2018-10-01
#
# Description:
# Using trie, print set of words in sorted order.
#
# Approach:
# Starting from root, used DFS approach to find complete words. Sorted order is
# guaranteed by scanning each node's children from left(a) to right(z). If node
# has a children present, prefix string is updated and called same function
# recursively.
#
# Complexity:
# O(ALPHABET_SIZE*N*L)
#
# ALPHABET_SET - Size of alphabet set, 26 if trie has all lower case chars
# N - Number of words in trie
# L - Average length word


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

  def words_in_sorted_order_utils(self, p_root, prefix=None):
    """Recursively, prints all words present in trie, in sorted order."""
    if p_root.is_end_of_word:
      print prefix

    # Check for all children in order - 0-25/a-z. It will automatically take
    # care of sorted order.
    for index in range(ALPHABET_SIZE):
      if p_root.children[index]:
        ch = self._index_to_char(index)
        # If this is a new starting(prefix not initialized yet for this) of
        # word, pass this first word to function as prefix otherwise add this
        # new character to prefix string.
        if prefix:
          self.words_in_sorted_order_utils(p_root.children[index], prefix + ch)
        else:
          self.words_in_sorted_order_utils(p_root.children[index], ch)

  def words_in_sorted_order(self):
    """Prints all words present in trie, in sorted order."""
    print 'Words in sorted order:'
    self.words_in_sorted_order_utils(self.root)


def main():
  trie = Trie()

  words = [
    'the', 'a', 'there', 'aa', 'ab', 'aab', 'any', 'by', 'their', 'abb'
  ]

  # Insert in trie
  for word in words:
    trie.insert(word)

  trie.words_in_sorted_order()


if __name__ == '__main__':
  main()


# Output:
# ----------------
# Words in sorted order:
# a
# aa
# aab
# ab
# abb
# any
# by
# the
# their
# there
