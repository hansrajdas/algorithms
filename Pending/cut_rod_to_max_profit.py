#!/usr/bin/python

# Date: 2018-08-02
#
# Description:
# Given a rod of length n inches and an array of prices that contains prices of
# all pieces of size smaller than n. Determine the maximum value obtainable by
# cutting up the rod and selling the pieces.
#
# Approach:
# 
#
# Problem description:
# https://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/
#
# Complexity:
# O(n^2)

def max_profit(prices, n, memo):
  """Returns max profit that can be achieved by cutting a rod optimally.

  Args:
    prices: List having prices corresponding to given rod length.
    n: Length of rod.
  """
  if not n:
    return 0
  if n in memo:
    return memo[n]
  max_price = prices[n - 1]
  for first_half_len in range(1, n):
    max_price = max(
        max_price,
        max_profit(prices, first_half_len, memo) + max_profit(prices, n - first_half_len, memo))
  memo[n] = max_price
  return memo[n]


print max_profit([1, 5, 8, 9, 10, 17, 17, 20], 8, {})  # 22 -> 5*2 + 17*6

print max_profit([3, 5, 8, 9, 10, 17, 17, 20], 8, {})  # 24 ->  3*8

print max_profit(range(50), 50, {})  # 49
