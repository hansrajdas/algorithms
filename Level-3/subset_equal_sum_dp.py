#!/usr/bin/python

"""
Date: 2019-01-29

Description:
Determine whether a given set can be partitioned into two subsets such that
the sum of elements in both subsets is same.

Approach:
- Top down
  - Check all possibilities - if we are able to sum(A) // 2 by checking all
    possibilities to take a number or skip that number.
  - Use caching to save results so that it can be reused later.
- Bottom up
  - If sum of all elements in list comes out to be odd, then it is not possible
    to partition list in 2 subsets having same sum
  - We can use DP(bottom up) approach to solve the problem, similar to solve
    knapsack problem. We can take a 2D array of size (sum/2 + 1)*(n + 1) and
    fill this array using bottom up approach, see comments in program.
  - Above approach becomes inefficient when n is smaller and sum is very large, we
    waste a lot of memory. In those cases we can use recursion to check all
    combinations - At each element we will have 2 conditions whether to take this
    element or not.

Reference:
https://leetcode.com/problems/partition-equal-subset-sum/
https://www.geeksforgeeks.org/partition-problem-dp-18/

Complexity:
O(N*SUM), this is pseudo-polynomial
"""

def setWithEqualSumTopDown(A):
    S = sum(A)
    if S % 2:
        return False
    cache = {}
    def isSum(idx, remSum):
        if remSum == 0:
            return True
        if idx == len(A) or remSum < 0:
            return False
        if (idx, remSum) in cache:
            return cache[(idx, remSum)]
        cache[(idx, remSum)] = isSum(idx + 1, remSum) or isSum(idx + 1, remSum - A[idx])
        return cache[(idx, remSum)]
    return isSum(0, S // 2)

def setWithEqualSumBottomUp(A):
  """
  Returns True is list A can be divided in 2 subsets having equal sum other
  False.
  """
  if not A:
    return True

  n = len(A)
  s = sum(A)

  # A can be divided in 2 subsets only if total sum is even otherwise it's not
  # possible to divide array having equal sum.
  if s % 2:
    return False

  # Create a matrix of size - (sum/2 + 1)*(n + 1)
  # dp[i][j] = true if a subset of {arr[0], arr[1], ..arr[j-1]} has sum equal to
  # i, otherwise false
  half_sum = s // 2
  dp = [[None]*(n + 1) for _ in range(half_sum + 1)]

  # Initialize top row as true as sum of 0 is always possible with any subset of
  # numbers - using empty set
  for i in range(n + 1):
    dp[0][i] = True

  # Initialize leftmost column, except part[0][0], as no positive sum is
  # possible with 0 elements
  for i in range(1, half_sum + 1):
    dp[i][0] = False

  # Update matrix using bottom up approach
  for i in range(1, half_sum + 1):
    for j in range(1, n + 1):

      # If sum i is possible with subset of element from A[0..j-2] then same sum
      # is also possible with subsets of elements from A[0..j-1]
      dp[i][j] = dp[i][j - 1]

      # In case d[i][j] comes to be false and current element is less than
      # running sum, we can assign value which was at sum = without current
      # element
      if i >= A[j-1] and (not dp[i][j]):
        dp[i][j] = dp[i - A[j-1]][j - 1]

  return dp[half_sum][n]



assert setWithEqualSumTopDown([3, 1, 1, 2, 2, 1]) == True  # 3,1,1 == 2,2,1
assert setWithEqualSumTopDown([3, 1, 1, 2, 2, 10]) == False
assert setWithEqualSumTopDown([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == True
assert setWithEqualSumTopDown([1, 2, 3, 4, 5, 6, 7]) == True
assert setWithEqualSumTopDown([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == True
assert setWithEqualSumTopDown([1, 10, 5, 21, 4]) == False
assert setWithEqualSumTopDown([1, 10, 5, 21, 4, 1]) == True

assert setWithEqualSumBottomUp([3, 1, 1, 2, 2, 1]) == True  # 3,1,1 == 2,2,1
assert setWithEqualSumBottomUp([3, 1, 1, 2, 2, 10]) == False
assert setWithEqualSumBottomUp([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == True
assert setWithEqualSumBottomUp([1, 2, 3, 4, 5, 6, 7]) == True
assert setWithEqualSumBottomUp([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == True
assert setWithEqualSumBottomUp([1, 10, 5, 21, 4]) == False
assert setWithEqualSumBottomUp([1, 10, 5, 21, 4, 1]) == True
