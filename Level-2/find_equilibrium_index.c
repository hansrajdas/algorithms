/*
 * Date: 2018-09-27
 *
 * Description:
 * Find equilibrium index of an array that is sum of elements on left and right
 * side are equal.
 *
 * Like in array [2, 3, 10, 1, 4], 2 is the equilibrium index as sum of elements
 * on left side of a[2] is equal to sum of elements on right side of a[2],
 * mathematically a[0] + a[1] = a[3] + a[4]
 *
 * If not such index is found, return -1.
 *
 * Approach:
 * - Take sum of all array elements, call it sum.
 * - Again start with first element and take temp sum.
 * - In each step subtract temp sum and current element from total sum, if these
 *   are equal then current element's index will be the equilibrium index.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int equilibrium_idx = -1;
  int left_sum = 0, right_sum = 0;
  int sum = 0, tmp_sum = 0;
  int n = 0;
  int *a = NULL;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);

  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
    sum += a[i];
  }

  for (i = 0; i < n; i++) {
    if (tmp_sum == (sum - tmp_sum - a[i])) {
      equilibrium_idx = i;
      break;
    }
    else
      tmp_sum += a[i];
  }
  printf("Equilibrium index is: %d\n", equilibrium_idx);
  return 0;
}

/*
 * Output:
 * -------------------
 * Enter number of elements: 5
 * Enter element[0]: 1
 * Enter element[1]: 3
 * Enter element[2]: 2
 * Enter element[3]: 4
 * Enter element[4]: 0
 * Equilibrium index is: 2
 *
 * Enter number of elements: 5
 * Enter element[0]: 4
 * Enter element[1]: 4
 * Enter element[2]: 10
 * Enter element[3]: 2
 * Enter element[4]: 6
 * Equilibrium index is: 2
 *
 * Enter number of elements: 3
 * Enter element[0]: 100
 * Enter element[1]: 100
 * Enter element[2]: 100
 * Equilibrium index is: 1
 *
 * Enter number of elements: 4
 * Enter element[0]: 4
 * Enter element[1]: 4
 * Enter element[2]: 4
 * Enter element[3]: 4
 * Equilibrium index is: -1
 */
