/*
 * Date: 2018-10-04
 *
 * Description:
 * We are given two sorted array. We need to merge these two arrays such that
 * the initial numbers (after complete sorting) are in the first array and the
 * remaining numbers are in the second array.
 *
 * Approach:
 * - Save the last element of first array and keep on shifting elements of first
 *   array to right till we find greater element than current element of second
 *   array i.e. ar2[i]
 * - Update ar1 with element found in second array.
 * - Copy saved copy of last element to ar2
 *
 * Complexity:
 * O(M*N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n1 = 0, n2 = 0;
  int *a1 = NULL, *a2 = NULL;
  int num = 0, last = 0;
  printf("Enter number of elements in a1: ");
  scanf("%d", &n1);
  a1 = (int *)malloc(sizeof(int)*n1);
  for (i = 0; i < n1; i++) {
    printf("Enter element a1[%d]: ", i);
    scanf("%d", &a1[i]);
  }

  printf("Enter number of elements in a2: ");
  scanf("%d", &n2);
  a2 = (int *)malloc(sizeof(int)*n2);
  for (i = 0; i < n2; i++) {
    printf("Enter element a2[%d]: ", i);
    scanf("%d", &a2[i]);
  }

  // Iterate through all elements of a2[] starting from the last element
  for (i = n2 -1; i >= 0; i--) {
    last = a1[n1 - 1];

    /*
     * Find the smallest element greater than a2[i]. Move all elements one
     * position ahead till the smallest greater element is not found
     */
    for (j = n1 - 2; (j >= 0 && a1[j] > a2[i]); j--)
      a1[j + 1] = a1[j];

    // If there was a greater element
    if (j != n1 - 2 || last > a2[i]) {
      a1[j + 1] = a2[i];
      a2[i] = last;
    }
  }

  printf ("First Array:\n");
  for (i = 0; i < n1; i++)
    printf("a1[%d]: %d\n", i, a1[i]);
  printf ("\n\nSecond Array:\n");
  for (i = 0; i < n2; i++)
    printf("a2[%d]: %d\n", i, a2[i]);
  return 0;
}


/*
 * Output:
 * -----------------------
 * Enter number of elements in a1: 6
 * Enter element a1[0]: 1
 * Enter element a1[1]: 5
 * Enter element a1[2]: 9
 * Enter element a1[3]: 10
 * Enter element a1[4]: 15
 * Enter element a1[5]: 20
 * Enter number of elements in a2: 4
 * Enter element a2[0]: 2
 * Enter element a2[1]: 3
 * Enter element a2[2]: 8
 * Enter element a2[3]: 13
 * First Array:
 * a1[0]: 1
 * a1[1]: 2
 * a1[2]: 3
 * a1[3]: 5
 * a1[4]: 8
 * a1[5]: 9
 * 
 * 
 * Second Array:
 * a2[0]: 10
 * a2[1]: 13
 * a2[2]: 15
 * a2[3]: 20 
 */
