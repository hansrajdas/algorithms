#!/usr/bin/python

# Date: 2018-10-01
#
# Description:
# Implement auto suggestion feature using trie.
#
# Approach:
# Starting from root, check if query string is present in trie or not, if not
# no suggestions are possible, otherwise check for all complete words below it
# recursively.
# Keep on incrementing prefix string as we go down the trie. At each node check
# for all 26 possible children characters.
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

  def is_leaf_node(self):
    """
    Checks if node is leaf or not. If a node don't have any children it is a
    leaf node.
    """
    for ch in self.children:
      if ch:
        return False
    return True


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

  def suggestions_rec(self, curr_root, curr_prefix):
    # If current prefix itself is a complete word, print it.
    if curr_root.is_end_of_word:
      print curr_prefix

    # If no children below this node, no more suggestions possible
    if curr_root.is_leaf_node():
      return -1

    # Search for all children below current node for suggestions
    for idx in range(ALPHABET_SIZE):
      if curr_root.children[idx]:
        self.suggestions_rec(curr_root.children[idx],
                             curr_prefix + self._index_to_char(idx))
 
  def print_auto_suggestions(self, query):
    """Prints suggestions for a given query string."""
    print '\nSuggestions for query string {QUERY!r} are:'.format(QUERY=query)

    # Scan query string and search if this is present in trie or not, if this
    # query is not present then can't be any suggestions for given query.
    ptr = self.root
    for ch in query:
      index = self._char_to_array_index(ch)
      if not ptr.children[index]:
        print 'No suggestions found'
        return -1

      ptr = ptr.children[index]

    # Query is present in trie, all complete words below this point would
    # contribute to suggestions for given query.
    self.suggestions_rec(ptr, query)


def main():
  trie = Trie()

  # Insert in trie
  for word in ['the', 'a', 'there', 'answer', 'any', 'by', 'their']:
    trie.insert(word)

  # Auto suggestions
  trie.print_auto_suggestions('th')
  trie.print_auto_suggestions('test')
  trie.print_auto_suggestions('a')


if __name__ == '__main__':
  main()


# Output:
# ----------------
# Suggestions for query string 'th' are:
# the
# their
# there
# 
# Suggestions for query string 'test' are:
# No suggestions found
# 
# Suggestions for query string 'a' are:
# a
# answer
# any
