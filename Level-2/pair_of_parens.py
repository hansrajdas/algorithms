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
# On each recursive call, we have the index for a particular in the string. We
# need to select either a left or right paren.
# - We will use left paren, as long as we haven't used up all the left
#   parenthesis, we can always insert a left paren.
# - We will use right paren as long as it won't lead to a syntax error, that is
#   we have more right parens than left.
#
# For more explaination check problem 8.9 of cracking the coding interview(6th
# edition)
#
# Complexity:
# ...

def generatePairOfParens(left_rem, right_rem, holder, idx, parens):
    if left_rem < 0 or right_rem < left_rem:
        return
    if not (left_rem or right_rem):
        parens.append(''.join(holder))
    else:
        if left_rem > 0:
            holder[idx] = '('
            generatePairOfParens(left_rem - 1, right_rem, holder, idx + 1, parens)
        if right_rem > left_rem:
            holder[idx] = ')'
            generatePairOfParens(left_rem, right_rem - 1, holder, idx + 1, parens)

def main():
  n = input("Enter number: ")
  try:
    n = int(n)
  except ValueError:
    print('Invalid input')
    return
  parens = []
  holder = [''] * n * 2
  generatePairOfParens(n,  # Left braces remaining
                       n,  # Right braces remaining  
                       holder,  # Var to store one valid paren expression
                       0,  # Index for holder
                       parens)  # Store response
  for idx in range(len(parens)):
    print('{idx}: {parens}'.format(idx=idx + 1, parens=parens[idx]))

if __name__ == '__main__':
  main()


# Output:
# --------
# (env) hansrajdas@Hansrajs-MacBook-Air ~/code/algorithms$ python Level-2/pair_of_parens.py
# Enter number: 1
# 1: ()
# (env) hansrajdas@Hansrajs-MacBook-Air ~/code/algorithms$ python Level-2/pair_of_parens.py
# Enter number: 2
# 1: (())
# 2: ()()
# (env) hansrajdas@Hansrajs-MacBook-Air ~/code/algorithms$ python Level-2/pair_of_parens.py
# Enter number: 3
# 1: ((()))
# 2: (()())
# 3: (())()
# 4: ()(())
# 5: ()()()
# (env) hansrajdas@Hansrajs-MacBook-Air ~/code/algorithms$ python Level-2/pair_of_parens.py
# Enter number: 4
# 1: (((())))
# 2: ((()()))
# 3: ((())())
# 4: ((()))()
# 5: (()(()))
# 6: (()()())
# 7: (()())()
# 8: (())(())
# 9: (())()()
# 10: ()((()))
# 11: ()(()())
# 12: ()(())()
# 13: ()()(())
# 14: ()()()()
