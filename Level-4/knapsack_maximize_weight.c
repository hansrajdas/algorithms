/*
 * Date: 2018-07-16
 *
 * Description:
 * In a variant of the Knapsack problem, all the items in the vault are gold
 * bars. The value of a gold bar is directly proportional to its weight.
 * Therefore, in order to make the most amount of money, you must fill your
 * knapsack up to its full capacity of W pounds. Can you find a subset of the
 * gold bars whose weights add up to exactly W?
 *
 * Approach:
 * Same as knapsack(Level-4/knapsack.c) with small variation - we have to take
 * care item values here
 *
 * Complexity:
 * Time: O(n*W), Space(n*W)
 * This is polynomial (in fact linear as exponent is 1, n^1) in terms in input
 * size n but exponential in terms of W, so this is called pseudo polynomial.
 *
 * Pseudo polynomial behavior is explained here:
 * https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec21.pdf
 */

#include "stdio.h"

#define n 4
#define W 10
// #define n 3
// #define W 50

int max (int A, int B) {
  return A > B ? A : B;
}

int knapsack_maximize_weight(int weights[]) {
  int knapsack[n + 1][W + 1];
  int item = 0, weight = 0;

  // Solved using bottom up manner.
  // knapsack[i][j] represents max weight (upto j) achieved using items from
  // 0 to i - 1.
  // As first column row and column of knapsack matrix is used as base condition
  // knapsack taken is of size (n + 1) * (W + 1) and current items are accessed
  // using item - 1.
  for (item = 0; item <= n; item++) {
    for (weight = 0; weight <= W; weight++) {
      // Base condition: If no item is present or weight of knapsack is 0.
      if (!item || !weight)
          knapsack[item][weight] = 0;
      // Can current item be accommodated in current knapsack size (weight).
      else if (weights[item - 1] <= weight)
        knapsack[item][weight] = max(
            knapsack[item - 1][weight],
            weights[item - 1] + knapsack[item - 1][weight - weights[item - 1]]);
      else
        knapsack[item][weight] = knapsack[item - 1][weight];
    }
  }
  return knapsack[n][W];
}

int main() {
  int wt[n] = {5, 4, 6, 3};
  // int wt[n] = {10, 20, 30};

  printf("Max weight with given configuration (W and weights) is: %d\n",
    knapsack_maximize_weight(wt));
  return 0;
}

/*
 * Output:
 *
 * wt = {5, 4, 6, 3}, n = 4, W = 10
 * Max weight with given configuration (W and weights) is: 10
 *
 * wt = {10, 20, 30}, n = 3, W = 50
 * Max weight with given configuration (W and weights) is: 50
 */
