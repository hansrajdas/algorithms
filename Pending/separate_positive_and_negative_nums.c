/*
 * Date: 2018-
 *
 * Description:
 * Given an array having positive and negative numbers, separate positive and
 * negative numbers. Update array such that first we have all positive numbers
 * then negatives, 0s should be with positive numbers.
 * Like if array is [-2, 0, -4, 9, -3, 4]
 * Output array should be: [0, 9, 4, -2, -3, -4] or in other order but first
 * positives/zeros and then negatives.
 * 
 * Approach:
 *
 * Complexity:
 * O(n)
 */

#include "stdio.h"
#include "stdlib.h"

void printArray(int arr[], int n, char *msg) {
  int i = 0;
  printf("*********** %s *****************\n", msg);
  for (i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n\n");
}

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++)
  {
    printf("Enter element [%d]: ", i);
    scanf("%d",&a[i]);
  }
  printArray(a, n, "Inserted Array");
  return 0;
}
