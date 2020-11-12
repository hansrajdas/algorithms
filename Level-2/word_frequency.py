#!/usr/bin/python

# Date: 2020-11-12
#
# Description:
# Design a method to find the frequency of occurrneces of any given word in a
# book. What if we were running this algo multiple times.
#
# Approach:
# We can keep word frequencies in a dictionary then check if asked key present
# or not.
#
# Complexity:
# O(n) Time and space(n = Number of words in book)


def get_words_count(words):
    d = {}
    for word in words:
        word = word.lower().strip()
        if word and word not in d:
            d[word] = 0
        d[word] += 1
    return d

def get_word_frequency(words, key):
    if not words:
        return 0
    frequencies = get_words_count(words)

    key = key.lower().strip()
    if key in frequencies:
        return frequencies[key]
    return 0

assert get_word_frequency(['this', 'is', 'sample'], 'Is') == 1
assert get_word_frequency(['this', 'is', 'another', 'sample', 'Is'], 'is') == 2
assert get_word_frequency(['hi', ' hi', 'hi   ', 'hello'], 'Hi') == 3
assert get_word_frequency(['new', 'sample', 'string'], 'new   ') == 1
