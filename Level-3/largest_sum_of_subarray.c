/*
 * Date: 2018-10-05
 *
 * Description:
 * Given an unsorted array having positive and negative numbers, find max sum
 * for a subarray. If all elements are negative, show max sum as 0.
 *
 * Approach:
 * Initialize sum so far and max sum with first element of array, scan array
 * from starting and update sum so far, if it becomes negative update it to 0.
 * If sum so far becomes more than max sum, update max sum.
 *
 * This is a standard algorithm called kadane's algorithm to find subarray
 * having maximum sum.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0;
  int *A = NULL;
  int max_sum = 0, sum_so_far = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);

  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  for (i = 0; i < n; i++) {
    sum_so_far += A[i];
    if (0 > sum_so_far)
      sum_so_far = 0;

    if (max_sum < sum_so_far)
      max_sum = sum_so_far;
  }
  printf("Max sum of subarray is: %d\n", max_sum);
  return 0;
}


/*
 * Output:
 * ---------------------------
 * Enter number of elements: 5
 * Enter element[0]: -2
 * Enter element[1]: 3
 * Enter element[2]: 5
 * Enter element[3]: -5
 * Enter element[4]: 7
 * Max sum of subarray is: 10
 *
 * Enter number of elements: 6
 * Enter element[0]: 2
 * Enter element[1]: 3
 * Enter element[2]: 4
 * Enter element[3]: -20
 * Enter element[4]: 2
 * Enter element[5]: 3
 * Max sum of subarray is: 9
 *
 * Enter number of elements: 3
 * Enter element[0]: 3
 * Enter element[1]: 4
 * Enter element[2]: 5
 * Max sum of subarray is: 12
 */
