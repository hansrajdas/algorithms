#!/usr/bin/python

# Date: 2020-11-21
#
# Description:
# Implement a method rand7() given rand5(). That is, given a method that
# generates a random number between 0 and 4(inclusive), write a method that
# generates a random number between 0 and 6(inclusive).
#
# Approach:
# Problem to solve here is to map numbers from 0 to 4 to 0 to 6 so that numbers
# generated b/w 0 to 6 are equally likely. To achieve this we can generate a
# range of values where each value is equally likely(and where the range has at
# least 7 elements - 0 to 24). If we can do this, we can discard(21 to 24) the
# elements greater than the previous multiple of 7, and mod the rest of them by
# 7. This will get us a value within the range 0 to 6, with each value being
# equally likely.
#
# In code, we generate the range 0 to 24 by 5 * rand5() + rand5(). Them we
# discard the values b/w 21 to 24, since they would otherwise make rand7()
# unfairly weighted towards 0 through 3.
#
# 5 * rand5() + rand5() gives us exactly one way of getting each number in its
# range (0 to 24). This ensures that each value(0 to 6) is equally probable.
# 
# rand5    5 * rand5    5 * rand5 + rand5(based on this rand5, we can have 5 values)
# -----------------------------------------------------------------------------
#   0        0          0, 1, 2, 3, 4
#   1        5          5, 6, 7, 8, 9
#   2        10         10, 11, 12, 13, 14
#   3        15         15, 16, 17, 18, 19
#   4        20         20, 21, 22, 23, 24
#
# Numbers 0 to 20 when moded with 7 will give numbers 0 to 6 so we will have to
# ignore 21, 22, 23 and 24 to maintain the equal probability
#
# Complexity:
# -


import random
import time

def rand5():
    return random.randint(0, 5)

def rand7():
    while True:
        num = 5 * rand5() + rand5()
        if num < 21:
            return num % 7

def main():
    while True:
        print(rand7())
        time.sleep(0.5)


if __name__ == '__main__':
    main()
