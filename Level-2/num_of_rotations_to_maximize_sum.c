/*
 * Date: 2018-10-21
 *
 * Description:
 * Given an array, find the number of right rotations required to maximize
 * sum(i*a[i])
 *
 * Approach:
 * With simple mathematics equations, we can develop below recurrence relation:
 *                 Ri = Ri-1 + array_sum - n*a[n - i]
 * where Ri is sum(i*a[i]) after i right rotations.
 *
 * So we can first iterate over all array elements and find array_sum and R0.
 * Then in another loop we can check all values of Ri, i = 1 to n - 1.
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
  int arr_sum = 0;
  int R_i = 0, max_sum = 0, num_of_rot = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
    R_i += i*A[i];  // Compute R_0, sum(i*a[i]) after 0 right rotations
    arr_sum += A[i];
  }

  max_sum = R_i;
  for (i = 1; i < n; i++) {
    /*
     * Relation was developed for Ri - Ri-1 = arr_sum - n*a[n - i]
     * Ri is sum(i*a[i]) after i right rotations
     * Ri-1 is sum(i*a[i]) after i-1 right rotations
     */
    R_i = arr_sum - n*A[n - i] + R_i;
    if (R_i > max_sum) {
      max_sum = R_i;
      num_of_rot = i;
    }
  }
  printf("Number of rotations[%d], Max sum[%d]\n", num_of_rot, max_sum);
  return 0;
}


/*
 * Output:
 * ------------------
 * Enter number of elements: 5
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Enter element[4]: 5
 * Number of rotations[0], Max sum[40]
 *
 * Enter number of elements: 5
 * Enter element[0]: 4
 * Enter element[1]: 3
 * Enter element[2]: 2
 * Enter element[3]: 1
 * Enter element[4]: 0
 * Number of rotations[2], Max sum[25] 
 */
