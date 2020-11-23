#!/usr/bin/python

# Date: 2020-11-23
#
# Description:
# Write a method to shuffle a deck of cards. It must be a perfect shuffle - 
# in other words, each of the 52! permutations of the deck has to be equally
# likely. Assume that you are given a random number generator which is perfect.
#
# Approach:
# Idea is if we have n - 1 shuffled cards, we can shuffle n cards so:
# - Take one card, shuffle it
# - Take next card and generate random number b/w 0 and 1 and replace current
#   with the number generated
# - And so on, we can replace current card with the random number which is
#   generated
#
# Complexity:
# O(N)

import random

def shuffle_elements(cards):
    for i in range(len(cards)):
        r = random.randint(0, i)
        cards[r], cards[i] = cards[i], cards[r]
    return cards

def main():
    cards = [f'card-{i}' for i in range(52)]
    print(shuffle_elements(cards))

if __name__ == '__main__':
    main()
