#!/usr/bin/python

# Date: 2018-09-08
#
# Description:
# Implement selection sort.
#
# Approach:
# Finds index of minimum(when sorting in ascending) element from the remaining
# array and swap it with element at the end of sorted(starting portion of
# array) sub-array.
# While sorting in ascending order minimum element reaches at first place after
# first iteration of outer loop.
#
# Complexity:
# O(n^2)


def main():
    a = []
    n = input('Enter number of elements: ')
    for i in range(n):
        x = input('Enter value of a[%d]: ' % i)
        a.append(x)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[i] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]  # Swap min with sorted sub-array.

    # Sorted array.
    for i in range(n):
        print a[i]


if __name__ == '__main__':
    main()
