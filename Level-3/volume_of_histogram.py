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
# We can take follow divide and conquer approach:
# - Find index having max height
# - Find second tallest in each subgraph (left and right)
# - Compute the volumes between the tallest and the second tallest
# - Recurse towards left and right
#
# Complexity:
# O(N^2)


def compute_histrogram_volume(histogram):
    max_index = find_index_of_max(histogram, 0, len(histogram) - 1)

    left_volume = subgraph_volume(histogram, 0, max_index, True)
    right_volume = subgraph_volume(histogram, max_index, len(histogram) - 1, False)
    return left_volume + right_volume

def subgraph_volume(histogram, start, end, is_left):
    if start >= end:
        return 0
    volume = 0
    if is_left:
        max_idx = find_index_of_max(histogram, start, end - 1)
        volume += bodered_volume(histogram, max_idx, end)
        volume += subgraph_volume(histogram, start, max_idx, is_left)
    else:
        max_idx = find_index_of_max(histogram, start + 1, end)
        volume += bodered_volume(histogram, start, max_idx)
        volume += subgraph_volume(histogram, max_idx, end, is_left)
    return volume
        
def find_index_of_max(histogram, start, end):
    max_idx = start
    for i in range(start + 1, end + 1):
        if histogram[max_idx] < histogram[i]:
            max_idx = i
    return max_idx

def bodered_volume(histogram, start, end):
    """
    Compute volume between start and end. Assume tallest bar is at start and
    second tallest is at end.
    """
    if start >= end:
        return 0
    vol = 0
    _min = min(histogram[start], histogram[end])
    for i in range(start + 1, end):
        vol += _min - histogram[i]
    return vol

assert compute_histrogram_volume([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]) == 26
