/*
 * Date: 2018-10-13
 *
 * Description:
 * Given an unsorted array of integers, find max product of a subarray.
 *
 * Approach:
 * - Scan array and keep track of max-ending-here and min-ending-here.
 * - If current element is 0, both will be initialised again to 1.
 * - If current element is positive, max-eh will product of max-eh and current
 *   element and min-en will be 1 if min-eh * current-element is positive
 *   otherwise min-eh * current-element.
 * - If current element is negative, max-eh will min-eh * current if it is
 *   positive otherwise 1 and min-eh will be max-eh * current.
 * - And end check if max product calculated so far is less than max-eh then
 *   update max product.
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
  int max_ending_here = 1,  // Holds 1 or max(positive) product till scanned
      min_ending_here = 1,  // Holds 1 or min(negative) product till scanned
      max_so_far = 1,
      tmp = 1;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  for (i = 0; i < n; i++) {
    if (!a[i]) {
      max_ending_here = 1;
      min_ending_here = 1;
    }
    else if (a[i] > 0) {
      max_ending_here *= a[i];
      min_ending_here = min_ending_here * a[i] > 0 ? 1 : min_ending_here * a[i];
    }
    else {
      tmp = max_ending_here;
      max_ending_here = min_ending_here * a[i] > 0 ? min_ending_here * a[i] : 1;
      min_ending_here = tmp * a[i];
    }
    if (max_so_far < max_ending_here)
      max_so_far = max_ending_here;
  }
  printf("Max prod of subarray is: %d\n", max_so_far);
  return 0;
}


/*
 * Output:
 * ---------------------------
 * Enter number of elements: 5
 * Enter element[0]: 2
 * Enter element[1]: 3
 * Enter element[2]: -4
 * Enter element[3]: 5
 * Enter element[4]: 1
 * Max prod of subarray is: 6
 *
 * Enter number of elements: 6
 * Enter element[0]: 2
 * Enter element[1]: 3
 * Enter element[2]: 4
 * Enter element[3]: 0
 * Enter element[4]: 10
 * Enter element[5]: 2
 * Max prod of subarray is: 24
 */ 
