#!/usr/bin/python

# Date: 2020-08-14
# 
# Description:
# Rabin karp algo to find all occurrences of a pattern string from a large text
# string.
# 
# Approach:
# Idea behind rabin karp is a rolling hash is used which can be used to
# compute new hash from existing hash when a new character is added at end and
# an existing character is removed from beginning.
# 
# Reference:
# http://www-igm.univ-mlv.fr/~lecroq/string/node5.html#SECTION0050
# 
# Complexity:
# Space: O(1)
# Time: Average case - O(n + m), Worst case - O(m*(n-m))

def rehash(prev_hash, first, last, d):
    """Returns new hash if first char removed and last char is added."""
    return ((prev_hash - ord(first) * d) << 1) + ord(last)

def rabin_karp(txt, pat):
    """Returns list of indices in text string which matches given pattern."""
    matches = []
    hy = 0  # Hash of running text frame
    hx = 0  # Hash of pattern
    n = len(txt)
    m = len(pat)

    if m > n:
        return []

    d = 1 << m - 1

    for i in range(m):
        hx = (hx << 1) + ord(pat[i])
        hy = (hy << 1) + ord(txt[i])

    # Search
    j = 0
    while j <= n - m:
        if hx == hy and pat == txt[j:j + m]:
            matches.append(j)
        if j < n - m:
            hy = rehash(hy, txt[j], txt[j + m], d)
        j += 1
    return matches

assert rabin_karp('THIS IS A TEST TEXT', 'TEST') == [10]
assert rabin_karp('AABAACAADAABAABA', 'AABA') == [0, 9, 12]
assert rabin_karp('AAAAABAAABA', 'AAAA') == [0, 1]
assert rabin_karp('ABABDABACDABABCABAB', 'ABABCABAB') == [10]
