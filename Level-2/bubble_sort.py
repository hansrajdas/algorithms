#!/usr/bin/python

# Date: 2018-09-08
#
# Description:
# Implement bubble sort.
#
# Approach:
# Compares adjacent elements and pushes to it's required extreme. Here while
# sorting in ascending order largest element reaches at last place after first
# iteration of outer loop.
#
# Complexity:
# O(n^2)


def main():
    a = []
    n = input ("Enter number of elements: ")
    for i in range (n):
        x = input ("Enter value of a[%d]: " % i)
        a.append(x)

    for i in range(n):
        swap_flag = False;
        for j in range(0, n - 1 - i, 1):
            if (a[j] > a[j + 1]):
                a[j], a[j+1] = a[j+1], a[j]
                swap_flag = True;

        if not swap_flag:
            break

    # Print sorted array
    for i in range(n):
        print a[i]


if __name__ == '__main__':
  main()
