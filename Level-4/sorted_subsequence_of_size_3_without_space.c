/*
 * Date: 2018-09-28
 *
 * Description:
 * Given an array of n integers, find the 3 elements such that
 * a[i] < a[j] < a[k] and i < j < k. If there are multiple such triplets, then
 * print any one of them.
 *
 * Approach:
 * In first loop find a smaller(min) and second smaller(mid) number, If a more
 * than both appears, break the loop. Now we have mid and max element we need
 * to find a min element which on left side of mid and max. Again run a loop
 * till i to find element smaller than larger.
 *
 * Complexity:
 * O(N) Time
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0;
  int *A = NULL;
  int small = 1 << 30;
  int large = 1 << 30;

  printf("Enter number of elements: ");
  scanf("%d", &n);

  A = (int *)malloc(sizeof(int) * n);

  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  for (i = 0; i < n; i++) {
    // Track smallest element
    if (small >= A[i])
      small = A[i];

    // Track second largest element
    else if (large >= A[i])
      large = A[i];
    else
      break;
  }

  if (i == n) return -1;

  for (j = 0; j <= i; j++) {
    // Find smaller element which appears on left of larger and A[i]
    if (large >= A[j]) {
      small = A[j];
      break;
    }
  }
  printf("3 sorted values are: %d %d %d\n", small, large, A[i]);
  return 0;
}


/*
 * Output:
 * ----------------
 * Enter number of elements: 5
 * Enter element[0]: 4
 * Enter element[1]: 7
 * Enter element[2]: 2
 * Enter element[3]: 9
 * Enter element[4]: 1
 * 
 * 3 sorted elements are: 4 7 9
 */ 
