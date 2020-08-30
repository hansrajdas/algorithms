# Date: 2020-08-30
#
# Description:
# Implement counting sort.
#
# Approach:
# This works for integer only and sorts in O(n). We has to find the range(min
# to max - k) of elements and allocate an array of that size. Then keep of
# saving the counts of each element that appears.
#
# Problem:
# As range of elements(k) increases and dominates over n, both time and space
# complexity increases. Like if k = n^2 then complexity of this algorithm
# becomes O(n^2).
# In such cases radix sort can be used.
#
# Reference:
# https://www.hackerearth.com/practice/algorithms/sorting/counting-sort/tutorial/
#
# Complexity:
# Time - O(n + k)
# Space - O(k)

def counting_sort(A):
    if not A:
        return A
    _min = min(A)
    _max = max(A)

    counter = [0 for _ in range(_max - _min + 1)]

    for n in A:
        counter[n - _min] += 1

    i = 0
    for value, count in enumerate(counter):
        for _ in range(count):
            A[i] = value + _min
            i += 1

def sort(A):
    counting_sort(A)
    return A

assert sort([3, 4, 5, 2, 1]) == [1, 2, 3, 4, 5]
assert sort([3, 4, 5, 2, 1, 6]) == [1, 2, 3, 4, 5, 6]
assert sort([]) == []
assert sort([1]) == [1]
assert sort([2, 1]) == [1, 2]
assert sort([-2, 1]) == [-2, 1]
assert sort([-10, -20, 1, 10, 5, 0, 7, 9]) == [-20, -10, 0, 1, 5, 7, 9, 10]
