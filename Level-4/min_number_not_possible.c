/*
 * Date: 2018-10-07
 *
 * Description:
 * Given a sorted array (sorted in non-decreasing order) of positive numbers,
 * find the smallest positive integer value that cannot be represented as sum of
 * elements of any subset of given set.
 *
 * Approach:
 * https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/
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
  int res = 1;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d",&a[i]);
  }

  /*
   * - If arr[i] is greater than ‘res’, then we found the gap which is ‘res’
   * because the elements after arr[i] are also going to be greater than ‘res’.
   *
   * - The value of ‘res’ is incremented by arr[i] (why? If elements from 0 to
   * (i-1) can represent 1 to ‘res-1’, then elements from 0 to i can represent
   * from 1 to ‘res + arr[i] – 1’ be adding ‘arr[i]’ to all subsets that
   * represent 1 to ‘res’).
   */
  for (i = 0; (i < n) && (a[i] <= res); i++)
    res = res + a[i];

  printf("Minimum number not possible as sum of any subset: %d\n", res);
  return 0;
}


/*
 * Output:
 * -------------------------------------------------------------
 * Enter number of elements : 5
 * Enter element [0] : 1
 * Enter element [1] : 2
 * Enter element [2] : 4
 * Enter element [3] : 8
 * Enter element [4] : 16
 * Minimum number not possible as sum elements of any subset: 32
 *
 * Enter number of elements : 5
 * Enter element [0] : 1
 * Enter element [1] : 2
 * Enter element [2] : 3
 * Enter element [3] : 4
 * Enter element [4] : 5
 * Minimum number not possible as sum elements of any subset: 16
 */
