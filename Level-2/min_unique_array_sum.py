#!/usr/bin/python

# Date: 2018-10-15
#
# Description:
# Given an array, increment any duplicate elements until all its elements are
# unique. In addition, the sum of its elements must be the minimum possible
# within the rules.
# For example if arr = [3, 2, 1, 2, 7], then arrMin will be [3, 2, 1, 4, 7]
# and its elements sum to minimal value of 3 + 2 + 1 + 4 + 7 = 17
#
# Approach:
# Take an empty set and scan array from beginning, if array element is present
# in set increment that element until we find an element which is not present in
# set and add that to set.
# Return sum of all set elements.
#
# Complexity:
# O(N) average case, O(N^2) in worst case
# N = Number of elements in array

MAX_VALUE = 5001

def getMinimumUniqueSum(arr):
  unique = set()
  for a in arr:
    for x in range(a, MAX_VALUE):
      if x not in unique:
        break
    unique.add(x)
  return sum(unique)


def main():
  a = []
  n = input('Enter number of elements: ')
  for i in xrange (n):
      x = input('Enter value of a[%d]: ' % i)
      a.append(x)

  print getMinimumUniqueSum(a)


if __name__ == '__main__':
  main()


# Output:
# ------------------------
# Enter number of elements: 3
# Enter value of a[0]: 1
# Enter value of a[1]: 2
# Enter value of a[2]: 2
# 6
#
# Enter number of elements: 5
# Enter value of a[0]: 3
# Enter value of a[1]: 2
# Enter value of a[2]: 1
# Enter value of a[3]: 2
# Enter value of a[4]: 7
# 17
