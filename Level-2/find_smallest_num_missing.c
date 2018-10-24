/*
 * Date: 2018-10-24
 *
 * Description:
 * Find smallest missing number from a sorted array of size n. Range of numbers
 * in array is 0 to n - 1.
 *
 * Approach:
 * We can use divide and conquer approach:
 * - When index becomes smaller than element, search on left subarray otherwise
 *   on right subarray
 * - If start becomes more than end, no element array is missing return end + 1
 * - And if start index and element at that index are not same, start is missing
 *
 * Complexity:
 * O(logn)
 */

#include "stdio.h"
#include "stdlib.h"

int findSmallestMissing(int arr[], int start, int end) {
  int mid = 0;
  if (start > end)
    return end + 1;
  else if (arr[start] != start)
    return start;
  else {
    mid = (start + end)/2;
    if (arr[mid] > mid)
      findSmallestMissing(arr, start, mid + 1);
    else
      findSmallestMissing(arr, mid + 1, end);
  }
}

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }
  printf("Smallest missing number is: %d\n", findSmallestMissing(a, 0, n - 1));
  return 0;
}


/*
 * Output:
 * -------------------
 * Enter number of elements: 5
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Enter element[4]: 5
 *
 * Enter number of elements: 5
 * Enter element[0]: 0
 * Enter element[1]: 1
 * Enter element[2]: 2
 * Enter element[3]: 3
 * Enter element[4]: 4
 *
 * Enter number of elements: 5
 * Enter element[0]: 0
 * Enter element[1]: 1
 * Enter element[2]: 3
 * Enter element[3]: 3
 * Enter element[4]: 4
 * Smallest missing number is: 2
 */
