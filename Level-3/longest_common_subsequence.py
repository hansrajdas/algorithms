#!/usr/bin/python

# Date: 2019-01-27
#
# Description:
# Given two sequences, find the length of longest subsequence present in both
# of them. A subsequence is a sequence that appears in the same relative order,
# but not necessarily contiguous.
# For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of
# “abcdefg”.
#
# Approach:
# - A string of length n can have 2^n susequences which can be compared with
#   other string. This solution will take O(2^n) time.
# - Another approach would be to use matrix of size (M + 1)*(N + 1) and use
#   bottom up approach to fill that matrix. One dimension of matrix corresponds
#   to one string and another approach to other string. This approach is similar
#   to knapsack approach. Max LCS length is stored in matrix[M][N].
#
# Reference:
# https://www.youtube.com/watch?v=NnD96abizww
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
#
# Complexity:
# O(M*N) Time and space

def longest_common_subsequence(str1, str2):
  m = len(str1)
  n = len(str2)

  # Treat m as rows of dp matrix and n as cols
  dp = [[None]*(n + 1) for _ in range(m + 1)]

  for i in range(m + 1):
    for j in range(n + 1):
      if not i or not j:  # Base, if length of either string is 0 then lcs=0
        dp[i][j] = 0
      elif str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # Max of adjacent row or col
  return dp[m][n]

# Test
assert longest_common_subsequence("AGGTAB", "GXTXAYB") == 4
assert longest_common_subsequence("ABCDGH", "AEDFHR") == 3
