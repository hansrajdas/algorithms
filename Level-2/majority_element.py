#!/usr/bin/python

# Date: 2020-11-28
# 
# Description:
# Find majority element from an array, majority element in array is one that
# occurs more than n/2 times. It is guaranteed that array will surely have one
# such element which occurs more than n/2 times.
# 
# Approach:
# - Assume first element as majority element, taking count = 1
# - Scan further in array, if same element appears, increment count by 1
#   otherwise decrement count by 1
# - If count becomes 0, consider new element as max occurring element and
#   reset count to 1
# - Do another pass to verify if given element occurred more than n/2 times.
# 
# This cancellation algorithm is called Moore's voting algorithm.
# 
# Complexity:
# O(N)

def get_majority_element(A):
    maj = A[0]
    count = 1
    for i in range(1, len(A)):
        if maj == A[i]:
            count += 1
        else:
            count -= 1

        if not count:
            maj = A[i]
            count = 1

    # Validate if we found correct majority element
    count = 0
    for i in range(len(A)):
        if maj == A[i]:
            count += 1
    if count > len(A) // 2:
        return maj
    return -1


assert get_majority_element([1, 2, 5, 9, 5, 9, 5, 5, 5]) == 5
assert get_majority_element([1, 2, 3, 4, 4, 4]) == -1
assert get_majority_element([4, 4, 4, 1, 2, 3, 4]) == 4
