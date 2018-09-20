#!/usr/bin/python

# Date: 2018-09-20
#
# Description:
# Given 2 sorted arrays find overall median of the combined sorted arrays.
#
# Approach:
# Idea is to find points in both array which divides part of smaller array
# + some part of larger array in exactly half of the total size of array. To
# find this point we will use divide and conquer approach on smaller array.
#
# Explained:
# https://www.youtube.com/watch?v=LPFhl65R7ww
# https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/
#
# Complexity:
# O(log(min(m + n)))


def median_of_2_sorted_arrays(A, B):
  """Finds median from 2 sorted arrays."""

  # Keep first array as smaller one.
  if len(A) > len(B):
    return median_of_2_sorted_arrays(B, A)

  x = len(A)
  y = len(B)
  low = 0
  high = x

  while low <= high:
    partition_x = low + (high - low)/2
    partition_y = (x + y + 1)/2 - partition_x

    max_left_x = A[partition_x - 1] if partition_x else float('-inf')
    min_right_x = A[partition_x] if partition_x < x else float('inf')
    max_left_y = B[partition_y - 1] if partition_y else float('-inf')
    min_right_y = B[partition_y] if partition_y < y else float('inf')

    # We have divided 2 arrays in exactly half-half partition so now we just
    # have to return the middle elements.
    if max_left_x <= min_right_y and max_left_y <= min_right_x:
      # Odd number of total elements, median is Array[n/2] otherwise it will be
      # (Array[n/2] + Array[n/2 + 1])/2
      if (x + y) % 2:
        return max(max_left_x, max_left_y)
      else:
        return (
          max(max_left_x, max_left_y) + min(min_right_x, min_right_y))/2.0
    elif max_left_x > min_right_y:
      # Too right move partition point more towards left.
      high = partition_x - 1
    else:
      low = partition_x + 1

  raise ValueError('Arrays are not sorted')  # Error condition


def main():
  A = [3, 5, 10, 11, 17]
  B = [9, 13, 20, 21, 23, 27]

  print ('Median is: %f' % median_of_2_sorted_arrays(A, B))


if __name__ == '__main__':
  main()


# Output:
# -------------
# Median is: 13.000000 
