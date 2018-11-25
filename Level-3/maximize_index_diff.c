/*
 * Date: 2018-10-07
 *
 * Description:
 * Given an array arr[], find the maximum j – i such that arr[j] > arr[i].
 *
 * Examples:
 *
 * Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
 * Output: 6  (j = 7, i = 1)
 *
 * Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
 * Output: 8 ( j = 8, i = 0)
 *
 * Input:  {1, 2, 3, 4, 5, 6}
 * Output: 5  (j = 5, i = 0)
 *
 * Input:  {6, 5, 4, 3, 2, 1}
 * Output: -1
 *
 * Approach:
 * So we construct two auxiliary arrays LMin[] and RMax[] such that LMin[i]
 * holds the smallest element on left side of arr[i] including arr[i],
 * and RMax[j] holds the greatest element on right side of arr[j]
 * including arr[j].
 * Then we traverse both of these arrays from left to right.
 * While traversing if we see that LMin[i] is greater than RMax[j], then we
 * must move ahead in LMin[] (or do i++) because all elements on left of LMin[i]
 * are greater than or equal to LMin[i]. Otherwise we must move ahead in RMax[j]
 * to look for a greater j – i value.
 *
 * Reference:
 * https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
 *
 * Complexity:
 * O(N) Time and space
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0;
  int *A = NULL, *LMin = NULL, *RMax = NULL;
  int res = -1;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element [%d]: ", i);
    scanf("%d",&A[i]);
  }

  // Populate LMin[] such that LMin[i] contains min element in A[0...i].
  LMin = (int *)malloc(sizeof(int) * n);
  LMin[0] = A[0];
  for (i = 1; i < n; i++)
    LMin[i] = A[i] > LMin[i - 1] ? LMin[i - 1] : A[i];

  // Populate RMax[] such that RMax[i] contains max element in A[n-1...i].
  RMax = (int *)malloc(sizeof(int) * n);
  RMax[n - 1] = A[n - 1];
  for (i = n - 2; i >=0; i--)
    RMax[i] = A[i] > RMax[i + 1] ? A[i] : RMax[i + 1];

  i = 0;
  j = 0;
  while (i < n && j < n) {
    if (LMin[i] < RMax[j]) {
      if (res < j - i)
        res = j - i;
      j++;
    }
    else
      i++;
  }
  printf("Max(j - i) with A[j] > A[i] is: %d\n", res);
  return 0;
}

/*
 * Output:
 * ----------------------------------------------
 * Enter number of elements: 9
 * Enter element [0]: 34
 * Enter element [1]: 8
 * Enter element [2]: 10
 * Enter element [3]: 3
 * Enter element [4]: 2
 * Enter element [5]: 80
 * Enter element [6]: 30
 * Enter element [7]: 33
 * Enter element [8]: 1
 * Max(j - i) with A[j] > A[i] is: 6
 *
 * Enter number of elements: 4
 * Enter element [0]: 1
 * Enter element [1]: 2
 * Enter element [2]: 3
 * Enter element [3]: 4
 * Max(j - i) with A[j] > A[i] is: 3
 *
 * Enter number of elements: 4
 * Enter element [0]: 4
 * Enter element [1]: 3
 * Enter element [2]: 2
 * Enter element [3]: 1
 * Max(j - i) with A[j] > A[i] is: -1
 */
