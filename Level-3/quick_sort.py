# Date: 2020-07-19
#
# Description:
# Implement quick sort.
#
# Implementation:
# Uses divide and conquer approach. It divides the array in 2 parts lower part
# has all elements lesser than all elements at higher part. Partitioning is
# done across an element called pivot. So after each iteration selected pivot
# gets placed at correct position in array.
# In below program last element of sub array is taken as pivot and that is
# placed at correct place after each call to partition function.
#
# Complexity:
# O(nlogn) time, Best and average case
# O(n^2) time, Worst case, when array is already sorted in asc or dsc order
# O(1) space

def partion(A, low, high):
    pivot = A[high]
    i = low  # Counts the number of elements less than or equal to pivot
    j = low  # For looping over all elements of A

    while j < high:
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
        j += 1
    A[i], A[high] = A[high], A[i]  # Place pivot element at correct place
    return i

def quick_sort(A, low, high):
    if low < high:
        pivot_idx = partion(A, low, high)
        quick_sort(A, low, pivot_idx - 1)
        quick_sort(A, pivot_idx + 1, high)


def sort(A):
    quick_sort(A, 0, len(A) - 1)
    return A  # To verify assert, otherwise A passed is sorted - inplace sorting

assert sort([2, 3, 10, 5, 6, 1, 3, 9]) == [1, 2, 3, 3, 5, 6, 9, 10]
assert sort([3, 4, 5, 2, 1]) == [1, 2, 3, 4, 5]
assert sort([3, 4, 5, 2, 1, 6]) == [1, 2, 3, 4, 5, 6]
assert sort([]) == []
assert sort([1]) == [1]
assert sort([2, 1]) == [1, 2]
