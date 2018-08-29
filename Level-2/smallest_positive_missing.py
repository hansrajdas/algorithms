#!/usr/bin/python2.7

# Date: 2018-08-28
#
# Description:
# Given an array of random integers(positive and negative numbers), find the
# smallest positive integer missing. For example:
#
# A = [1, 2, 3, 4] result = 5
# A = [10, 2, 3, 4] result = 1
# A = [-1, 0, 1, 3, 3, 5] result = 2
#
# Approach:
# Use a hash map to mark all positive numbers present in array and iterate once
# again to find which is the smallest missing. If no such element is found
# return max + 1.
#
# Complexity:
# Time - O(n)
# Space - O(n)


def solution(A):
    """
    Returns smallest positive number missing from a given array.

    Keyword arguments:
    A: List of numbers.
    """
    are_all_negative = True
    max_element = max(A)
    hash_map = {n: False for n in range(1, max_element + 1, 1)}
    
    # Populate hash map to mark all positive numbers present in input array.
    for a in A:
        if a > 0:
            are_all_negative = False
            hash_map[a] = True
   
    # If all numbers are negative in input array, 1 is the smallest positive
    # missing in array.
    if are_all_negative:
      return 1

    # Check hash map and return missing positive number, other max + 1 will be
    # returned.
    for num in range(1, max_element + 1, 1):
        if not hash_map[num]:
            return num
            
    return max_element + 1


def main():
    print (solution([-1, -3, -6, -4, -1, -2]))
    print (solution([1, 3, 6, 4, 1, 2]))
    print (solution([1, 2, 3, 4, 5]))
    print (solution([1, -2, -3, 2, -3, 5]))


if __name__ == '__main__':
  main()


# Output:
# 1
# 5
# 6
# 3
