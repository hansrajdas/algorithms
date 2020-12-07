#!/usr/bin/python

# Date: 2020-12-07
#
# Description:
# Design an algorithm to find the kth number such that the only prime factors
# are 3, 5 and 7. Note that 3, 5 and 7 do not have to be factors, but is should
# not have any other prime factors. For example, the first several multiples
# would be (in order) 1, 3, 5, 7, 9, 15, 21.
#
# Approach:
# - We are actually to find kth smallest number in the form 3^a * 5^b * 7^c
# - A number of this sequence will create another 3 number for example, if we
#   we have a number N, then we will surely have 3 * N, 5 * N and 7 * N so we
#   can maintain 3 queues to save numbers which are multiple of 3, 5 or 7
# - Above fact can be used to find next numbers starting with 1, 3, 5, 7...
# - In this approach we will have to handle duplicates, this can be done using
#   keeping track of which queue has min value, we will remove min from that
#   queue and add multiple of 5 or 7 in other queues
# - Repeat above step k times
# - Check CTCI problem 17.9 for better explanation
#
# Complexity:
# O(k) time and space


import collections

def get_kth_multiple(k):
    if k < 2:
        return k

    Q3 = collections.deque([3])
    Q5 = collections.deque([5])
    Q7 = collections.deque([7])

    for k in range(k - 1):
        v3 = Q3[0]
        v5 = Q5[0]
        v7 = Q7[0]
        
        v = min(v3, v5, v7)

        if v == v3:
            _min = Q3.popleft()
            Q3.append(_min * 3)
            Q5.append(_min * 5)
        elif v == v5:
            _min = Q5.popleft()
            Q5.append(_min * 5)
        else:
            _min = Q7.popleft()
        Q7.append(_min * 7)  # Always enque to Q7
    return _min

def main():
    results = [
        0, 1, 3, 5, 7, 9, 15, 21, 25, 27, 35, 45, 49, 63, 75, 81, 105, 125,
        135, 147, 175, 189, 225, 243, 245
    ]
    for i in range(25):
        assert get_kth_multiple(i) == results[i]

if __name__ == '__main__':
    main()
