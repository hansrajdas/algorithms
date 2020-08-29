def partition(A, low, high):
    pivot = A[high]
    i = low
    j = low

    while j < high:
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
        j += 1
    A[high], A[i] = A[i], A[high]
    return i

def kth_smallest(A, low, high, k):
    if k < 1 or k > high - low + 1:
        return None
    pivot_idx = partition(A, low, high)
    if pivot_idx - low == k - 1:
        return A[pivot_idx]
    elif pivot_idx - low < k - 1:
        return kth_smallest(A, pivot_idx + 1, high, k - pivot_idx + low - 1)  # Check right
    return kth_smallest(A, low, pivot_idx - 1, k)  # Check left

A = [12, 3, 5, 7, 4, 19, 26]
assert kth_smallest(A, 0, len(A) - 1, 3) == 5
assert kth_smallest(A, 0, len(A) - 1, 4) == 7
assert kth_smallest(A, 0, len(A) - 1, 7) == 26
assert kth_smallest(A, 0, len(A) - 1, 8) == None
