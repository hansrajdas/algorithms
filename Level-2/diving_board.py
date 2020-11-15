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
# At any point of time(util we use k planks) we have 2 options, pick shorter
# or longer plank. We can make recursive calls until we are exausted with all
# planks.
#
# Complexity:
# O(2^k)
#
# Note:
# This can be optimized to memoize data across function calls we will have
# repeated calls. Memoization key should be based on (current_len, k).
# This optimization will reduce complexity from exponential to quadratic.


def get_all_lengths(k, current_len, shorter, longer, response):
    if not k:
        response.add(current_len)
        return
    get_all_lengths(k - 1, current_len + shorter, shorter, longer, response)
    get_all_lengths(k - 1, current_len + longer, shorter, longer, response)

def main():
    response = set()
    get_all_lengths(1, 0, 2, 5, response)
    print(response)

    response = set()
    get_all_lengths(2, 0, 2, 5, response)
    print(response)

    response = set()
    get_all_lengths(10, 0, 2, 50, response)
    print(response)


if __name__ == '__main__':
    main()
