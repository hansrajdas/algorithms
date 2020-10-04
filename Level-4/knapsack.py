# Date: 2020-10-04
#
# Description:
# Given a Knapsack of a maximum capacity of W and N items each with its own
# value and weight, throw in items inside the Knapsack such that the final
# contents has the maximum value.
#
# Approach:
# Solved using bottom up approach.
# https://www.hackerearth.com/practice/notes/the-knapsack-problem/
#
# Complexity:
# Time: O(n*W), Space(n*W)
# This is polynomial (in fact linear as exponent is 1, n^1) in terms in input
# size n but exponential in terms of W, so this is called pseudo polynomial.
#
# Pseudo polynomial behavior is explained here:
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec21.pdf


def knapsack(weights, values, W):
    """
    Returns max knapsack value that can be generated using given list of
    weights and values.
    """
    assert len(weights) == len(values)
    n = len(weights)  # Number of items
    dp = [[None] * (W + 1) for _ in range(n + 1)]

    for item in range(n + 1):
        for weight in range(W + 1):
            if not item:  # If we don't select any item so value will always be 0
                dp[item][weight] = 0
            elif not weight:  # If knapsack weight is 0 -> no item can be accomodated so value should be 0
                dp[item][weight] = 0
            elif weights[item - 1] <= weight:  # Current item can be accomodated
                # Take max of 2 things:
                # 1. Value for the same weight without this item.
                # 2. Value of the current item + value that we could accommodate with
                # the remaining weight.
                dp[item][weight] = max(
                    dp[item - 1][weight],
                    values[item - 1] + dp[item - 1][weight - weights[item - 1]])
            else:
                dp[item][weight] = dp[item - 1][weight]  # Can't accomodate current item, carry forward value without this item
    return dp[item][weight]


assert knapsack([5, 4, 6, 3], [10, 40, 30, 50], 10) == 90
assert knapsack([10, 20, 30], [60, 100, 120], 50) == 220
