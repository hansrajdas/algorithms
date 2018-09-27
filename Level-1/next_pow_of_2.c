/*
 * Date: 2018-09-26
 *
 * Description:
 * Given a number, find next greater number which is of the form 2^n.
 *
 * Approach:
 * Keep on shifting left 1 by number bits in given number.
 *
 * Complexity:
 * O(b), b = Number of bits set in given number.
 */

#include "stdio.h"

int main() {
  int i = 1;
  int num = 1;
  printf("Enter number: ");
  scanf("%d", &num);

  while (num) {
    num = num >> 1;
    i = i << 1;
  }
  printf("Next power of 2 will be: %d\n", i);
  return 0;
}
