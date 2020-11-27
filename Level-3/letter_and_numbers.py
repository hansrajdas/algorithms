#!/usr/bin/python

# Date: 2020-11-27
#
# Description:
# Given an array filled with letters and numbers, find the longest subarray
# with an equal number of letters and numbers.
#
# Approach:
# Scan given array and create another delta array which has difference of
# number of numbers seen and number of letters seen till a given index.
# Then, we will scan delta array to find same difference at 2 indices which are
# max indices apart.
#
# Complexity:
# O(N) time and space


def get_delta_subarray(s):
    delta = 0
    delta = 0
    delta_list = []
    for x in s:
        if x.isdigit():
            delta += 1
        else:
            delta -= 1
        delta_list.append(delta)
    return delta_list

def get_longest_match(delta):
    delta_to_indices = {0: -1}
    res = {
        'start': 0,
        'end': 0
    }
    for i in range(len(delta)):
        if delta[i] not in delta_to_indices:
            delta_to_indices[delta[i]] = i
        else:
            start = delta_to_indices[delta[i]]
            longest = res['end'] - res['start']
            if i - start > longest:
                res['start'] = start
                res['end'] = i
    return res

def get_subarray(string, indices):
    s = []
    for i in range(indices['start'] + 1, indices['end'] + 1):
        s.append(string[i])
    return s

def max_subarray_same_letters_and_nums(s):
    delta = get_delta_subarray(s)
    max_indices = get_longest_match(delta)
    return get_subarray(s, max_indices)

print(max_subarray_same_letters_and_nums('abc112345d'))
print(max_subarray_same_letters_and_nums('aaaa11a11aa1aa1aaaaa'))
