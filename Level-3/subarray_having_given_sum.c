/*
 * Date: 2018-09-29
 *
 * Description:
 * Given an array having positive numbers, find a sub array having given sum
 *
 * Approach:
 * Traverse array from starting to end, keep track of sum so far. If sum is
 * more than given sum, subtract elements from beginning of array till current
 * sum becomes less than required sum.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  int j = 0;
  int sum = 0;
  int curr_sum = 0;
  int start_idx = 0;
  
  printf("Enter required sum: ");
  scanf("%d", &sum);

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }
  curr_sum = a[0];
  for (i = 1; i <= n; i++) {
    while (curr_sum > sum && start_idx < i - 1) {
      curr_sum -= a[start_idx];
      start_idx += 1;
    }

    if (curr_sum == sum) {
      printf("\nSubarray having given sum: index from %d to %d\n",
        start_idx, i - 1);
    }
    if (i < n) {
      curr_sum += a[i];
    }
  }
  return 0;
}
