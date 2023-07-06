# Date: 2020-10-02
#
# Description:
# Find operations required to change a source string(str1) to target(str2).
# Operations allowed are (on source string):
# - Insert a character,
# - Remove a character or
# - Replace a character
#
# Approach:
# Use DP table and fill up using bottom up approach, result will be present
# at last cell of DP table.
#
# Reference:
# https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
#
# Complexity:
# Time: O(mxn)
# Space: O(mxn)


def edit_distance_dp(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Add
                    dp[i - 1][j - 1])  # Replace
    return dp[-1][-1]

assert edit_distance_dp('sunday', 'saturday') == 3
assert edit_distance_dp('sunday', 'sunday') == 0
assert edit_distance_dp('', 'sunday') == 6
assert edit_distance_dp('sunday', '') == 6
