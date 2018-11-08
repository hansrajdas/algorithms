/*
 * Date: 2018-11-08
 *
 * Description:
 * Given a binary array, find the maximum number zeros in an array with one flip
 * of a subarray allowed. A flip operation switches all 0s to 1s and 1s to 0s.
 *
 * Approach:
 * This problem can be reduced to largest subarray sum problem. The idea is to
 * consider every 0 as -1 and every 1 as 1, find the sum of largest subarray sum
 * in this modified array. This sum is our required
 * max_diff(count of 1s - count of 0s in any subarray). Finally we return the
 * max_diff plus count of zeros in original array.
 *
 * Complexity:
 * O(N)
 *
 * Reference:
 * https://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0;
  int *a = NULL;
  int orig_zeros = 0, max_1_0_diff = 0;
  int curr_max = 0, val = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for(i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }
  for(i = 0; i < n; i++) {
    if (!a[i])
      orig_zeros++;

    val = a[i] ? 1 : -1;
    curr_max = (val < curr_max + val) ? (curr_max + val) : val;
    max_1_0_diff = (curr_max < max_1_0_diff) ? max_1_0_diff : curr_max;
  }
  printf("Max 0's after subarray flip is: %d\n", (orig_zeros + max_1_0_diff));
  return 0;
}


/*
 * Output:
 * ------------------------
 * Enter number of elements: 7
 * Enter element[0]: 0
 * Enter element[1]: 1
 * Enter element[2]: 0
 * Enter element[3]: 0
 * Enter element[4]: 1
 * Enter element[5]: 1
 * Enter element[6]: 0
 * Max 0's after subarray flip is: 6
 *
 * Enter number of elements: 6
 * Enter element[0]: 0
 * Enter element[1]: 0
 * Enter element[2]: 0
 * Enter element[3]: 1
 * Enter element[4]: 0
 * Enter element[5]: 1
 * Max 0's after subarray flip is: 5
 */
