def min_heapify(A, n, i):
    left = (i << 1) + 1
    right = (i << 1) + 2
    min_idx = i

    if left < n and A[min_idx] > A[left]:
        min_idx = left
    if right < n and A[min_idx] > A[right]:
        min_idx = right
    if min_idx != i:
        A[min_idx], A[i] = A[i], A[min_idx]
        min_heapify(A, n, min_idx)

def get_kth_largest(A, k):
    # Build min heap of size k
    for i in range(k // 2, -1, -1):
        min_heapify(A, k, i)

    for i in range(k, len(A)):
        if A[0] < A[i]:
            A[0] = A[i]
            min_heapify(A, k, 0)
    return A[0]

get_kth_largest([1, 2, 3, 4, 5, 6, 7], 3) == 5
get_kth_largest([7, 6, 5, 4, 3, 2, 1], 3) == 5
get_kth_largest([1, 2, 3, 4, 5, 6], 1) == 6
