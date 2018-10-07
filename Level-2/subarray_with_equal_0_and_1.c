/*
 * Date: 2018-10-07
 *
 * Description:
 * Given an unsorted array of 0s and 1s, find the largest subarray having equal
 * number of 0s and 1s.
 *
 * Approach:
 * Consider all possible subarrays, track 0s and 1s using sum(1 as 1 and
 * 0 as -1). When sum becomes 0 it means we have equal number of 0s and 1s, now
 * check if it's length is more than last computed, update start index and size.
 *
 * Complexity:
 * O(N^2)
 *
 * Note:
 * There is O(N) solution also for this problem at geeksforgeeks, not clear :(
 * Check second solution - https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0;
  int *a = NULL;
  int sum = 0, start_idx = -1, size = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  for (i = 0; i < n - 1; i++) {
    sum = a[i] ? 1 : -1;
    for (j = i + 1; j < n; j++) {
      sum += a[j] ? 1 : -1;
      if (!sum && size < j - 1) {
        start_idx = i;
        size = j - i;
      }
    }
  }

  if (!size)
    printf("None\n");
  else
    printf("Start index[%d], End index[%d]\n", start_idx, size);
  return 0;
}


/*
 * Output:
 * -----------------------------------------
 * Enter number of elements: 6
 * Enter element[0]: 0
 * Enter element[1]: 0
 * Enter element[2]: 0
 * Enter element[3]: 1
 * Enter element[4]: 1
 * Enter element[5]: 1
 * Start index[0], End index[5]
 *
 * Enter number of elements: 5
 * Enter element[0]: 1 
 * Enter element[1]: 0
 * Enter element[2]: 1
 * Enter element[3]: 0
 * Enter element[4]: 1
 * Start index[0], End index[3] 
 */
