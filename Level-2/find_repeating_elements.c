/*
 * Date: 2018-09-27
 *
 * Description:
 * Given an array of n elements which contains elements from 0 to n-1, with any
 * of these numbers appearing any number of times. Find these repeating numbers
 * in O(n) and using only constant memory space.
 *
 * For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6}, the answer
 * should be 1, 3 and 6.
 *
 * Approach:
 * - Traverse the given array from i= 0 to n-1 elements.
 * - Go to index arr[i]%n and increment its value by n.
 * - Now traverse the array again and print all those indexes i for which
 *   arr[i]/n is greater than 1.
 *
 * This approach works because all elements are in range from 0 to n-1 and
 * arr[i]/n would be greater than 1 only if a value "i" has appeared more than
 * once.
 *
 * Complexity:
 * O(N) time
 * O(1) space
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int idx = 0;
  int n = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);

  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  for (i = 0; i < n; i++) {
    idx = a[i] % n;
    a[idx] += n;
  }

  for (i = 0; i < n; i++) {
    if (a[i] / n > 1)
      printf("Repeated number: %d\n", i);
  }
  return 0;
}


/*
 * Output:
 * -------------------
 * Enter number of elements: 4
 * Enter element[0]: 2
 * Enter element[1]: 2
 * Enter element[2]: 4
 * Enter element[3]: 4
 * Repeated number: 0
 * Repeated number: 2
 *
 * Enter number of elements: 5
 * Enter element[0]: 3
 * Enter element[1]: 3
 * Enter element[2]: 2
 * Enter element[3]: 2
 * Enter element[4]: 4
 * Repeated number: 2
 * Repeated number: 3
 */
