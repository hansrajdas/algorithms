/*
 * Date: 2018-10-06
 *
 * Description:
 * Given 2 sorted arrays arr1 and arr2 having distinct elements, find if arr2
 * is subset of arr1. arr2 will considered subset of arr1 if arr1 contains all
 * elements of arr2.
 *
 * Approach:
 * Scan array linearly keeping track of index of smaller and larger array.
 * If current element is same increment both indexes,
 * If element at arr1 is smaller increment index of first array
 * Otherwise if arr1 element becomes more than of arr2, arr2 can't be subset of
 * arr1.
 *
 * Complexity:
 * O(N), N = Number of elements in longer elements.
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n1 = 0, n2 = 0;
  int *arr1 = NULL, *arr2 = NULL;

  printf("Enter number of elements in first array, arr1: ");
  scanf("%d", &n1);
  arr1 = (int *)malloc(sizeof(int) * n1);
  for (i = 0; i < n1; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &arr1[i]);
  }
  printf("Enter number of elements in second array, arr2: ");
  scanf("%d", &n2);
  arr2 = (int *)malloc(sizeof(int) * n2);
  for (i = 0; i < n2; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &arr2[i]);
  }

  i = 0;
  j = 0;
  while ((i < n1) && (j < n2)) {
    if (arr1[i] == arr2[j]) {
      i++;
      j++;
    }
    else if (arr1[i] < arr2[j])
      i++;
    else {
      printf("arr2 is not subset of arr1\n");
      return 0;
    }
  }
  if (j < n2)
    printf("j < n2, arr2 is not subset of arr1\n");
  else
    printf("arr2 is subset of arr1\n");
  return 0;
}


/*
 * Output:
 * --------------
 * Enter number of elements in first array, arr1: 6
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Enter element[4]: 5
 * Enter element[5]: 6
 * Enter number of elements in second array, arr2: 3
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 4
 * arr2 is subset of arr1
 */
