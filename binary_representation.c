/*
 * Date: 2018-07-03
 *
 * Description:
 * Print binary representation of an integer.
 *
 * Complexity:
 * O(1)
 */

#include "stdio.h"

void binary_representation(int n) {
  unsigned short int size = sizeof(int) * 8;
  unsigned int i = 0;
  printf("Binary representation of %d is: ", n);

  // Checking bit at individual position and printing 0 or 1.
  for (i = 1 << size - 1; i > 0; i = i/2)
    (n & i) ? printf("1") : printf("0");
}

int main() {
  int n = 0;
  printf("Enter number: ");
  scanf("%d", &n);
  binary_representation(n);
  printf("\n");
  return 0;
}
