#!/usr/bin/python

# Date: 2018-07-20
#
# Description:
# Given a sorted array of strings that is interspersed with empty strings, write
# a method to find the location of a given string.
# Example:
# array: ['at', '', 'cvb', '', '', 'kl'], find: 'cvb'
# Output: 2
#
# Approach:
# Modified binary search is used. If we encounter empty string at mid position
# we find nearest non empty (right to mid in this case, can be left also) string
# and compare.
#
# Complexity:
# Average case: O(log(n))
# Worst case: O(n), if string is found at extreme right and there are all empty
# strings from mid to right.

def search_string_in_sparse_array(strings, string, l, r):
  """Returns index of string from strings array.
  
  Args:
    strings: Array of string.
    string: string to be searched.
    l: Left index.
    r: Right index.

  Returns:
    -1 if string not found otherwise index of searched string.
  """
  m = l + (r - l)/2
  
  if strings[m] == string:
    return m

  if l > r:
    return -1
  
  original_mid = m
  # If mid index has empty string then find first index to the right where
  # string is non empty.
  if not strings[m]:
    while (m < r) and (not strings[m]):
      m += 1

  # Moving we encounter first non empty string same as key.
  if (m < r) and (string == strings[m]):
    return m

  if m == r or string < strings[m]:  # Key is on left half.
    return search_string_in_sparse_array(strings, string, l, original_mid - 1)
  return search_string_in_sparse_array(strings, string, original_mid + 1, r)

def main():
  array = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
  key = 'att'

  for i in range(len(array)):
    print 'Array[{index}]: {string!r}'.format(index=i, string=array[i])
  
  idx = search_string_in_sparse_array(array, key, 0, len(array) - 1)
  if idx == -1:
    print '\nString {key!r} not found in array'.format(key=key)
  else:
    print '\nString {key!r} found at index: {idx}'.format(key=key, idx=idx)


if __name__ == '__main__':
  main()

# Output:
# hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ python search_sparse_string.py
# Array[0]: 'at'
# Array[1]: ''
# Array[2]: ''
# Array[3]: ''
# Array[4]: 'ball'
# Array[5]: ''
# Array[6]: ''
# Array[7]: 'car'
# Array[8]: ''
# Array[9]: ''
# Array[10]: 'dad'
# Array[11]: ''
# Array[12]: ''
#
# String 'ball' found at index: 4
# hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ python search_sparse_string.py
# *** SAME AS ABOVE ***
#
# String 'car' found at index: 7
# hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ python search_sparse_string.py
# *** SAME AS ABOVE ***
#
# String 'dad' found at index: 10
# hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ python search_sparse_string.py
# *** SAME AS ABOVE ***
#
# String 'at' found at index: 0
# hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ python search_sparse_string.py
# *** SAME AS ABOVE ***
#
# String 'att' not found in array
