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
# From iterative approach `max_minutes_iterative` (Level-2/max_minutes.py),
# we are only interested in last values that is, if we are at index i we are
# only interested in index i + 1 and i + 2 so these values can be maintained in
# variables instead of taking an array.
#
# Complexity:
# O(n) time

def max_minutes(meetings):
    one_away = 0
    two_away = 0
    for i in range(len(meetings) - 1, -1, -1):
        best_with = meetings[i] + two_away
        best_without = one_away
        current = max(best_with, best_without)
        two_away = one_away
        one_away = current
    return current
        

def main():
    assert max_minutes([30, 15, 60, 75, 45, 15, 15, 45]) == 180
    assert max_minutes([75, 105, 120, 75, 90, 135]) == 330
    assert max_minutes([45, 60, 45, 15]) == 90

if __name__ == '__main__':
    main()
