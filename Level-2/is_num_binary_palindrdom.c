/*
 * Date: 2018-09-06
 *
 * Description:
 * Check if a numbers binary representation is palindrome or not.
 *
 * Approach:
 * Compare from both ends one by one, each LSB with corresponding bit position
 * at MSB.
 *
 * Complexity:
 * O(d), d = Number of bits required to represent a number under test.
 */

#include "stdio.h"

int main() {
  unsigned int a = 0x1ffffff8;  // 0001 1111 1111 1111 1111 1111 1111 1000
  unsigned int x, y, r, l;
  l = 1 << 31;
  r = 1;
  while (l > r) {
    if ((a & l ? 1 : 0) != ( a & r ? 1 : 0)) {
      printf("Not palindrome\n");
      return -1;
    }
    l = l >> 1;
    r = r << 1;
  }
  printf("Palindrome\n");
  return 0;
}
