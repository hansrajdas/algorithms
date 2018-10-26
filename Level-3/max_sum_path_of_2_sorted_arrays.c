/*
 * Date: 2018-10-26
 *
 * Description:
 * Given two sorted arrays such the arrays may have some common elements. Find
 * the sum of the maximum sum path to reach from beginning of any array to end
 * of any of the two arrays. We can switch from one array to another array only
 * at common elements. Examples:
 *
 * Input:  ar1[] = {2, 3, 7, 10, 12}, ar2[] = {1, 5, 7, 8}
 * Output: 35
 * 35 is sum of 1 + 5 + 7 + 10 + 12.
 * We start from first element of arr2 which is 1, then we move to 5, then 7.
 * From 7, we switch to ar1 (7 is common) and traverse 10 and 12.
 *
 * Input:  ar1[] = {10, 12}, ar2 = {5, 7, 9}
 * Output: 22
 * 22 is sum of 10 and 12. Since there is no common element, we need to take all
 * elements from the array with more sum.
 *
 * Approach:
 * We need to calculate sums of elements between all common points for both
 * arrays. Whenever we see a common point, we compare the two sums and add the
 * maximum of two to the result.
 *
 * Complexity:
 * O(M + N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0, m = 0;
  int *a1 = NULL, *a2 = NULL;

  // sum1 and sum2 holds sum between common elements.
  int sum1 = 0, sum2 = 0, result = 0;

  printf("Enter number of elements for a1: ");
  scanf("%d", &n);
  a1 = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element a1[%d]: ", i);
    scanf("%d", &a1[i]);
  }
  printf("Enter number of elements for a2: ");
  scanf("%d", &m);
  a2 = (int *)malloc(sizeof(int)*m);
  for (i = 0; i < m; i++) {
    printf("Enter element a2[%d]: ", i);
    scanf("%d", &a2[i]);
  }
  i = 0;
  j = 0;
  while (i < n && j < m) {
    if (a1[i] < a2[j])
      sum1 += a1[i++];  // Keep on adding smaller element and advance in array
    else if (a1[i] > a2[j])
      sum2 += a2[j++];
    else {  // Found a common element, update result with max of sum1 and sum2
      result += (sum1 > sum2) ? sum1 : sum2;
      result += a1[i];
      i++;
      j++;
      sum1 = 0;
      sum2 = 0;
    }
  }

  // Add remaining elements to sum1 or sum2 and update final result.
  while (i < n)
    sum1 += a1[i++];
  while (j < m)
    sum2 += a2[j++];

  result += (sum1 > sum2) ? sum1 : sum2;
  printf("Max sum path of 2 sorted arrays is: %d\n", result);
  return 0;
}


/*
 * Output:
 * ---------------------------
 * Enter number of elements for a1: 5
 * Enter element a1[0]: 2
 * Enter element a1[1]: 3
 * Enter element a1[2]: 7
 * Enter element a1[3]: 10
 * Enter element a1[4]: 12
 * Enter number of elements for a2: 4
 * Enter element a2[0]: 1
 * Enter element a2[1]: 5
 * Enter element a2[2]: 7
 * Enter element a2[3]: 8
 * Max sum path of 2 sorted arrays is: 35
 *
 * Enter number of elements for a1: 2
 * Enter element a1[0]: 10
 * Enter element a1[1]: 12
 * Enter number of elements for a2: 3
 * Enter element a2[0]: 5
 * Enter element a2[1]: 7
 * Enter element a2[2]: 9
 * Max sum path of 2 sorted arrays is: 22
 */
