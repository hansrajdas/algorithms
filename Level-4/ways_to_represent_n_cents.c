/*
 * Date: 2018-08-06
 *
 * Description:
 * Given an infinite number of quarters (25 cents), dimes (10 cents), nickels
 * (5 cents) and pennies (1 cent). Write a program to calculate the number of
 * ways  of representing n cents.
 *
 * Approach:
 * ...
 *
 * Complexity:
 * O(n * NUM_OF_DENOMS)
 */

#include "stdio.h"
#include "stdlib.h"

#define MAX_DENOMS 4

int makeChange(int amount, int denoms[], int index, int **map) {
  int i = 0, ways = 0;
  int amountRemaining = amount;
  int currentDenomAmount = 0;
  
  // Only pennies left so there can be only one way - 1*amount.
  if (index >= MAX_DENOMS - 1)
    return 1;

  if (map[amount][index])
    return map[amount][index];

  currentDenomAmount = denoms[index];
  for (i = 0; i*currentDenomAmount <= amount; i++) {
    amountRemaining = amount - i*currentDenomAmount;
    
    // Go to next denom, i coins of current denom used.
    ways += makeChange(amountRemaining, denoms, index + 1, map);
  }
  map[amount][index] = ways;
  return ways;
}

int main() {
  int i = 0, j = 0;
  int amount = 0;
  int denoms[MAX_DENOMS] = {
    25,  // Quarters
    10,  // Dimes
    5,  // Nickels
    1  // Pennies
  };
  int **map = NULL;
  printf("Enter amount: ");
  scanf("%d", &amount);

  // Allocate memory for map.
  map = (int **)malloc(sizeof(int *) * (amount + 1));
  for (i = 0; i < amount + 1; i++)
    map[i] = (int *)malloc(sizeof(int) * MAX_DENOMS);

  // Initialize map with all 0s.
  for (i = 0; i < amount + 1; i++) {
    for (j = 0; j < MAX_DENOMS; j++)
      map[i][j] = 0;
  }

  printf("Ways to represent %d in denoms is: %d\n",
    amount, makeChange(amount, denoms, 0, map));
  return 0;
}

/*
Output:

Enter amount: 1
Ways to represent 1 in denoms is: 1

Enter amount: 4
Ways to represent 4 in denoms is: 1

Enter amount: 5
Ways to represent 5 in denoms is: 2

Enter amount: 10
Ways to represent 10 in denoms is: 4

Enter amount: 50
Ways to represent 50 in denoms is: 49

Enter amount: 98
Ways to represent 98 in denoms is: 213

Enter amount: 550
Ways to represent 550 in denoms is: 25004

Enter amount: 10000
Ways to represent 10000 in denoms is: 134235101
*/
