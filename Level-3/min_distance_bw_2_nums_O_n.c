/*
 * Date: 2018-10-29
 *
 * Description:
 * Given an unsorted array and 2 numbers, find the minimum distance between 2
 * given numbers in array.
 *
 * Approach:
 * - Scan array and find any of the 2 element, once found save the index and
 *   break from loop.
 * - Now scan array further and check if any of the 2 element appears again, if
 *   it is same as at saved index, updated index to new index
 * - otherwise check if min distance is less than previously saved update that
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
  int first = 0, second = 0, prev_idx = 0;
  int min_dist = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }
  printf("Enter first number: ");
  scanf("%d", &first);

  printf("Enter second number: ");
  scanf("%d", &second);

  min_dist = n - 1;
  for (i = 0; i < n; i++) {
    if ((a[i] == first) || (a[i] == second)) {
      prev_idx = i;
      break;
    }
  }
  for (; i < n; i++) {
    if (a[i] == first || a[i] == second) {
      if ((a[i] != a[prev_idx]) && (min_dist > i - prev_idx))
        min_dist = i - prev_idx;
      else
        prev_idx = i;
    }
  }
  printf("Min distance between %d and %d is: %d\n", first, second, min_dist);
  return 0;
}


/*
 * Output:
 * ------------------------
 * Enter number of elements: 7
 * Enter element[0]: 2
 * Enter element[1]: 3
 * Enter element[2]: 5
 * Enter element[3]: 1
 * Enter element[4]: 9
 * Enter element[5]: 8
 * Enter element[6]: 3
 * Enter first number: 3
 * Enter second number: 2
 * Min distance between 3 and 2 is: 1
 */
