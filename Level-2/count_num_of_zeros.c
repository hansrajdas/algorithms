/*
 * Date: 2018-10-06
 *
 * Description:
 * Given an array having 0s followed by 1s, find the number of 0s present.
 * For example:
 * A: [1, 0, 0], Ans - 2
 * A: [1, 1, 0], Ans - 1
 *
 * Approach:
 * Check for special cases - All zeros or all ones in array.
 * Use binary search approach and try to find a condition where A[mid] = 1 and
 * A[mid + 1] = 0.
 *
 * Complexity:
 * O(logn)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, left = 0, right = 0, mid = 0;
  int n = 0;
  int *a = NULL;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  if (!a[0])
    printf("All zeros present in list: %d\n", n);
  else if (a[n - 1])
    printf("None zero present in list\n");
  else {
    left = 0;
    right = n - 1;
    while (left < right) {
      mid = (left + right)/2;
      if (a[mid] && !a[mid + 1])
        break;
      else if (a[mid] && a[mid + 1])
        left = mid;
      else
        right = mid;
    }
    printf("Number of zeros in sorted list of 1 and 0 are: %d\n",
      (n - (mid + 1)));
  }
  return 0;
}


/*
 * Output:
 * ---------------
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 1
 * Enter element[2]: 0
 * Number of zeros in sorted list of 1 and 0 are: 1
 *
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 0
 * Enter element[2]: 0
 * Number of zeros in sorted list of 1 and 0 are: 2
 */
