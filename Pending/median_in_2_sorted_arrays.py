#!/usr/bin/python

# Date: 2018-
#
# Description:
# Given 2 sorted arrays find overall median of the combined sorted arrays.
#
# Approach:
#
# Explained:
# https://www.youtube.com/watch?v=LPFhl65R7ww&t=74s
# https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/
#
# Complexity:
# O(log(min(m + n)))


def median_of_2_sorted_arrays(A, B):
  if len(A) < len(B):
    return median_of_2_sorted_arrays(B, A)


def main():
  A = [3, 5, 10, 11, 17]
  B = [9, 13, 20, 21, 23, 27]

  print ('Median is: %d' % median_of_2_sorted_arrays(A, B))


if __name__ == '__main__':
  main()
