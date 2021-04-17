#!/usr/bin/python

# Date: 2021-04-13
#
# Description:
# Given an array of non-negative numbers and a non-negative number k, find the
# number of subarrays having sum less than k. We may assume that there is no
# overflow.
#
# Approach:
#
# Reference:
# https://www.geeksforgeeks.org/number-subarrays-sum-less-k/
#
# Complexity:
# O(N)


def solve(A, k):
    ans = 0
    _sum = A[0]
    start = end = 0
    n = len(A)

    while start < n and end < n:
        if _sum <= k:
            end += 1

            if end > start:
                ans += end - start

            if end < n:
                _sum += A[end]
        else:
            _sum -= A[start]
            start += 1
    return ans

# Driver Code
if __name__ == "__main__":
    array = [1, 11, 2, 3, 15]
    k = 10
    print(solve(array, k))
