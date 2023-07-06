# Date: 2020-10-02
#
# Description:
# Find operations required to change a source string(str1) to target(str2).
# Operations allowed are (on source string):
# - Insert a character 
# - Remove a character or
# - Replace a character
#
# Approach:
# Check all possible combinations by recursively generating and take min
#
# Reference:
# https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
#
# Complexity:
# Time: O(3^m)


def min_edit_distance(word1, word2):
    cache = {}
    def _min_edit_distance(i, j):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        if (i, j) in cache:
            return cache[(i, j)]
        if word1[i] == word2[j]:
            cache[(i, j)] = _min_edit_distance(i + 1, j + 1)
        else:
            cache[(i, j)] = 1 + min(
                _min_edit_distance(i + 1, j),     # Delete
                _min_edit_distance(i, j + 1),     # Insert
                _min_edit_distance(i + 1, j + 1)  # Replace
                )
        return cache[(i, j)]
    return _min_edit_distance(0, 0)

assert min_edit_distance('abc', 'abc') == 0
assert min_edit_distance('abc', 'ac') == 1
assert min_edit_distance('sunday', 'saturday') == 3
