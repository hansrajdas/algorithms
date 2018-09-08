#!/usr/bin/python

# Date: 2018-09-08
#
# Description:
# Implement insertion sort.
#
# Approach:
# Scans from right in sorted sub-array and inserts current element at correct
# place by shifting all the elements to right.
#
# Complexity:
# O(n^2)


def main():
    a = []
    n = input('Enter number of elements: ')
    for i in range(n):
        x = input('Enter value of a[%d]: ' % i)
        a.append(x)

    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key  # Insert current element at correct place.

    # Sorted array.
    for i in range(n):
        print a[i]


if __name__ == '__main__':
  main()
