#!/usr/bin/python

# Date: 2020-12-18
#
# Description:
# A circus is designing a tower routine consisting of people standing atop one
# another's shoulders. For practical and aesthetic reasons, each person must be
# both shorter and lighter than the person below him or her. Given the heights
# and weights of each person in the circus, write a method to compute the
# largest possible number of people in such a tower.
# EXAMPLE
# Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
# Output: The longest tower is length 6 and includes from top to bottom:
# (56, 90) (60, 95) (65, 100) (68, 110) (70, 150) (75, 190)
#
# Approach:
# In simple words, this problem is "Given list of pairs of items. Find the
# longest sequence such that both the first and second items are in
# non-decreasing order."
# - First sort on basis of one param ht or wt, we sorted on ht. This will give
#   us the relative ordering of people.
# - Now, we will recursively check all possibilities and return the one having
#   max number of people. This will take O(2^n) time so we can memoize the
#   computation results and reuse later
#
# Complexity:
# Time: O(nlogn)
# Space: O(n^2)


def first_val(p):
    return p[0]

def best_sequence_at_index(persons, sequence, index, cache):
    if index >= len(persons):
        return sequence
    if index in cache:
        return cache[index]
    best_with = []
    if not sequence or (sequence and sequence[-1][1] < persons[index][1]):
        sequence_with = sequence[:]
        sequence_with.append(persons[index])
        best_with = best_sequence_at_index(persons, sequence_with, index + 1, cache)
    best_without = best_sequence_at_index(persons, sequence, index + 1, cache)

    if len(best_with) > len(best_without):
        cache[index] = best_with
    else:
        cache[index] = best_without
    return cache[index]

def max_persons_in_circus(persons):
    persons.sort(key=first_val)
    sequence = []
    cache = {}
    return best_sequence_at_index(persons, sequence, 0, cache)

def main():
    persons = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
    print(max_persons_in_circus(persons))

main()
