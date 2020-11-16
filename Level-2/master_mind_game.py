#!/usr/bin/python

# Date: 2020-11-16
#
# Description:
# The game of master mind is played as follows:
# This computer has four slots, and each slot will contain a ball that is red(R),
# yellow(Y), green(G) or blue(B). For example, the computer might have RGGB(
# Slot #1 is red, Slots #2 and #3 are green, Slot #4 is blue)>
#
# You, the user, are trying to guess the solution. You might, for example,
# guess YRGB.
#
# When you guess the correct color for the correct slot, you get a "hit". If
# you guess a color that exists but is in the wrong slot, your get a
# "pseudo-hit". Not that a slot that is a hit can never count as a pseudo-hit.
#
# For example, if the actual solution is RGBY and you guess GGRR, you have one
# hit and one pseudo-hit.
#
# Write a method that, given a guess and a solution, returns the number of hits
# and pseudo-hits.
#
# Approach:
# Finding hits is easy, we can just compare chars in actual and guess and each
# position, if same it's a hit otherwise:
# - We will copy the non hit chars of guess
# - Save the count of non hits in actuals
#
# In iteration, we will scan remaining non hit guess and check if it was present
# in actuals, we will increment pseudo hits and decrement count from actuals
# map.
#
# Complexity:
# O(n), n = length of actual and guess strings


def get_hits_and_pseudo_hits(actual, guess):
    if len(actual) != len(guess):
        return -1
    actual_wo_hits = {}
    guess_wo_hits = []
    hits = 0
    pseudo_hits = 0
    for i in range(len(actual)):
        if actual[i] == guess[i]:
            hits += 1
        else:
            guess_wo_hits.append(guess[i])
            if actual[i] not in actual_wo_hits:
                actual_wo_hits[actual[i]] = 0
            actual_wo_hits[actual[i]] += 1

    for i in range(len(guess_wo_hits)):
        if guess_wo_hits[i] in actual_wo_hits and actual_wo_hits[guess_wo_hits[i]] > 0:
            pseudo_hits += 1
            actual_wo_hits[guess_wo_hits[i]] -= 1
    return hits, pseudo_hits

assert get_hits_and_pseudo_hits('RGBY', 'GGRR') == (1, 1)
assert get_hits_and_pseudo_hits('RGBY', 'RGBY') == (4, 0)
assert get_hits_and_pseudo_hits('RGBY', 'YBGR') == (0, 4)
