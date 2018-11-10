/*
 * Date: 2018-11-10
 *
 * Description:
 * Given a sorted array and an integer X, find floor and ceil of X from array.
 * For example:
 * A = [3, 4, 7, 8, 10], X = 5 so floor of 5 would be 4 and ceil would be 7
 *
 * Approach:
 * First check for corner cases that is:
 * - If X is smaller than first element in array
 * - If X is larger than last element in array
 * - If above 2 don't meet do a binary search and check if we are able to find
 *   same number as X in array or we are able to find a condition a[m] < X and
 *   a[m + 1] > X
 *
 * Complexity:
 * O(logn)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0, x = 0;
  int *a = NULL;
  int floor = -1, ceil = -1;
  int mid = 0, low = 0, high = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d",&a[i]);
  }
  printf("Enter element: ");
  scanf("%d", &x);
  if (x < a[0]) {
    printf("Ceil - %d, Floor - Not possible\n", a[0]);
    return 0;
  }
  else if (x > a[n - 1]) {
    printf("Ceil - Not possible, Floor - %d\n", a[n - 1]);
    return 0;
  }
  low = 0;
  high = n - 1;
  while (low < high) {
    mid = (low + high)/2;
    if (x == a[mid]) {
      printf("Ceil - %d, Floor - %d\n", a[mid], a[mid]);
      break;
    }
    else if ((a[mid] < x) && (a[mid + 1] > x)) {
      printf("Ceil - %d, Floor - %d\n", a[mid + 1], a[mid]);
      break;
    }
    else if (x > a[mid])
      low = mid;
    else
      high = mid;
  }
  return 0;
}


/*
 * Output:
 * ------------------
 * Enter number of elements: 4
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Enter element: 2
 * Ceil - 2, Floor - 2
 *
 * Enter number of elements: 5
 * Enter element[0]: 2
 * Enter element[1]: 7
 * Enter element[2]: 10
 * Enter element[3]: 16
 * Enter element[4]: 111
 * Enter element: 50
 * Ceil - 111, Floor - 16
 *
 * Enter number of elements: 3
 * Enter element[0]: 4
 * Enter element[1]: 5
 * Enter element[2]: 6
 * Enter element: 10
 * Ceil - Not possible, Floor - 6
 *
 * Enter number of elements: 3
 * Enter element[0]: 4
 * Enter element[1]: 5
 * Enter element[2]: 6
 * Enter element: 1
 * Ceil - 4, Floor - Not possible
*/
