#!/usr/bin/python

# Date: 2018-10-01
#
# Description:
# Pattern matching using suffix tries.
#
# Approach:
# The idea is, every pattern that is present in text (or we can say every
# substring of text) must be a prefix of one of all possible suffixes. So if we
# build a Trie of all suffixes, we can find the pattern in O(m) time where m is
# pattern length.
# For a text string of size n, there would be n possible substrings(suffix
# strings) possible, we would insert all these suffix strings in trie with
# indexes.
#
# While searching we will consider searching in all suffix strings as any
# pattern would be suffix of text string.
#
# References:
# https://www.geeksforgeeks.org/pattern-searching-using-trie-suffixes/
# https://www.geeksforgeeks.org/pattern-searching-using-suffix-tree/
#
# Complexity:
# O(m), m = length of pattern string


ALPHABET_SIZE = 256


class SuffixTrieNode:
  """Holds data and methods required for a single suffix tree node."""
  def __init__(self):
    """Initializes a suffix trie node."""
    self.children = [None for i in range(ALPHABET_SIZE)]
    self.indexes = []

  def insert_suffix(self, suffix, index):
    """
    Inserts suffix string into suffix trie, rooted with node with which this
    function is called.

    Args:
      suffix: Suffix string.
      index: Index of first character in original string.
    """
    self.indexes.append(index)

    # If string has more characters to be inserted in suffix trie.
    if len(suffix):
      first = ord(suffix[0])
      if self.children[first] is None:
        self.children[first] = SuffixTrieNode()

      # Recur for next suffix
      self.children[first].insert_suffix(suffix[1:], index + 1)

  def search(self, pattern):
    """
    Recursively searches for pattern string in suffix trie rooted with
    current/called node.

    Args:
      pattern: Pattern string to be searched.
    """

    # If all characters in pattern is processed, return.
    if not len(pattern):
      return self.indexes

    # If there is an edge from current node in suffix trie, follow that.
    if self.children[ord(pattern[0])]:
      return self.children[ord(pattern[0])].search(pattern[1:])
    else:
      return None  # No edge from current node, pattern doesn't exist in text


class SuffixTrie:
  """Implements insert and search functionality in suffix trie."""
  def __init__(self, text):
    """Initializes and builds a trie of suffixes for given test string."""
    self.root = SuffixTrieNode()

    # Consider inserting all n suffixes(T[0] to T[n-1], T[1] to T[n-1], ...
    # T[n-1] to T[n-1]) of text in suffix trie.
    for i in range(len(text)):
      self.root.insert_suffix(text[i:], i)

  def search(self, pattern):
    """Prints all occurrences of pattern in suffix trie."""

    # Get list of indexes where pattern is present in text.
    indexes = self.root.search(pattern)  # search() of SuffixTrieNode

    if indexes is None:
      print 'Pattern {PAT!r} not found'.format(PAT=pattern)
    else:
      for idx in indexes:
        print 'Pattern {PAT!r} found at position: {POS}'.format(
          PAT=pattern, POS=(idx - len(pattern)))


def main():
  suffix_trie = SuffixTrie('geeksforgeeks.org')
  suffix_trie.search('ee')
  suffix_trie.search('geek')
  suffix_trie.search('quiz')
  suffix_trie.search('forgeeks')


if __name__ == '__main__':
  main()
