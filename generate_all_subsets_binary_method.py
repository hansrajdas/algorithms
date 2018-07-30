#!/usr/bin/python

# Date: 2018-07-30
#
# Description:
# Write a method to return all subsets of a set.
#
# Approach:
# Subsets can be modelled as binary representation of a number where 1
# represents that element is present in subset and 0 represents element will not
# be present in subset. For example subsets of {a1, a2} will be:
#
# a1 a2 subset
# ------------
# 0  0  {}
# 0  1  {a2}
# 1  0  {a1}
# 1  1  {a1, a2}
#
# This is how all subsets can be generated where each bit position represents an
# element in the original set.
#
# Complexity:
# Time: O(n*2^n)
# Space: O(n*2^n)

def convertNumToSubset(a, k):
  """Based on binary representation of k subset is generated using elements
     in original set a.
     
   Args:
   a: Original set
   k: Number whose each bit position represents element will be included in set
    or not.
   """
  idx = 0
  subset = set()
  while k:
    if k & 1:
      subset.add(a[idx])
    idx += 1
    k >>= 1
  return subset

def generateAllSubsets(a, n):
  """Generates all subsets using elements given in list a.
  
  Args:
    a: List of elements.
    n: Number of elements in list a.
  """
  subsets = []
  if not n:
    return [set()]
 
  numberOfSubsets = 1 << n
  k = 0
  while k < numberOfSubsets:
    subs = convertNumToSubset(a, k)
    subsets.append(subs)
    k += 1
  return subsets

def main():
  a = []
  n = input("Enter number of elements: ")
  for i in xrange(n):
      x = input("Enter value of a[%d] : " % i)
      a.append(x)

  subsets = generateAllSubsets(a, n)
  print "\nAll subsets are: "
  for i in range(len(subsets)):
    print "{idx}: {subset}".format(idx=i, subset=subsets[i])

if __name__ == '__main__':
  main()

# Output:
# *************************
# python generate_all_subsets_binary_method.py 
# Enter number of elements: 2
# Enter value of a[0] : 1
# Enter value of a[1] : 2
# 
# All subsets are: 
# 0: set([])
# 1: set([1])
# 2: set([2])
# 3: set([1, 2])
#
# python generate_all_subsets_binary_method.py 
# Enter number of elements: 3
# Enter value of a[0] : 1
# Enter value of a[1] : 2
# Enter value of a[2] : 3
# 
# All subsets are: 
# 0: set([])
# 1: set([1])
# 2: set([2])
# 3: set([1, 2])
# 4: set([3])
# 5: set([1, 3])
# 6: set([2, 3])
# 7: set([1, 2, 3])
