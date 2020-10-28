#!/usr/bin/python

# Date: 2018-08-04
#
# Description:
# Implement an algorithm to print all valid (i.e properly opened and closed)
# combinations of n pairs of parentheses.
# Example:
# Input: 3
# Output: ((())), (()()), (())(), ()(()), ()()()
#
# Approach:
# List of possible valid parens for any number, n can be generated with list of
# parens with n = n - 1. So we can follow recursive approach to build this list
# with any n. Suppose we have list of parens for n = n - 1 called SOLUTION so
# for n = n we can generate by adding parens to the left, right and enclosing
# to each item of SOLUTION: () + SOLUTION, (SOLUTION) + SOLUTION + ().
# One exception in this for simple parens - ()()()...() we just have to add ()
# to the left or right otherwise it will give us repeated result as:
# ()...() + '()' will be same as '()' + ()...()
# For example:
# n = 1 => ()
# n = 2 => ()(), (())
# n = 3 => Use above results:
# ()() => Adding enclosing and left => ()()(), (()())
# (()) => Adding enclosing, left and right => ((())), ()(()), (())()
#
# Complexity:
# Around O(n * n!)

def generatePairOfParens(n):
  if n == 1:
    return ['()']
  parens = generatePairOfParens(n - 1)
  newParensPairs = []
  for idx in range(len(parens)):
    newParensPairs.append('()' + parens[idx])
    newParensPairs.append('(' + parens[idx] + ')')

    # Symmetric parens(list of open/close parens '()()...()') is stored at 0th
    # index we should not add '()' at the end of this pair otherwise we would
    # get repeated entries i.e '()' + ()() will be same as ()() + '()' so
    # skipping first index while suffixing '()', only prefixed in this case.
    if idx:
      newParensPairs.append(parens[idx] + '()')
  return newParensPairs

def main():
  n = input("Enter number: ")
  try:
    n = int(n)
  except ValueError:
    print('Invalid input')
    return
  parens = generatePairOfParens(int(n))
  for idx in range(len(parens)):
    print('{idx}: {parens}'.format(idx=idx + 1, parens=parens[idx]))

if __name__ == '__main__':
  main()

# Output:
#
# Enter input string: 1
# 1: ()
#
# Enter input string: 2
# 1: ()()
# 2: (())
#
# Enter input string: 3
# 1: ()()()
# 2: (()())
# 3: ()(())
# 4: ((()))
# 5: (())()
#
# Enter input string: 4
# 1: ()()()()
# 2: (()()())
# 3: ()(()())
# 4: ((()()))
# 5: (()())()
# 6: ()()(())
# 7: (()(()))
# 8: ()(())()
# 9: ()((()))
# 10: (((())))
# 11: ((()))()
# 12: ()(())()
# 13: ((())())
# 14: (())()()
