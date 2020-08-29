class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end_of_word = False

    def is_leaf_node(self):
        for ch in self.children:
            if ch:
                return False
        return True

class Trie:
    def __init__(self):
        self.root = self.get_new_node()

    def get_new_node(self):
        return TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, string):
        if not string:
            return None
        print('Inserting %r' % string)
        ptr = self.root
        for c in string:
            idx = self._char_to_index(c)
            if not ptr.children[idx]:
                ptr.children[idx] = self.get_new_node()
            ptr = ptr.children[idx]
        ptr.is_end_of_word = True

    def search(self, key):
        ptr = self.root
        for c in key:
            idx = self._char_to_index(c)
            if not ptr.children[idx]:
                return False
            ptr = ptr.children[idx]
        return ptr.is_end_of_word

    def delete_util(self, curr_node, key, level, length):
        if not curr_node:
            print('%r not found' % key)
            return None
        if level == length:  # Trversed till length of key
            if curr_node.is_end_of_word:  # Node matched
                print('%r found, deleting' % key)
                curr_node.is_end_of_word = False
            return curr_node.is_leaf_node()
        idx = self._char_to_index(key[level])
        if self.delete_util(curr_node.children[idx], key, level + 1, length):
            del curr_node.children[idx]
        return not curr_node.is_end_of_word and curr_node.is_leaf_node() 

    def delete(self, key):
        if self.root:
            self.delete_util(self.root, key, 0, len(key))

def main():
    trie = Trie()
    for word in ['the', 'a', 'there', 'answer', 'any', 'by', 'their', 'some']:
        trie.insert(word)

    for s in ['any', 'anyone', 'th', 'there', 'something', 'some']:
        print(s, '->', trie.search(s))

    # Delete
    print('\nDeleting words...')
    trie.delete('Hello')  # Deletion failed, Hello not found

    trie.delete('by')
    print(trie.search('by'))  # False

    trie.delete('by')  # Deletion failed, 'by' not found

if __name__ == '__main__':
    main()
