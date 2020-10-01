# Date: 2020-10-01
#
# Description:
# Given a sentence, reverse it's individual words. For example if sentence is
# "Hello World" it should be changed to "World Hello".
#
# Approach:
# - First, reverse whole string
# - Take individual words from reversed string and reverse them
# - Above 2 steps will result in reversed words in sentence.
#
# Complexity:
# O(N)

def _reverse(l):
    start = 0
    end = len(l) - 1
    while start < end:
        l[start], l[end] = l[end], l[start]
        start += 1
        end -= 1
    return l

def reverse_sentence(sentence):
    if not sentence:
        return sentence
    sentence = list(sentence)
    rev = _reverse(sentence)

    i = 0
    temp = []
    res = []
    while i < len(rev):
        if rev[i] == ' ':
            res.extend(_reverse(temp) + [' '])
            temp = []
        else:
            temp.append(rev[i])
        i += 1
    if temp:
        res.extend(_reverse(temp))
    return ''.join(res)


assert reverse_sentence('hello world') == 'world hello'
assert reverse_sentence('world') == 'world'
