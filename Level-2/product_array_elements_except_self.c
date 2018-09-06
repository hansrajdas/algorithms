/*
 * Date: 2018-09-06
 *
 * Description:
 * Given an array, create another array such that value at each index is product
 * of all elements except element at that index.
 * a = [1, 2, 3], output = [6, 3, 2]
 *
 * Approach:
 * First scan array from left to right multiplying each element encountered and
 * keep on assigning product to respective index in product array. Note that
 * first we have to assign and then compute product just to skip current
 * element.
 * So after first iteration product array will have element which is product of
 * all previous elements.
 * Secondly scan from right to left following the same approach. Resultant will
 * be product of all elements except current one.
 *
 * Complexity:
 * O(n)
 */

#include "stdio.h"

int main() {
  int i = 0, temp = 1;
  int input[10] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
  int prod[10];
  int n = 10;

  for (i = 0; i < n; i++) {
    prod[i] = temp;
    temp *= input[i];
  }

  temp = 1;
  for (i = n - 1; i >= 0; i--) {
    prod[i] *= temp;
    temp *= input[i];
  }

  for (i = 0; i < n; i++)
    printf("%d ",prod[i]);

  printf("\n");
  return 0;
}
