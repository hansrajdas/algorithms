/*
 * Date: 2018-10-02
 *
 * Description:
 * Given an array of random integers(positive and negative numbers), find the
 * smallest positive integer missing. For example:
 *
 * A = [1, 2, 3, 4] result = 5
 * A = [10, 2, 3, 4] result = 1
 * A = [-1, 0, 1, 3, 3, 5] result = 2
 *
 * Approach:
 * - Move all non positive(0 and negative) numbers to starting as we only care
 *   about positive numbers.
 * - Again scan array for positive numbers and if number is not more than n,
 *   mark number at this index as negative.
 * - Scan array again and check element is which index is still positive, that
 *   would be the missing number, if none return n + 1.
 *
 * Complexity:
 * O(N) Time
 * O(1) Space
 */

#include "stdio.h"
#include "stdlib.h"

int abs(int n) {
  return n ? n : -n;
}

int find_min_positive_missing(int arr[], int n) {
  int i;
  for (i = 0; i < n; i++) {
    if ((arr[i] <= n) && (arr[abs(arr[i]) - 1] > 0))
      arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1];
  }
  for (i = 0; i < n; i++) {
    if (arr[i] > 0)
      return i + 1;
  }
  return n + 1;
}

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  int min_positive = 0, non_positive = 0, tmp;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);

  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d",&a[i]);
  }

  for (i = 0; i < n; i++) {
    if (0 >= a[i]) {
      tmp = a[non_positive];
      a[non_positive] = a[i];
      a[i] = tmp;
      non_positive++;
    }
  }
  min_positive = find_min_positive_missing(a + non_positive, n - non_positive);
  printf("Minimum positive missing: %d\n", min_positive);
  return 0;
}


/*
 * Output:
 * -----------
 * Enter number of elements: 3
 * Enter element[0]: 3
 * Enter element[1]: 2
 * Enter element[2]: 1
 * Minimum positive missing: 4
 *
 * Enter number of elements: 5
 * Enter element[0]: -2
 * Enter element[1]: -1
 * Enter element[2]: 2
 * Enter element[3]: 1
 * Enter element[4]: 4
 * Minimum positive missing: 3
 */ 
