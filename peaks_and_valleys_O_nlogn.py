# Date: 2018-07-26
#
# Description:
# In an array of integers, a "peak" is an element which is greater than or equal
# to the adjacent integers and a "valley" is an element which is less than or
# equal to the adjacent integers.
# For example, in the array {5, 8, 6, 2, 3, 4, 6 }, {8, 6} are peaks and {5, 2}
# are valleys. Given an array of integers, sort the array into an alternating
# sequence of peaks and valleys.
# EXAMPLE
# Input: {5, 3, 1, 2, 3}
# Output: {5, 1, 3, 2, 3}
#
# Approach:
# Sort the array in ascending order then swap current and last element. Current
# element would start from 0 and increment by 2 so we would require only n/2
# swaps to get required array.
#
# Complexity:
# O(nlogn)

def getPeaksAndValleys(a, n):
  idx = 0
  # Sort a in ascending order, O(nlogn) operation.
  a.sort()

  # Swap current and last element.
  a[idx], a[n - 1] = a[n - 1], a[idx]
  idx += 3
  while idx < n:
    a[idx], a[n - 1] = a[n - 1], a[idx]
    idx += 2
  return a

def main():
  arr = [5, 3, 1, 2, 3]
  print 'Input: ', arr
  print 'Peak valley pattern: ', getPeaksAndValleys(arr, len(arr))

  arr = [10, 5, 2, 3, 9, 8, 7, 6, 1, 4]
  print '\nInput: ', arr
  print 'Peak valley pattern: ', getPeaksAndValleys(arr, len(arr))

  arr = [5, 10]
  print '\nInput: ', arr
  print 'Peak valley pattern: ', getPeaksAndValleys(arr, len(arr))

if __name__ == '__main__':
  main()


# Output:
# Input:  [5, 3, 1, 2, 3]
# Peak valley pattern:  [5, 2, 3, 1, 3]
#
# Input:  [10, 5, 2, 3, 9, 8, 7, 6, 1, 4]
# Peak valley pattern:  [10, 2, 3, 1, 5, 4, 7, 6, 9, 8]
#
# Input:  [5, 10]
# Peak valley pattern:  [10, 5]
