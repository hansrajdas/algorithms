/*
 * Date: 2018-06-30
 *
 * Description:
 * Length of longest increasing subsequence.
 *
 * Approach:
 * A -> Input array
 * tail -> temp array to store LIS.
 * 1. If A[i] is smallest among all end candidates of active lists (tail), we
 *    will start new active list by inserting A[i] at tail[0].
 * 2. If A[i] is largest among all end candidates of active lists, we will
 *    insert it at end of tail and increment length of LIS by 1.
 * 3. If A[i] is in between, we will find a list with largest end element that
 *    is smaller than A[i].  Clone and extend this list by A[i]. We will discard
 *    all other lists of same length as that of this modified list.
 * 
 * All active lists are maintained using a single array as we only require
 * length of LIS not elements in LIS.
 *
 * Reference:
 * https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
 *
 * Complexity:
 * Time - O(n*logn), space: O(n)
 */

#include "stdio.h"
#include "stdlib.h"

int ceil_index(int *array, int l, int r, int key) {
  int m = 0;
  while (r - l > 1) {
    m = l + (r - l)/2;
    if (array[m] >= key)
      r = m;
    else
      l = m;
  }
  return r;
}

int main() {
  int i = 0;
  int num_of_elements = 0;
  int *p_input = NULL, *tail = NULL;
  int length = 1;
  
  printf("Enter number of elements: ");
  scanf("%d", &num_of_elements);
  p_input = (int *)malloc(sizeof(int) * num_of_elements);
  tail = (int *)malloc(sizeof(int) * num_of_elements);

  for (i = 0; i < num_of_elements; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &p_input[i]);
  }

  tail[0] = p_input[0];
  for (i = 1; i < num_of_elements; i++) {
    // If current element is larger than last element in LIS array (tail) then
    // increment length of LIS.
    // If current element is smaller than first element in tail, replace first
    // element in tail with new smallest (this new smallest may start a new and
    // longer LIS).
    // If current element is in between tail[0] and tail[last] then find correct
    // index (using binary search) where current element should be stored as
    // this can also create a new and longer LIS.
    if (tail[0] > p_input[i])
      tail[0] = p_input[i];
    else if (tail[length - 1] < p_input[i])
      tail[length++] = p_input[i];
    else
      tail[ceil_index(tail, -1, length - 1, p_input[i])] = p_input[i];
  }
  printf("LIS length is %d.\n", length);
  return 0;
}
