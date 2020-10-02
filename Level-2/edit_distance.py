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


def _min_edit_distance(s1, s2, i, j):
    if i == len(s1) - 1:
        return len(s2) - j - 1
    if j == len(s2) - 1:
        return len(s1) - i - 1
    if s1[i] == s2[j]:
        return _min_edit_distance(s1, s2, i + 1, j + 1)
    return 1 + min(
        _min_edit_distance(s1, s2, i + 1, j + 1),  # Replace
        _min_edit_distance(s1, s2, i + 1, j),  # Add
        _min_edit_distance(s1, s2, i, j + 1)  # Delete
    )

def min_edit_distance(s1, s2):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    return _min_edit_distance(s1, s2, 0, 0)

assert min_edit_distance('abc', 'abc') == 0
assert min_edit_distance('abc', 'ac') == 1
assert min_edit_distance('sunday', 'saturday') == 3
