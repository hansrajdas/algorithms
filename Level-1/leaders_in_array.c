/*
 * Date: 2018-09-27
 *
 * Description:
 * Print all leaders in array. Leaders are elements which are greater than all
 * elements at it's right
 *
 * Approach:
 * Scan from last and keep track of max, if new max occurs, print that.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0, max = 0;
  int *a = NULL;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  // Keep track of max, print and update max if new max is seen while scanning
  // from right to left.
  max = a[n - 1];
  printf("%d ", max);
  for (i = n - 2; i >= 0; i--) {
    if (a[i] > max) {
      printf("%d ",a[i]);
      max = a[i];
    }
  }
  printf("\n");
  return 0;
}
