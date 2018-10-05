#!/usr/bin/python

# Date: 2018-10-05
#
# Description:
# Given 3 numbers n, k and b, you have to select b numbers from 1 to k such
# that sum of b selected numbers is n. There can be multiple solutions, return
# any one. In case of no solution possible return -1.
#
# For example:
# n = 12, k = 7 and b = 4
# One possible selection would be: [1, 2, 4, 5] as we have selected b = 4
# values which sums to n = 12 within range 1 to k = 7.
#
# Approach:
# Not working
#
# Complexity:
# -

def select_buckets_decreasing(n, k, b, selections):
  if not (n or b):
    return selections

  for val in range(k, 0, -1):
    if (n - val > 0 and b > 1) or (n - val == 0 and b == 1):
      selections.append(val)
      return select_buckets_decreasing(n - val, val - 1, b - 1, selections)

  return -1


def select_buckets_increasing(n, k, b, selections):
  if not (n or b):
    return selections

  for val in range(1, k + 1):
    if (n - val > 0 and b > 1) or (n - val == 0 and b == 1):
      selections.append(val)
      return select_buckets_increasing(n - val, val + 1, b - 1, selections)

  return -1


def select_buckets(n, k, b):
  selections = select_buckets_decreasing(n, k, b, [])
  if selections == -1:
    return select_buckets_increasing(n, k, b, [])

  return selections

def main():
  print select_buckets(12, 7, 2)
  print select_buckets(12, 7, 3)
  print select_buckets(12, 7, 4)
  print select_buckets(15, 7, 4)


if __name__ == '__main__':
  main()
