/*
 * Date: 2018-10-07
 *
 * Description:
 * Given an array of distinct integers, find length of the longest subarray
 * which contains numbers that can be arranged in a continuous sequence. Like:
 *
 * Input:  arr[] = {10, 12, 11}
 * Output: Length of the longest contiguous subarray is 3
 *
 * Input:  arr[] = {14, 12, 11, 20}
 * Output: Length of the longest contiguous subarray is 2
 *
 * Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45}
 * Output: Length of the longest contiguous subarray is 5
 *
 * Approach:
 * As array elements are distinct, we can keep track of min and max for each
 * subarray and check if max - min = diff of last and first index of subarray,
 * it means that subarray can be arranged as contiguous elements.
 *
 * Complexity:
 * O(N^2)
 *
 * Follow up:
 * If duplicates are present in array, then we can use a set and check if an
 * element has already appeared in subarray, then that subarray can't be
 * arranged as array having contigous elements.
 * https://www.geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-2/
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0, min = 0, max = 0, maxlen = 1;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element [%d]: ", i);
    scanf("%d", &a[i]);
  }

  for (i = 0; i < n - 1; i++) {
    min = a[i];
    max = a[i];
    for (j = i + 1; j < n; j++) {
      min = min < a[j] ? min : a[j];
      max = max > a[j] ? max : a[j];
      if (max - min == j - i)
        maxlen = maxlen > j - i + 1 ? maxlen : j - i + 1;
    }
  }
  printf("Max len of sub-array that can be arranged in contiguous order: %d\n",
    maxlen);
  return 0;
}


/*
 * Output:
 * -----------------------------------
 * Enter number of elements: 3
 * Enter element [0]: 10
 * Enter element [1]: 12
 * Enter element [2]: 11
 * Max len of sub-array that can be arranged in contiguous order: 3
 *
 * Enter number of elements: 4
 * Enter element [0]: 14
 * Enter element [1]: 12
 * Enter element [2]: 11
 * Enter element [3]: 20
 * Max len of sub-array that can be arranged in contiguous order: 2
 */ 
