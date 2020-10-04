# Date: 2020-10-04
#
# Description:
# In a variant of the Knapsack problem, all the items in the vault are gold
# bars. The value of a gold bar is directly proportional to its weight.
# Therefore, in order to make the most amount of money, you must fill your
# knapsack up to its full capacity of W pounds. Can you find a subset of the
# gold bars whose weights add up to exactly W? If not what is max weight that
# we can accommodate.
#
# Approach:
# Same as knapsack(Level-4/knapsack.py) with small variation - we have to take
# care item values here
#
# Complexity:
# Time: O(n*W), Space(n*W)
# This is polynomial (in fact linear as exponent is 1, n^1) in terms in input
# size n but exponential in terms of W, so this is called pseudo polynomial.
#
# Pseudo polynomial behavior is explained here:
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec21.pdf


def knapsack_maximize_weight(weights, W):
    n = len(weights)
    dp = [[None] * (W + 1) for _ in range(n + 1)]

    for item in range(n + 1):
        for weight in range(W + 1):
            if not item:  # No items
                dp[item][weight] = 0
            elif not weight:  # Weight of given knapsack is 0
                dp[item][weight] = 0
            elif weights[item - 1] <= weight:  # Can current item be accommodated in current knapsack size (weight).
                dp[item][weight] = max(
                    dp[item - 1][weight],
                    weights[item - 1] + dp[item - 1][weight - weights[item - 1]])
            else:
                dp[item][weight] = dp[item - 1][weight]

    return dp[item][W]

assert knapsack_maximize_weight([5, 4, 6, 3], 10) == 10
assert knapsack_maximize_weight([10, 20, 30], 50) == 50
assert knapsack_maximize_weight([10, 20, 30], 55) == 50
assert knapsack_maximize_weight([10, 20, 30], 65) == 60
