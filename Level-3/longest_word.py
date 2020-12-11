#!/usr/bin/python

# Date: 2020-12-10
#
# Description:
# Given a list of words, write a program to find the longest word made of other
# words in the list.
#
# EXAMPLE:
# Input: [cat, banana, dog, nana, walk, walker, dogwalker]
# Output: dogwalker
#
# Approach:
# Idea is taken from, how to solve this if we were asked to find pair of
# words which makes a other word. Below approach is followed
# - Sort words with respect to length in descending order
# - Fill all words in map, for easy lookup
# - Scan words, starting from longest(W) and try to find if this can be formed
#   using other words. To find this split W at all possible locations calling
#   left and right substrings
# - If left is present in map, recursively check if right is also present in
#   the map
#
# Complexity:
# O(nlogn + L^2) time and O(n) space
# n = number of strings
# L = average length of string

def length_sorted(word):
    return len(word)

def can_build_word(word, is_original, _map):
    if not is_original and word in _map:
        return _map[word]

    for i in range(1, len(word)):
        left = word[:i]
        right = word[i:]
        if left in _map and _map[left] and can_build_word(right, False, _map):
            return True
    _map[word] = False
    return False

def longest_word(words):
    sorted_words = sorted(words, reverse=True, key=length_sorted)
    _map = {}
    for word in sorted_words:
        _map[word] = True

    for word in sorted_words:
        if can_build_word(word, True, _map):
            return word
    return ''

words = [
    'cat',
    'banana',
    'dog',
    'nana',
    'walk',
    'walker',
    'bananadogcatty',
    'dogwalker'
]
assert longest_word(words) == 'dogwalker'
