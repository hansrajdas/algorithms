#!/usr/bin/python

# Date: 2020-08-15
#
# Description:
# There are 2 sorted arrays in ascending order (having distinct elements). Task
# is to find element having overall rank of k or kth smallest element.
#
# Approach:
# Scan linearly both arrays and stop overall traversal is done for k elements.
# If any of the array ends, scan the other array till k.
#
# Complexity:
# O(k)

def rank_k_element(A, B, k):
    """Return element having rank k b/w 2 sorted arrays in ascending order."""
    if len(A) + len(B) < k:
        return None
    i = 0
    j = 0
    while i < len(A) and j < len(B) and k:
        if A[i] < B[j]:
            rank = A[i]
            i += 1
        else:
            rank = B[j]
            j += 1
        k -= 1
    if not k:
        return rank
    if i == len(A):
        z = j
        P = B
    else:
        z = i
        P = A
    while k:
        rank = P[z]
        z += 1
        k -= 1
    return rank

assert rank_k_element([1, 2, 3], [4, 5, 6], 1) == 1
assert rank_k_element([1, 2, 3], [4, 5, 6], 2) == 2
assert rank_k_element([1, 2, 3], [4, 5, 6], 3) == 3
assert rank_k_element([1, 2, 3], [4, 5, 6], 4) == 4
assert rank_k_element([1, 2, 3], [4, 5, 6], 5) == 5
assert rank_k_element([1, 2, 3], [4, 5, 6], 6) == 6

assert rank_k_element([4, 5, 6], [1, 2, 3], 1) == 1
assert rank_k_element([4, 5, 6], [1, 2, 3], 2) == 2
assert rank_k_element([4, 5, 6], [1, 2, 3], 3) == 3
assert rank_k_element([4, 5, 6], [1, 2, 3], 4) == 4
assert rank_k_element([4, 5, 6], [1, 2, 3], 5) == 5
assert rank_k_element([4, 5, 6], [1, 2, 3], 6) == 6

assert rank_k_element([2, 4, 6, 8], [1, 3, 5, 9], 5) == 5
