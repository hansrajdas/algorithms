#!/usr/bin/python

# Date: 2018-08-04
#
# Description:
# Write a method to compute all permutations of a string whose characters are
# not necessarily unique. The list of permutations should not have duplicates.
#
# Approach:
# Not much clear, refer 8.6 from CTCI.
#
# Complexity:
# O(n * n!)

import collections

def computePermutationsNonUniqueChars(hashMap, prefix, rem, result):
  """Generates list of all permutations of a given string.
  
  Args:
    hashMap: Dictionary having characters as key and there count of occurrences
      as value.
    prefix: Prefix string used, initially empty.
    rem: Length of string remaining.
    result: List to store all permutations.
  """
  if not rem:
    result.append(prefix)
    return;
  
  for k in hashMap:
    count = hashMap[k]
    if count:
      hashMap[k] = count - 1
      computePermutationsNonUniqueChars(hashMap, prefix + k, rem - 1, result)
      hashMap[k] = count
     
def getHashMap(string):
  """Creates a hash map from string.
  
  Key as character, value as count of occurrences.
  """
  m = collections.defaultdict(int)
  for k in string:
    m[k] += 1
  return m
    
def main():
  result = []
  string = raw_input("Enter input string (having unique characters): ")
  hashMap = getHashMap(string)
  computePermutationsNonUniqueChars(hashMap, "", len(string), result)
  for idx in range(len(result)):
    print '{idx}: {perm}'.format(idx=idx + 1, perm=result[idx])

if __name__ == '__main__':
  main()
