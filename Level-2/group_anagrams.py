#!/usr/bin/python

# Date: 2018-07-18
#
# Description:
# Write a method to sort an array of strings so that all the anagrams are next
# to each other.
#
# Approach:
# Sort strings to check if they are anagram of any previous string in array.
# And store all strings in a hash map, key will be sorted string and value will
# be list of original strings which is anagram of key.
#
# Complexity:
# M = Number of strings, N = Average length of strings.
# Time: O(M*N*log(N)), If sort_string takes N*log(N)
# Space: O(M*N) In worst case also.
#
# Improvement scope:
# We can implement counting sort to sort characters in a string, which has a
# time complexity of O(N) so overall complexity of this algorithm will be
# O(M*N).

import collections


def sort_string(s):
  return ''.join(sorted(list(s)))

def group_anagrams(array):
  hash_map = collections.defaultdict(list)
  for s in array:
    value = sort_string(s)
    hash_map[value].append(s) 

  # Return grouped items - All values of hash map.
  return [v for k in hash_map for v in hash_map[k]]

def main():
  array = ["abc", "adb", "bac", "bad", "cat"]
  print "Input array of strings:", array
  grouped = group_anagrams(array)
  print "Anagrams grouped:\t", grouped


if __name__ == '__main__':
  main()

# Output:
# Input array of strings: ['abc', 'adb', 'bac', 'bad', 'cat']
# Anagrams grouped:	['abc', 'bac', 'adb', 'bad', 'cat']
