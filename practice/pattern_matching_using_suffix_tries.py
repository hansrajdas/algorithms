char_set = 256

class SuffixTrieNode:
    def __init__(self):
        self.children = [None for _ in range(char_set)]
        self.indices = []

    def insert_suffix(self, suffix, index):
        self.indices.append(index)
        if not suffix:
            return None
        i = ord(suffix[0])
        if not self.children[i]:
            self.children[i] = SuffixTrieNode()
        self.children[i].insert_suffix(suffix[1:], index + 1)

    def search(self, pattern):
        if not len(pattern):
            return self.indices
        c = pattern[0]
        if not self.children[ord(c)]:
            return []
        return self.children[ord(c)].search(pattern[1:])

class SuffixTrie:
    def __init__(self):
        self.root = SuffixTrieNode()

    def insert(self, text):
        for i in range(len(text)):
            self.root.insert_suffix(text[i:], i)

    def search(self, pattern):
        indices = self.root.search(pattern)
        if not indices:
            print('Pattern %r not found in suffix trie' % pattern)
            return None
        print('Pattern %r found at indice(s): %s' % (
            pattern, ', '.join(str(i - len(pattern)) for i in indices)))

def main():
    suffix_trie = SuffixTrie()

    suffix_trie.insert('Hello world')

    suffix_trie.search(' world')
    suffix_trie.search('llo world')
    suffix_trie.search('Hello world')
    suffix_trie.search('Hello')
    suffix_trie.search('world')
    suffix_trie.search('l')

    suffix_trie.search('world ')
    suffix_trie.search('world Hello')
    suffix_trie.search(' Hello')
    suffix_trie.search('hello')
    suffix_trie.search('Wello')

main()
