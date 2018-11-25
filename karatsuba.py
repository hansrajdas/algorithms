#!/usr/bin/python

# Date: 2017-12-17
#
# Description:
# Karatsuba algo an efficiant way to multiply very large numbers. Conventional
# way of multiplication has complexity of O(n^2) as every bit of one number is
# multiplied by every other. Karatsuba is efficient than quadratic.
#
# Approach:
# Both numbers can be expressed as high and low components like
# x = (10^n/2)*x_H + x_L and y = (10^n/2)*y_H + y_L
# where n is max of number of digits in x or y.
#
# So, x*y = (10^n)*x_H*y_H + (10^n/2)*(x_H*y_L + x_L*y_H) + x_L*y_L
# above expression requires 4 multiplies to get the result which can be reduced
# to 3 as we can find x_H*y_L + x_L*y_H using a hack:
#
# x_H*y_L + x_L*y_H = (x_H + x_L)*(y_H + y_L) - x_H*y_H - x_L*y_L
# and we have already found x_H*y_H and x_L*y_L. so we are done in 3 multiply
# operations instead of 4.
#
# Reference:
# https://brilliant.org/wiki/karatsuba-algorithm/
#
# Complexity:
# O(n^1.58), better than conventional algo.


def karatsuba(x, y):
  """
  Multiply 2 numbers by karatsuba algo.
  
  Args:
    x: first number to be multiplied.
    y: second number to be multiplied.

  Returns:
    Product of x and y.
  """

  # base case
  if (x < 10 and y < 10):
    return x*y

  n = max(len(str(x)), len(str(y)))
  m = n/2
  
  div_factor = 10**m
  x_H = x / div_factor
  x_L = x % div_factor

  y_H = y / div_factor
  y_L = y % div_factor

  a = karatsuba(x_H, y_H)
  d = karatsuba(x_L, y_L)
  e = karatsuba(x_H + x_L, y_H + y_L) - a - d

  return (a*(10**(m*2)) + e*(10**m) + d)


num_1 = raw_input("Enter first number: ")
num_2 = raw_input("Enter second number: ")

print (karatsuba(int(num_1), int(num_2)))
