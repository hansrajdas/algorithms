/*
 * Date: 2018-07-15
 *
 * Description:
 * Given a Knapsack of a maximum capacity of W and N items each with its own
 * value and weight, throw in items inside the Knapsack such that the final
 * contents has the maximum value.
 *
 * Approach:
 * Solved using bottom up approach.
 * https://www.hackerearth.com/practice/notes/the-knapsack-problem/
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

int knapsack(int weights[], int values[]) {
  int knapsack[n + 1][W + 1] = {0};
  int item = 0, weight = 0;

  // Building table knapsack using bottom up manner.
  // knapsack[i][j] is the maximum value that can be obtained by using subset of
  // the items 0...i-1 (first i-1) items which weighs at most j pounds.
  for (item = 0; item <= n; item++) {
    for (weight = 0; weight <= W; weight++) {
      // Base case: value of knapsack matrix will be 0 in 2 cases:
      // 1. If there is no item to select, item = 0
      // 2. Weight of knapsack is 0, W = 0
      if (item == 0 || weight == 0)
        knapsack[item][weight] = 0;

      // Current item is selected if current items weight is less than or equal
      // to running weight of knapsack.
      else if (weights[item - 1] <= weight)
        // Take max of 2 things:
        // 1. Value for the same weight without this item.
        // 2. Value of the current item + value that we could accommodate with
        // the remaining weight.
        knapsack[item][weight] = max(
          knapsack[item - 1][weight],
          values[item - 1] + knapsack[item - 1][weight - weights[item - 1]]);

      // Current item is not selected if current items weight is more than
      // running knapsack weight. In this case carry forward the value without
      // current item.
      else
        knapsack[item][weight] = knapsack[item - 1][weight];
    }
  }

  // Print knapsack matrix.
  /*
  for (item = 0; item <= n; item++) {
    for (weight = 0; weight <= W; weight++) {
      printf("%d\t", knapsack[item][weight]);
    }
    printf("\n");
  }
  */
  return knapsack[n][W];
}

int main() {
  int values[n] = {10, 40, 30, 50};
  int wt[n] = {5, 4, 6, 3};
  // int values[n] = {60, 100, 120};
  // int wt[n] = {10, 20, 30};

  printf("Max value with given configuration (W, values and weights) is: %d\n",
    knapsack(wt, values));
  return 0;
}

/*
 * Output:
 *
 * values = {10, 40, 30, 50};
 * wt = {5, 4, 6, 3};
 * With n = 4, W = 10
 * Max value with given knapsack is: 90
 *
 * values = {60, 100, 120}
 * wt = {10, 20, 30};
 * With n = 3, W = 50
 * Max value with given knapsack is: 220
 */
