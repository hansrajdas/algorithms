# Date: 2018-07-27
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
# Process numbers in batches of 3 and if middle number is not smallest then swap
# it with smallest among 3.
# Like in [0, 1, 2, 4, 5] -> Process [0, 1, 2] => [1, 0, 2, 4, 5]
# -> Process [2, 4, 5] => [1, 0, 4, 2, 5], this is peak-valley-peak sequence.
#
# Complexity:
# O(n)

MAX_INT = 1 << 32

def getMinIdx(a, n, i, j, k):
  iVal = a[i] if i < n else MAX_INT
  jVal = a[j] if j < n else MAX_INT
  kVal = a[k] if k < n else MAX_INT

  minimum = min(iVal, min(jVal, kVal))
  if iVal == minimum:
    return i
  elif jVal == minimum:
    return j
  else:
    return k

def getPeaksAndValleys(a, n):
  idx = 1
  while idx < n:
    minIdx = getMinIdx(a, n, idx - 1, idx, idx + 1)
    if minIdx != idx:
      a[minIdx], a[idx] = a[idx], a[minIdx]
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

  arr = [9, 1, 0, 4, 8, 7]
  print '\nInput: ', arr
  print 'Peak valley pattern: ', getPeaksAndValleys(arr, len(arr))

if __name__ == '__main__':
  main()


# Output:
# Input:  [5, 3, 1, 2, 3]
# Peak valley pattern:  [5, 1, 3, 2, 3]
#
# Input:  [10, 5, 2, 3, 9, 8, 7, 6, 1, 4]
# Peak valley pattern:  [10, 2, 5, 3, 9, 7, 8, 1, 6, 4]
#
# Input:  [5, 10]
# Peak valley pattern:  [10, 5]
#
# Input:  [9, 1, 0, 4, 8, 7]
# Peak valley pattern:  [9, 0, 4, 1, 8, 7]
