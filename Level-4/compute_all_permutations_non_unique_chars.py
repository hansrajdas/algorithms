#!/usr/bin/python

# Date: 2018-08-04
#
# Description:
# Write a method to compute all permutations of a string whose characters are
# not necessarily unique. The list of permutations should not have duplicates.
#
# Approach:
# One of way is to follow the same approach as used for unique characters(
# Level-3/compute_all_permutations_unique_chars.py) and while adding new
# permutation, check if it already added to the list, we can use set for this
# instead of list. But this solution will have the same complexity: O(n^2 * n!)
#
# We can leverage this fact that, input string can have duplicates and do this
# in better complexity but worst case would remain the same. This solution will
# be way faster in cases where we will have lot of duplicates.
#
# 1. Create a map haivng count of characters like a = 2, b = 2, c = 1
# 2. Let's imagine generating a permutation of this string(now in map). The
#    first choice we make is whether to use a, b or c as the first char. After
#    that, we have a subproblem to solve: find all permutations of the
#    remaining chars, and append those to the already picked "prefix".
#
# For better explaination, please refer problem 8.8 of cracking the coding
# interview, 6th edition.
#
# Complexity:
# O(n^2) best case, when we have all same chars in input string like "aaaaa"
# O(n^2 * n!) in worst case
#
# Additional O(n) space complexity to store char frequency, in addition to
# storing all permutations

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
  string = input("Enter input string: ")
  hashMap = getHashMap(string)
  computePermutationsNonUniqueChars(hashMap, "", len(string), result)
  for idx in range(len(result)):
    print('{idx}: {perm}'.format(idx=idx + 1, perm=result[idx]))

if __name__ == '__main__':
  main()
