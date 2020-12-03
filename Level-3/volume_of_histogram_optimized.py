#!/usr/bin/python

# Date: 2020-12-01
#
# Description:
# Imagine a histogram (bar graph). Design an algorithm to compute the volume of
# water it could hold if someone poured water across the top. You can assume
# that each histogram bar has width 1.
#
# EXAMPLE
# Input: [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
# Output: 26
#
# Approach:
# We can keep track of left and right max seen so far to optimize:
# - Scan left to right and keep maintain max seen so far
# - Scan right to left, keep on tracking max seen so far. Also at a given index
#   take min of left_max and right_max - this will be our second tallest
# - Now if current bar is shorter than second tallest, then this bar will hold
#   some water above it, difference to result
#
# Pictorial explanation in CTCI 17.21
#
# Complexity:
# O(N) time and space


def compute_histrogram_volume(histogram):
    n = len(histogram)
    volume = 0
    left_max = [-1 for _ in range(n)]
    right_max = [-1 for _ in range(n)]

    # Build left max
    _max = histogram[0]
    for i in range(n):
        _max = max(_max, histogram[i])
        left_max[i] = _max

    # Build right max and compute water logged
    _max = histogram[n - 1]
    for i in range(n - 1, -1, -1):
        _max = max(_max, histogram[i])
        right_max[i] = _max

        second_tallest = min(left_max[i], right_max[i])

        # If there are taller things on the left and right side, then there is
        # water above this bar. Compute the colume and add to the `volume`.
        if second_tallest > histogram[i]:
            volume += second_tallest - histogram[i]
    return volume

assert compute_histrogram_volume([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]) == 26
