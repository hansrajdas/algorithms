#!/usr/bin/python

# Date: 2018-08-11
#
# Description:
# Given a boolean expression consisting of the symbols 0 (false), 1 (true),
# & (AND), | (OR), and ^ (XOR), and a desired boolean result value result,
# implement a function to count the number of ways of parenthesizing the
# expression such that it evaluates to result. The expression should be fully
# parenthesized (e.g., (0) ^ (1)) but not extraneously (e.g., (((0)) ^ (1))).
#
# EXAMPLE
# countEval("1^0|0|1", false) -> 2
# countEval("0&0&0&1^1|0", true) -> 10
#
# Approach:
# Split (at each boolean operator) expression recursively into left and right
# sub expressions and calculate total combinations and which resulted as True.
# So if expected is True, we can add this to number of ways other we can
# subtract total true from total to get number of ways to get false. This can be
# done vice versa also.
#
# Complexity:
# n = Number of binary operators in expression
# Expression = 0&0&0&1, expected = 1, n = 3, function calls = 93, ways = 0
# Expression = 0&0&0&1, expected = 0, n = 3, function calls = 93, ways = 5
# Expression = 1^0|0|1, expected = 0, n = 3, function calls = 97, ways = 2
# Expression = 1^0|0|1, expected = 1, n = 3, function calls = 97, ways = 3
# Expression = 0&0&0&1^1|0, expected = 1, n = 5, function calls = 701, ways = 10
# Expression = 0&0&0&1^1|0, expected = 0, n = 5, function calls = 701, ways = 32
#
# Time complexity: O(n), Space: O(n^2), but performance depends on boolean
# expression. How symmetric is boolean expression which can be memoized and used
# later.
#
# Without memoization time complexity would be O(n*4^n)

import collections

def boolToString(boolValue):
  return '#True' if boolValue else '#False'

def characterToBoolean(s):
  return True if s == '1' else False

def countEval(s, result, memo):
  if not len(s):
    return 0
  
  if len(s) == 1:
    return 1 if result == characterToBoolean(s) else 0

  if memo[s + boolToString(result)]:
    return memo[s + boolToString(result)]
  
  ways = 0
  # Split left and right substrings with boolean operators.
  for idx in range(1, len(s), 2):
    booleanOperator = s[idx]
    left = s[:idx]
    right = s[idx + 1:]

    # Evaluate left and right substring for false and true.
    leftTrue = countEval(left, True, memo)
    leftFalse = countEval(left, False, memo)
    rightTrue = countEval(right, True, memo)
    rightFalse = countEval(right, False, memo)

    total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

    # Calculate number of ways we can have true if boolean operator between left
    # and right substring is XOR, AND and OR.
    # For XOR both left and right substring should evaluate to different.
    # For AND both left and right substring should evaluate to True.
    # For OR either left or right should evaluate to True.
    if booleanOperator == '^':
        totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
    elif booleanOperator == '&':
        totalTrue = leftTrue * rightTrue
    elif booleanOperator == '|':
        totalTrue = (leftTrue * rightFalse + leftFalse * rightTrue +
                     leftTrue * rightTrue)
    else:
        totalTrue = 0
        print 'In valid operator: {op}'.format(op=booleanOperator)

    # If expected result is False we can get that from total substrings which
    # evaluated and total substring which evaluated to True.
    subWays = totalTrue if result else total - totalTrue
    ways += subWays
  memo[s + boolToString(result)] = ways
  return ways

def main():
  memo = collections.defaultdict(int)
  s = raw_input('Enter boolean expression: ')
  result = input('Enter expected result (0 or 1): ')
  result = bool(result)
  print 'Number of ways: {ways}'.format(ways=countEval(s, result, memo))

if __name__ == '__main__':
  main()
