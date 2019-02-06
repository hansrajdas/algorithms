#!/usr/bin/python

# Date: 2019-02-06
#
# Description:
# Given a rope of length n meters, cut the rope in different parts of integer
# lengths in a way that maximizes product of lengths of all parts.
#
# Approach:
# Consider all combinations and keep track of max product. For considering
# all combinations there will be lot of repeated work(as seen in recursion tree),
# we can memoize all those repeated work so that we don't have to compute max
# product for any number which is already calculated.
#
# For example if n = 3, we will consider all combinations like:
# 3 = 1*2, 2*1, 1*1*1
#
# Problem description:
# https://www.geeksforgeeks.org/maximum-product-cutting-dp-36/
#
# Complexity:
# O(N^2) time and O(N) space
# N for recursion and for each call to function with new N and loop runs from
# 2 to N - 1 hence overall complexity comes out to be N^2

def getMaxProduct(n, memo):
  if n < 3:
    return 1
  if n in memo:
    return memo[n]
  max_product = 0
  for first_num in range(2, n):
    max_product = max(
      max_product,
      first_num*(n - first_num),  # product with this partition of n
      getMaxProduct(n - first_num, memo)*first_num)
  memo[n] = max_product
  return max_product

# Main
print getMaxProduct(2, {})  # 1 -> 1*1
print getMaxProduct(3, {})  # 2 -> 1*2
print getMaxProduct(4, {})  # 4 -> 2*2
print getMaxProduct(5, {})  # 6 -> 2*3
print getMaxProduct(10, {})  # 36 -> 3*3*4
print getMaxProduct(50, {})  # 86093442
