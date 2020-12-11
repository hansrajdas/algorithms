#!/usr/bin/python

# Date: 2020-12-11
#
# Description:
# Given a large text file containing words. Given any two words, find the
# shortest distance (in terms of number of words) between them in the file. If
# the operation will be repeated many times for the same file (but different
# pairs of words), can you optimize solution?
#
# Approach:
# - As we are asked to run this algorithm multiple times, we can keep
#   occurrence of each words in a map
# - Then we need to find closest numbers in 2 list of numbers
#
# Complexity:
# Preprocessing: O(N)
# Finding closest pair: O(A + B)
# N = Number of words
# A, B = Number of occurrences of words


def find_closest(_map, words, word1, word2):
    distance = len(words) - 1
    if word1 not in _map or word2 not in _map:
        raise ValueError('Word(s) not found in list')

    l1 = _map[word1]
    l2 = _map[word2]
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        distance = min(distance, abs(l1[i] - l2[j]))
        if l1[i] > l2[j]:
            j += 1
        else:
            i += 1
    return distance            

def get_word_locations(words):
    _map = {}
    for i in range(len(words)):
        if words[i] not in _map:
            _map[words[i]] = []
        _map[words[i]].append(i)
    return _map

def main():
    words = [
        'cat',
        'bat',
        'hello',
        'hi',
        'abc',
        'hi',
        'last',
        'bat',
    ]
    _map = get_word_locations(words)
    assert find_closest(_map, words, 'bat', 'hi') == 2

if __name__ == '__main__':
    main()
