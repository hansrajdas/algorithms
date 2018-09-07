/*
 * Date: 2018-
 *
 * Description:
 * Given 2 sorted arrays find overall median.
 * 
 * Approach:
 *
 * Complexity:
 * O(log(...))
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
