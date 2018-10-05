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
