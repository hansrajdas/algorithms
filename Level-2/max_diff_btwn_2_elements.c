/*
 * Date: 2018-10-07
 *
 * Description:
 * Find maximum difference between 2 elements in a array such that larger
 * element appears at right of smaller element
 *
 * Approach:
 * - Take an initial diff between first 2 elements.
 * - Scan array and keep track of smallest element appeared so far.
 * - With each new element calculate its diff with smallest element, if diff is
 * more than previously calculate then update max diff.
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
  int max_diff = 0;
  int min_element = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element [%d] : ", i);
    scanf("%d",&a[i]);
  }
  max_diff = a[1] - a[0];  // Initial diff
  min_element = a[0];
  for (i = 1; i < n; i++) {
    if (a[i] - min_element > max_diff)
      max_diff = a[i] - min_element;

    if (min_element > a[i])
      min_element = a[i];
  }
  printf("Max difference between 2 elements(larger appearing later): %d\n",
    max_diff);
  return 0;
}


/*
 * Output:
 * -------------------------------------------------
 * Enter number of elements: 5
 * Enter element [0] : 1
 * Enter element [1] : 2
 * Enter element [2] : 3
 * Enter element [3] : 4
 * Enter element [4] : 5
 * Max difference between 2 elements(larger appearing later): 4
 *
 * Enter number of elements: 3
 * Enter element [0] : 3
 * Enter element [1] : 2
 * Enter element [2] : 1
 * Max difference between 2 elements(larger appearing later): -1
 *
 * Enter number of elements: 8
 * Enter element [0] : 5
 * Enter element [1] : 4
 * Enter element [2] : 6
 * Enter element [3] : 7
 * Enter element [4] : 2
 * Enter element [5] : 5
 * Enter element [6] : 7
 * Enter element [7] : 9
 * Max difference between 2 elements(larger appearing later): 7 
 */
