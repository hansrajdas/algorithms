/*
 * Date: 2018-11-07
 *
 * Description:
 * Given an array of 0s and 1s, find the position of 0 to be replaced with 1 to
 * get longest continuous sequence of 1s.
 *
 * Approach:
 * The idea is to keep track of three indexes, current index (curr), previous
 * zero index (prev_zero) and previous to previous zero index (prev_prev_zero).
 * Traverse the array, if current element is 0, calculate the difference between
 * curr and prev_prev_zero (This difference minus one is the number of 1s around
 * the prev_zero). If the difference between curr and prev_prev_zero is more
 * than maximum so far, then update the maximum.
 * Finally return index of the prev_zero with maximum difference.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int curr_index = 0;
  int n = 0;
  int prev_zero = -1;
  int prev_prev_zero = -1;
  int max_count = 0;
  int max_indx = -1;
  int *A = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int)*n);
  for (curr_index = 0; curr_index < n; curr_index++) {
    printf("Enter element[%d]: ", curr_index);
    scanf("%d", &A[curr_index]);
  }

  // If current element is 0, then calculate the difference between curr and
  // prev_prev_zero
  for (curr_index = 0; curr_index < n; curr_index++) {
    if (0 == A[curr_index]) {
      if (curr_index - prev_prev_zero > max_count) {
        max_count = curr_index - prev_prev_zero;
        max_indx = prev_zero;
      }
      prev_prev_zero = prev_zero;
      prev_zero = curr_index;
    }
  }

  // Check for last encountered 0
  if (n - prev_prev_zero > max_count)
    max_indx = prev_zero;
  printf("Index of 0 to be changed to 1 for longest sequence of 1 is: %d\n",
      max_indx);
  return 0;
}


/*
 * Output:
 * ------------------
 * Enter number of elements: 5
 * Enter element[0]: 1
 * Enter element[1]: 1
 * Enter element[2]: 1
 * Enter element[3]: 1
 * Enter element[4]: 0
 * Index of 0 to be changed to 1 for longest sequence of 1 is: 4
 *
 * Enter number of elements: 4
 * Enter element[0]: 1
 * Enter element[1]: 1
 * Enter element[2]: 0
 * Enter element[3]: 1
 * Index of 0 to be changed to 1 for longest sequence of 1 is: 2
 *
 * Enter number of elements: 5
 * Enter element[0]: 1
 * Enter element[1]: 1
 * Enter element[2]: 0
 * Enter element[3]: 1
 * Enter element[4]: 0
 * Index of 0 to be changed to 1 for longest sequence of 1 is: 2 
 */
