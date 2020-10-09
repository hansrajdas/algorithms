#!/usr/bin/python

# Date: 2020-10-09
#
# Description:
# There are 2 sorted arrays in ascending order (having distinct elements). Task
# is to find element having overall rank of k or kth smallest element.
#
# Approach:
# Modified binary search is used. We can discard elements from array for which
# element at index rank/2 is smaller than other array (Can now search in
# A[0...m] and B[k/2....n] for rank k - k/2).
#
# Complexity:
# O(log(k))

def rank_k(A, B, k):
    if not A:
        return B[k - 1]
    elif not B:
        return A[k - 1]
    elif k == 1:
        return min(A[0], B[0])

    i = min(k // 2, len(A))
    j = min(k // 2, len(B))

    # If A[k/2] > B[k/2], then we can discard B[0...k/2] elements as element
    # with rank k can't be in in B[0...k/2]. Taking this into consideration we
    # now has to find element with rank: k - k/2.
    if A[i - 1] > B[j - 1]:
        return rank_k(A, B[j:], k - j)
    return rank_k(A[i:], B, k - i)

assert rank_k([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5) == 5
