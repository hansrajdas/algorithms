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
 * - If above 2 don't meet do a linear search and check if we are able to find
 *   same number as X in array or just larger than X.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0, x = 0;
  int *a = NULL;
  int floor = -1, ceil = -1;
  printf("Enter number of elements: ");
  scanf("%d",&n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d",&a[i]);
  }
  printf("Enter element: ");
  scanf("%d",&x);
  if(x < a[0]) {
    printf("Ceil - %d, Floor - Not possible\n", a[0]);
    return 0;
  }
  else if(x > a[n - 1]) {
    printf("Ceil - Not possible, Floor - %d\n", a[n - 1]);
    return 0;
  }

  // Search sequentially
  for(i = 0; i < n; i++) {
    if(a[i] == x) {
      printf("Ceil[%d], Floor[%d]\n", a[i], a[i]);
      break;
    }
    else if(a[i] > x) {
      ceil = a[i];
      floor = !i ? -1 : a[i - 1];
      printf("Ceil[%d], Floor[%d]\n", ceil, floor);
      break;
    }
  }
  return 0;
}


/*
 * Output:
 * ----------------------
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element: 10
 * Ceil - Not possible, Floor - 3
 *
 * Enter number of elements: 3
 * Enter element[0]: 4
 * Enter element[1]: 5
 * Enter element[2]: 6
 * Enter element: 1
 * Ceil - 4, Floor - Not possible
 *
 * Enter number of elements: 5
 * Enter element[0]: 2
 * Enter element[1]: 6
 * Enter element[2]: 9
 * Enter element[3]: 10
 * Enter element[4]: 22
 * Enter element: 15
 * Ceil[22], Floor[10]
 */
