/*
 * Date: 2018-10-29
 *
 * Description:
 * Given an unsorted array and 2 numbers, find the minimum distance between 2
 * given numbers in array.
 *
 * Approach:
 * Scan array using an outer loop, if any of the 2 number is found, scan ahead
 * of array for next element using a nested inner loop.
 *
 * Complexity:
 * O(N^2)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0;
  int *a = NULL;
  int first = 0, second = 0, next = 0;
  int min_dist = 0, tmp_dist = 1;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ",i);
    scanf("%d", &a[i]);
  }
  printf("Enter first number: ");
  scanf("%d", &first);

  printf("Enter second number: ");
  scanf("%d", &second);

  min_dist = n - 1;
  for (i = 0; i < n; i++) {
    if (a[i] == first || a[i] == second) {
      tmp_dist = 1;
      if (a[i] == first)
        next = second;
      else
        next = first;
      
      for (j = i + 1; j < n; j++) {
        if (next == a[j])
          break;
        else
          tmp_dist++;
      }
      if (tmp_dist < min_dist && tmp_dist != 1)
        min_dist = tmp_dist;
    }
  }
  printf("Min distance between %d and %d is: %d\n", first, second, min_dist);
  return 0;
}


/*
 * Output:
 * ------------------------
 * Enter number of elements: 7
 * Enter element[0]: 3
 * Enter element[1]: 5
 * Enter element[2]: 2
 * Enter element[3]: 1
 * Enter element[4]: 8
 * Enter element[5]: 4
 * Enter element[6]: 3
 * Enter first number: 2
 * Enter second number: 3
 * Min distance between 2 and 3 is: 2 
 */
