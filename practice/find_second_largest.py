def get_second_largest(A):
    first = float('-inf')
    second = float('-inf')

    for n in A:
        if first < n:
            second = first
            first = n
        elif second < n and first != n:
            second = n
    return second

assert get_second_largest([1, 2, 3, 4, 5]) == 4
assert get_second_largest([5, 4, 3, 2, 1]) == 4
