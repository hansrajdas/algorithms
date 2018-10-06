/*
 * Date: 2018-10-06
 *
 * Description:
 * Check if an given unsorted array is jolly jumper sequence or not.
 * An array having n elements is a jolly jumper sequence if absolute difference
 * between adjacent elements ranges from 1 to n - 1, no difference repeated.
 * For example - [1, 4, 2, 3], n = 4 is a jolly jumper sequence as absolute
 * difference between adjacent elements are 1, 2 and 3.
 *
 * Approach:
 * Iterate over array and find difference between adjacent elements, if it is
 * 0, more than n - 1 or already found, break loop with failure message.
 * Otherwise save this difference and check for next adjacent element.
 *
 * Complexity:
 * O(N) Time and space
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0, diff = 0;
  int *a = NULL, *map = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  map = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d",&a[i]);
    map[i] = 0;
  }

  for (i = 0; i < n-1; i++) {
    diff = a[i + 1] - a[i];
    diff = diff > 0 ? diff : -diff;
    // If diff is 0, more than n - 1 or already found, it's not a jolly jumper
    // sequence.
    if (!diff || diff > n - 1 || map[diff]) {
      printf("NO\n");
      return -1;
    }
    else
      map[diff] = 1;
  }
  printf("YES\n");
  return 0;
}


/*
 * Output:
 * ------------------------
 * Enter number of elements: 4
 * Enter element[0]: 1
 * Enter element[1]: 4
 * Enter element[2]: 2
 * Enter element[3]: 3
 * YES
 *
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * NO
 */
