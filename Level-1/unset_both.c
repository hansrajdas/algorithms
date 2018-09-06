/*
 * Date: 2018-mm-dd
 *
 * Description:
 * There is an array of 2 elements, one of them is 0. Write a statement which
 * makes both 0.
 *
 * Approach:
 * a[a[1]] = a[a[0]]
 *
 * Complexity:
 * O(1)
 */

#include "stdio.h"

int main() {
  int a[2] = {1, 0};
  printf("Before a[0] = %d, a[1] = %d\n", a[0], a[1]);
  a[a[1]] = a[a[0]];
  printf("After a[0] = %d, a[1] = %d\n", a[0], a[1]);
  return 0;
}
