#!/usr/bin/python

# Date: 2020-12-19
#
# Description:
# A popular masseuse receives a sequence of back-to-back appointment requests
# and is debating which ones to accept. She needs a 15-minute break between
# appointments and therefore she cannot accept any adjacent requests. Given a
# sequence of back-to-back appointment requests (all multiples of 15 minutes,
# none overlap, and none can be moved), find the optimal (highest total booked
# minutes) set the masseuse can honor. Return the number of minutes.
# EXAMPLE
# Input {30, 15, 60, 75, 45, 15, 15, 45}
# Output 180 minutes ({30, 60,45, 45})
#
# Approach:
# Recursively check all possibilities
# - At every meeting, will have choice to take or skip that meeting
# - If taken, then can't take next meeting - go to i + 2
# - Else can take next meeting - go to i + 1
#
# Complexity:
# O(n) time and space

def max_minutes(meetings, index, cache):
    if index >= len(meetings):
        return 0
    if index in cache:
        return cache[index]
    cache[index] = max(
        meetings[index] + max_minutes(meetings, index + 2, cache),
        max_minutes(meetings, index + 1, cache))
    return cache[index]


def main():
    cache = {}
    assert max_minutes([30, 15, 60, 75, 45, 15, 15, 45], 0, cache) == 180

    cache = {}
    assert max_minutes([75, 105, 120, 75, 90, 135], 0, cache) == 330

    cache = {}
    assert max_minutes([45, 60, 45, 15], 0, cache) == 90

if __name__ == '__main__':
    main()
