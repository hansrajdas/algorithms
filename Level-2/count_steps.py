#!/usr/bin/python2.7

# Date: 2018-07-27
#
# Description:
# A child is running up a staircase with n steps and can hop either 1 step,
# 2 steps or 3 steps at a time. Implement a method to count how many possible
# ways the child can run up the stairs.
#
# Approach:
# Solved using DP bottom-up approach with base cases as if n < 0, ways = 0 and
# if n = 1, ways = 1 otherwise calculate with 3 possibilities that either 1
# step, 2 steps or 3 steps can be taken.
# Memoization used to improve complexity, without memoization complexity would
# be O(3^n).
#
# Complexity:
# O(n)

def ways(n, memo):
  """Counts the number of ways to run n steps (with step size of 1, 2 or 3).
  
  Args:
    n: Number of steps.
    memo: List to store already calculated ways.
  """
  if n < 0:
    return 0
  elif not n:
    return 1
  elif memo[n]:
    return memo[n]
  memo[n] = ways(n - 1, memo) + ways(n - 2, memo) + ways(n - 3, memo)
  return memo[n]

def countWays(n):
  memo = [0 for i in range(n + 1)]
  return ways(n, memo)

def main():
  for n in range(1, 25):
    print 'N = {n}, Ways = {ways}'.format(n = n, ways=countWays(n))

if __name__ == '__main__':
  main()
