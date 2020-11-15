#!/usr/bin/python

# Date: 2020-11-15
#
# Description:
# You are building a diving board by picking a bunch of planks of wood end to
# end. There are two types of planks. One of length shorter and one of length
# longer. You ust use exactly K planks of wood. Write a method to generate all
# possible lengths of diving board.
#
# Approach:
# For each value of k we can either select:
# - i shorter and (k - i) longer planks OR
# - (k - i) shorter and i longer planks
#
# So we can keep on generating all possible lengths using above fact for each
# value of k
#
# Complexity:
# O(k)


def get_all_lengths(k, current_len, shorter, longer):
    lengths = []
    for i in range(k + 1):
        length = i * shorter + (k - i) * longer
        lengths.append(length)
    return lengths

def main():
    print(get_all_lengths(1, 0, 2, 5))

    print(get_all_lengths(2, 0, 2, 5))

    print(get_all_lengths(10, 0, 2, 50))


if __name__ == '__main__':
    main()
