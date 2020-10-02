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


def edit_distance_dp(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    dp = [[None] * (n2 + 1) for _ in range(n1 + 1)]

    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if not i:
                dp[i][j] = j
            elif not j:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],  # Add
                    dp[i - 1][j],  # Delete
                    dp[i - 1][j - 1]  # Replace
                )
    return dp[n1][n2]


assert edit_distance_dp('sunday', 'saturday') == 3
assert edit_distance_dp('sunday', 'sunday') == 0
assert edit_distance_dp('', 'sunday') == 6
assert edit_distance_dp('sunday', '') == 6
