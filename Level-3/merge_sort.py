# Date: 2020-08-29
#
# Description:
# Implement merge sort.
#
# Approach:
# Partitions array in equal half and merges them back again in sorted order.
# This is done recursively until all array elements are sorted.
#
# Complexity:
# Time - O(nlogn)
# Space - O(n)

def merge(A, low, mid, high):
    first = A[low:mid + 1]  # Copy list elements
    second = A[mid + 1:high + 1]
    i = 0
    j = 0
    k = low
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            A[k] = first[i]
            i += 1
        else:
            A[k] = second[j]
            j += 1
        k += 1
    while i < len(first):
        A[k] = first[i]
        i += 1
        k += 1
    while j < len(second):
        A[k] = second[j]
        j += 1
        k += 1

def merge_sort(A, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(A, low, mid)
        merge_sort(A, mid + 1, high)
        merge(A, low, mid, high)

def sort(A):
    merge_sort(A, 0, len(A) - 1)
    return A  # To verify assert, otherwise A passed is sorted - inplace sorting

assert sort([3, 4, 5, 2, 1]) == [1, 2, 3, 4, 5]
assert sort([3, 4, 5, 2, 1, 6]) == [1, 2, 3, 4, 5, 6]
assert sort([]) == []
assert sort([1]) == [1]
assert sort([2, 1]) == [1, 2]
