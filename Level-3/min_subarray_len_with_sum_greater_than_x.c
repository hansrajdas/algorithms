/*
 * Date: 2018-10-20
 *
 * Description:
 * Find length of minimum subarray having sum greater than X.
 *
 * Approach:
 * Scan array elements from beginning and keep on adding to sum until it becomes
 * greater than X.
 * Once it becomes more than X subtract array element from beginning, keep track
 * if array length is less than min saved(min length should be initialised with
 * n + 1), if yes update min length.
 *
 * Complexity:
 * O(N) Average case
 */

#include "stdio.h"
#include "stdlib.h"

void minSubArrayHavingSum(int a[], int n, int x) {
  int start = 0, end = 0;
  int min_len = n + 1, sum = 0;
  while (end < n) {
    while (sum <= x && end < n)
      sum += a[end++];

    while (sum > x && start < n) {
      if (min_len > end - start)
        min_len = end - start;

      sum -= a[start++];
    }
  }
  printf("Min length of subarray having sum > %d is %d\n", x, min_len);
}

int main() {
  int i = 0;
  int n = 0, x = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }
  printf("Enter required sum: ");
  scanf("%d", &x);
  minSubArrayHavingSum(a, n, x);
  return 0;
}


/*
 * Output:
 * --------------------------------
 * Enter number of elements: 5
 * Enter element[0]: 3
 * Enter element[1]: 4
 * Enter element[2]: 1
 * Enter element[3]: 2
 * Enter element[4]: 6
 * Enter required sum: 5
 * Min length of subarray having sum > 5 is 1
 *
 * Enter number of elements: 7
 * Enter element[0]: 3
 * Enter element[1]: 4
 * Enter element[2]: 2
 * Enter element[3]: 1
 * Enter element[4]: 9
 * Enter element[5]: 10
 * Enter element[6]: 4
 * Enter required sum: 15
 * Min length of subarray having sum > 15 is 2
 *
 * Enter number of elements: 5
 * Enter element[0]: 4
 * Enter element[1]: 5
 * Enter element[2]: 2
 * Enter element[3]: 6
 * Enter element[4]: 1
 * Enter required sum: 9
 * Min length of subarray having sum > 9 is 3
 */
