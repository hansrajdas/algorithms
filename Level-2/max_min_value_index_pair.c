/*
 * Date: 2018-10-14
 *
 * Description:
 * Maximize value of (a[i] - i) - (a[j] - j) in an unsorted array
 *
 * Approach:
 * Consider a[i] - i and a[j] - j as independent, idea is to find maximum and
 * minimum value of a[x] - x and subtract them to max required value.
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
  int max = 0, min = 65536;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  for (i = 0; i < n; i++) {
    if (max < a[i] - i)
      max = a[i] - i;

    if (min > a[i] - i)
      min = a[i] - i;
  }
  printf ("Max((a[i] - i) - (a[j] - j)) is: %d\n", max - min);
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
 * Max((a[i] - i) - (a[j] - j)) is: 0
 *
 * Enter number of elements: 5
 * Enter element[0]: 5
 * Enter element[1]: 4
 * Enter element[2]: 3
 * Enter element[3]: 2
 * Enter element[4]: 1
 * Max((a[i] - i) - (a[j] - j)) is: 8
 *
 * Enter number of elements: 7
 * Enter element[0]: 2
 * Enter element[1]: 5
 * Enter element[2]: 9
 * Enter element[3]: 10
 * Enter element[4]: 0
 * Enter element[5]: 3
 * Enter element[6]: 4
 * Max((a[i] - i) - (a[j] - j)) is: 11 
 */
