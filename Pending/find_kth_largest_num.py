#!/usr/bin/python

# Date: 2018-
#
# Description:
# Find kth largest number from an unsorted array.
#
# Approach:
#
# Reference:
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-3-worst-case-linear-time/
#
# Complexity:
# O(n)

def main():
  a = []
  n = input('Enter number of elements: ')
  for i in xrange (n):
      x = input('Enter value of a[%d]: ' % i)
      a.append(x)


if __name__ == '__main__':
  main()
