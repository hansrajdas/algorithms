/*
 * Date: 2018-10-20
 *
 * Description:
 * Given an array of positive numbers, find the maximum sum of a subsequence
 * with the constraint that no 2 numbers in the sequence should be adjacent in
 * the array.
 * So 3 2 7 10 should return 13 (sum of 3 and 10) or
 * 3 2 5 10 7 should return 15 (sum of 3, 5 and 7)
 *
 * Approach:
 * Loop for all elements in arr[] and maintain two sums incl and excl where
 * incl = Max sum including the previous element and excl = Max sum excluding
 * the previous element.
 * Max sum excluding the current element will be max(incl, excl) and max sum
 * including the current element will be excl + current element (Note that only
 * excl is considered because elements cannot be adjacent).
 * At the end of the loop return max of incl and excl.
 *
 * https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
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
  int incl = 0, excl = 0, excl_new = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }
  incl = a[0];
  for (i = 1; i < n; i++) {
    excl_new = (excl > incl) ? excl : incl;
    incl = excl + a[i];
    excl = excl_new;
  }
  printf("Max sum with no adjacent element is: %d\n",
    (excl > incl) ? excl : incl);
  return 0;
}


/*
 * Output:
 * ---------------------
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Max sum with no adjacent element is: 4
 *
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 5
 * Enter element[2]: 3
 * Max sum with no adjacent element is: 5
 *
 * Enter number of elements: 5
 * Enter element[0]: 3
 * Enter element[1]: 6
 * Enter element[2]: 2
 * Enter element[3]: 4
 * Enter element[4]: 8
 * Max sum with no adjacent element is: 14, Adding 6 and 8
 */
