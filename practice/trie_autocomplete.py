ALPHABET_SIZE = 26

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(ALPHABET_SIZE)]
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, c):
        return ord(c) - ord('a')

    def _index_to_char(self, i):
        return chr(i + ord('a'))

    def insert(self, string):
        ptr = self.root
        for c in string:
            idx = self._char_to_index(c)
            if ptr.children[idx] is None:
                ptr.children[idx] = TrieNode()
            ptr = ptr.children[idx]
        ptr.is_end_of_word = True

    def update_suggestions(self, root, prefix, words):
        if root is None:
            return None
        if root.is_end_of_word:
            print(prefix)
            words.append(prefix)
        for i in range(ALPHABET_SIZE):
            self.update_suggestions(root.children[i], prefix + self._index_to_char(i), words)

    def autocomplete(self, prefix):
        words = []
        ptr = self.root
        for c in prefix:
            idx = self._char_to_index(c)
            if not ptr.children[idx]:
                return []
            ptr = ptr.children[idx]

        self.update_suggestions(ptr, prefix, words)
        return words

    def words_in_sorted_order_util(self, root, word):
        if root is None:
            return None
        if root.is_end_of_word:
            print(word)
        for i in range(ALPHABET_SIZE):
            self.words_in_sorted_order_util(root.children[i], word + self._index_to_char(i))

    def words_in_sorted_order(self):
        self.words_in_sorted_order_util(self.root, '')

    def longest_prefix_matching(self, word):
        ptr = self.root
        longest_matched = ''
        trie_word = ''
        for c in word:
            idx = self._char_to_index(c)
            if ptr.is_end_of_word:
                trie_word = longest_matched
            if not ptr.children[idx]:
                return trie_word
            longest_matched += c
            ptr = ptr.children[idx]
        if ptr.is_end_of_word:
            return longest_matched
        return trie_word

def main():
    trie = Trie()

    for string in ['a', 'abc', 'absent', 'abscond', 'absence', 'cat', 'attribute', 'aaa', 'bat', 'ballon', 'people', 'prank', 'pop']:
        trie.insert(string)

    print(trie.autocomplete('a'))

    print('------------ SORTED ORDER -----------')
    trie.words_in_sorted_order()

    print('------------ LONGEST PREFIX -----------')
    print(trie.longest_prefix_matching('ab'))
    print(trie.longest_prefix_matching('abc'))
    print(trie.longest_prefix_matching('abcdef'))

main()
