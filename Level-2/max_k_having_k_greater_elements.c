/*
 * Date: 2018-10-20
 *
 * Description:
 * Given an array of positive integers, find maximum possible value K such that
 * the array has at-least K elements that are greater than or equal to K. The
 * array is unsorted and may contain duplicate values.
 *
 * For example:
 * Input: [2, 3, 4, 5, 6, 7]
 * Output: 4
 * Explanation : 4 elements [4, 5, 6, 7] are greater than equal to 4
 *
 * Approach:
 * Initialise result with n and decrement result if we encounter an element
 * smaller than result
 *
 * Complexity:
 * O(N)
 *
 * Note:
 * If array has duplicates, this solution does not work - check last solution
 * from here, it requires O(N) extra space:
 * https://www.geeksforgeeks.org/maximum-value-k-such-that-array-has-at-least-k-elements-that-are-k/
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  int res = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  res = n;
  for (i = 0; i < n; i++) {
    if (res > a[i])
      res--;
  }
  printf("Max value of k such that, k elements are >= k: %d\n", res);
  return 0;
}


/*
 * Output:
 * ------------------------
 * Enter number of elements: 6
 * Enter element[0]: 2
 * Enter element[1]: 3
 * Enter element[2]: 4
 * Enter element[3]: 5
 * Enter element[4]: 6
 * Enter element[5]: 7
 * Max value of k such that, k elements are >= k: 4
 *
 * Enter number of elements: 4
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Max value of k such that, k elements are >= k: 2
 *
 * Enter number of elements: 5
 * Enter element[0]: 4
 * Enter element[1]: 5
 * Enter element[2]: 2
 * Enter element[3]: 3
 * Enter element[4]: 8
 * Max value of k such that, k elements are >= k: 3
 *
 * Enter number of elements: 5
 * Enter element[0]: 6
 * Enter element[1]: 7
 * Enter element[2]: 9
 * Enter element[3]: 8
 * Enter element[4]: 10
 * Max value of k such that, k elements are >= k: 5
 */
