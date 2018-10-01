#!/usr/bin/python

# Date: 2018-09-30
#
# Description:
# Implement prefix trie and perform all basic operations - Insert, Search and
# Delete.
#
# Approach:
# Each node of trie can have max supported alphabets children so we can have a
# array of 26(if only small case chars) whose index can be mapped to 26
# characters. Also we take a flag to store if this node marks an end of word or
# not.
#
# Insert
# ------
# Check if node exist or not, follow its children for next characters in trie
# otherwise add a new node to trie to accommodate new word. When all chars are
# inserted in trie for a word, mark is_end_of_word as True.
#
# Search
# ------
# Similar to insert operation, when we have found whole word, check if end of
# word is set or not, if set whole word exist in trie otherwise not.
#
# Delete
# ------
# Recursive approach followed and nodes deleted in bottom up manner. Lot of
# cases to be handled, explained in delete() below.
#
# Complexity:
# Space to store trie - O(ALPHABET_SET*L*N)
# Insert - O(L)
# Search - O(L)
# Delete - O(L)
#
# ALPHABET_SET - Size of alphabet set, 26 if trie has all lower case chars
# N - Number of words in trie
# L - Length of a word


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

  def insert(self, word):
    """Inserts a new word into trie if not already present."""
    ptr = self.root
    for ch in word:
      index = self._char_to_array_index(ch)

      # If current character is not present in trie at required place, create
      # a new node and point to that node.
      if not ptr.children[index]:
        ptr.children[index] = self.get_new_node()
      ptr = ptr.children[index]

    ptr.is_end_of_word = True

  def search(self, key):
    """Searches for a complete key in trie."""
    ptr = self.root
    for ch in key:
      index = self._char_to_array_index(ch)

      if not ptr.children[index]:
        return False
      ptr = ptr.children[index]

    return ptr.is_end_of_word

  def delete_utils(self, curr_node, key, level, length):
    """Utility function to delete a key from trie.
    
    Args:
      curr_node: Reference to current node.
      key: Key/word to be deleted from trie.
      level: Level till when search is done in trie, root is at level 0.
      length: Length of key.
    """
    if not curr_node:
      print 'Deletion failed, {KEY!r} not found'.format(KEY=key)
      return None

    # We have found key in trie
    if level == length:
      # If this is end of word, mark that false as we have to delete this key
      # so can't be end of word now
      if curr_node.is_end_of_word:
        print '{KEY!r} found, deleting'.format(KEY=key)
        curr_node.is_end_of_word = False

      # If this is a leaf node, have no children - this should be deleted
      return curr_node.is_leaf_node()

    else:  # Search recursively and delete node(s) if required
      index = self._char_to_array_index(key[level])
      if self.delete_utils(curr_node.children[index], key, level + 1, length):
        del curr_node.children[index]  # This is the last node, delete it

        # If current node is not an end of word and it doesn't has any children
        # then this node should be deleted.
        return not curr_node.is_end_of_word and curr_node.is_leaf_node()
 
      return False


  def delete(self, key):
    """Deletes a word/key from trie."""
    if key:
      root = self.root
      return self.delete_utils(root, key, 0, len(key))

def main():
  trie = Trie()

  # Insert in trie
  for word in ['the', 'a', 'there', 'answer', 'any', 'by', 'their']:
    trie.insert(word)

  # Search
  print '\nSearching words...'
  print trie.search('by')  # True
  print trie.search('ans')  # False
  print trie.search('the')  # True
  print trie.search('there')  # True
  print trie.search('abs')  # False
  print trie.search('a')  # True

  # Delete
  print '\nDeleting words...'
  trie.delete('Hello')  # Deletion failed, Hello not found

  trie.delete('by')
  print trie.search('by')  # False

  trie.delete('by')  # Deletion failed, 'by' not found


if __name__ == '__main__':
  main()
