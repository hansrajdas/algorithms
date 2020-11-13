#!/usr/bin/python

# Date: 2020-11-13
#
# Description:
# Compute number of trailing 0s in n factorial.
#
# Approach:
# 0s in factorial of a number is contributed by multiple of 5s present in that
# number so we can find number of trailing 0s by n // 5. We also has to
# consider cases when we have number like 25, this is multiple of 5 by 2 folds.
# So actual count would be: n // 5 + log(n), log with base 5
#
# Simplified way would be to keep on dividing number by 5^i till we are getting
# non zero result
#
# Complexity:
# O(log(n)), log with base 5


def factorial_trailing_zeros(n):
    if n < 0:
        return -1
    count = 0
    i = 5
    while n // i:
        count += n // i
        i *= 5
    return count

assert factorial_trailing_zeros(-9) == -1
assert factorial_trailing_zeros(9) == 1
assert factorial_trailing_zeros(5) == 1
assert factorial_trailing_zeros(10) == 2
assert factorial_trailing_zeros(11) == 2
assert factorial_trailing_zeros(25) == 6
