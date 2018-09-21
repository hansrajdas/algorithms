#!/usr/bin/python

# Date: 2018-09-21
#
# Description:
# Find longest palindrome from a given string. If input string is:
# forgeeksskeegfor, output should be: geeksskeeg as this is length longest(10)
# palindrome in given string.
#
# Approach:
# Checked all combinations. Considered all characters as middle one and tried
# to find as long palindrome as possible by expanding towards both left and
# right side.
#
# Complexity:
# O(n^2)
#
# Note:
# There is another approach called Manacher’s Algorithm which finds longest
# palindrome in O(n) time and O(n) space.

def find_longest_palindrome(string):
  max_len = 1
  start = 0
  n = len(string)

  # Consider all characters as middle one and find around them for longest
  # palindrome.
  for i in range(1, n):
    # Check for even length of palindromes.
    low = i - 1
    high = i
    while (low >= 0 and high < n) and (string[low] == string[high]):
      if max_len < high - low + 1:
        max_len = high - low + 1
        start = low
      low -= 1
      high += 1

    # Check for odd length of palindromes.
    low = i - 1
    high = i + 1
    while (low >= 0 and high < n) and (string[low] == string[high]):
      if max_len < high - low + 1:
        max_len = high - low + 1
        start = low
      low -= 1
      high += 1
  print ('Longest palindrome length is: %d, string: %s' % (
    max_len, string[start:start + max_len]))

def main():
  string = raw_input('Enter string: ')
  find_longest_palindrome(string)


if __name__ == '__main__':
  main()


# Output:
# -------------------
# Enter string: asd
# Longest palindrome length is: 1, string: a: 
#
# Enter string: asd
# Longest palindrome length is: 1, string: a
#
# Enter string: niti
# Longest palindrome length is: 3, string: iti
#
# Enter string: nitin
# Longest palindrome length is: 5, string: nitin
#
# Enter string: geeks
# Longest palindrome length is: 2, string: ee
#
# Enter string: forgeeksskeegfor
# Longest palindrome length is: 10, string: geeksskeeg
