/*
 * Date: 2018-11-08
 *
 * Description:
 * Given a binary array, find the maximum number zeros in an array with one flip
 * of a subarray allowed. A flip operation switches all 0s to 1s and 1s to 0s.
 *
 * Approach:
 * - Count number of 0s in original array, call it orig_zeros.
 * - Consider all subarrays and find subarary having maximum difference count of
 *   1s and 0s, this is the subarray which needs to be swapped to get max 0s.
 * - Result would be sum of orig_zeros and max(count_1 - count_0).
 *
 * Complexity:
 * O(N^2)
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
  int count0 = 0, count1 = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }
  for (i = 0; i < n; i++) {
    count1 = 0;
    count0 = 0;
    if (!a[i])
      orig_zeros++;
    for (j = i; j < n; j++) {
      (!a[j]) ? count0++ : count1++;
      max_1_0_diff = (max_1_0_diff > count1 - count0) ? max_1_0_diff : count1 - count0;
    }
  }
  printf("Max 0's after subarray flip is: %d\n", (orig_zeros + max_1_0_diff));
  return 0;
}


/*
 * Output:
 * ---------------
 * Enter number of elements: 9
 * Enter element[0]: 0
 * Enter element[1]: 1
 * Enter element[2]: 0
 * Enter element[3]: 0
 * Enter element[4]: 1
 * Enter element[5]: 1
 * Enter element[6]: 0
 * Enter element[7]: 1
 * Enter element[8]: 1
 * Max 0's after subarray flip is: 7
 */
