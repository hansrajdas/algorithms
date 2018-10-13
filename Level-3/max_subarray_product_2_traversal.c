/*
 * Date: 2018-10-13
 *
 * Description:
 * Given an unsorted array of integers, find max product of a subarray.
 *
 * Approach:
 * Find max product of whole array while scanning in forward and backward
 * direction. Max subarray product would be max of 2.
 * Also, whenever 0 is encountered while scanning, reset max-so-far to 1.
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
  int max_fwd = 1, max_bkwd = 1, max_so_far = 1;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  // Max product while traversing in forward direction
  for (i = 0; i < n; i++) {
    max_so_far = max_so_far * a[i];
    if (!max_so_far)
      max_so_far = 1;

    max_fwd = max_so_far > max_fwd ? max_so_far : max_fwd;
  }
  printf("max_fwd: %d\n", max_fwd);

  // Max product while traversing in backward direction
  max_so_far = 1;
  for (i = n - 1; i >=0; i--) {
    max_so_far = max_so_far * a[i];
    if (!max_so_far)
      max_so_far = 1;

    max_bkwd = max_so_far > max_bkwd ? max_so_far : max_bkwd;
  }
  printf("max_bkwd: %d\n", max_bkwd);

  printf("Maximum product of subarray is: %d\n",
    max_fwd > max_bkwd ? max_fwd : max_bkwd);
  return 0;
}


/*
 * Output:
 * -----------------------
 * Enter number of elements: 5
 * Enter element[0]: 5
 * Enter element[1]: -2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Enter element[4]: 5
 * max_fwd: 5
 * max_bkwd: 60
 * Maximum product of subarray is: 60 
 */
