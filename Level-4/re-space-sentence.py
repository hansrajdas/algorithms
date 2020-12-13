#!/usr/bin/python

# Date: 2020-12-13
#
# Description:
# Oh, no! You have accidentally removed all spaces, punctuation, and
# capitalization in a lengthy document. A sentence like "I reset the computer.
# It s till didn't boot!" became 'iresetthecomputeritstilldidntboot': You'll
# deal with the punctuation and capitalization later; right now you need to
# re-insert the spaces. Most of the words are in a dictionary but a few are
# not. Given a dictionary (a list of strings) and the document (a string)
# design an algorithm to unconcatenate the document in a way that minimizes
# the number of unrecognized characters.
#
# EXAMPLE:
# Input jesslookedjustliketimherbrother
# Output: jess looked just like tim her brother (7 unrecognized characters)
#
# Approach:
# We will consider adding space at each location and check which gives best
# result (min unrecognized chars)
# - Recursive approach with memoization if followed
#
# Note: Check CTCI problem 17.13 for explanation
#
# Complexity:
# O(N^2)


class ParseResult:
    def __init__(self, inv, string):
        self.invalid = inv
        self.parsed = string

def split(dictionary, sentence, start, memo):
    if start >= len(sentence):
        return ParseResult(0, '')
    if memo[start] is not None:
        return memo[start]
    partial = ''
    best_invalid = len(sentence)
    best_parsing = None
    index = start
    while index < len(sentence):
        partial += sentence[index]
        invalid = 0 if partial in dictionary else len(partial)
        if invalid < best_invalid:
            res = split(dictionary, sentence, index + 1, memo)
            if res.invalid + invalid < best_invalid:
                best_invalid = res.invalid + invalid
                best_parsing = partial + ' ' + res.parsed
                if best_invalid == 0:
                    break
        index += 1
    memo[start] = ParseResult(best_invalid, best_parsing)
    return memo[start]

def best_split(dictionary, sentence):
    memo = [None for _ in range(len(sentence))]
    r = split(dictionary , sentence, 0, memo)
    return None if r is None else r.parsed

def main():
    dictionary = set([
        'the', 'is', 'looked', 'like', 'her', 'awesome', 'just', 'brother',
        'this', 'makes', 'food'
    ])
    # Case: 1
    sentence = 'thisisawesome'
    string = best_split(dictionary, sentence)
    print(string)

    # Case: 2
    sentence = 'jesslookedjustliketimherbrother'
    string = best_split(dictionary, sentence)
    print(string)

if __name__ == '__main__':
    main()
