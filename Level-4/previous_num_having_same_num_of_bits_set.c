/**
 * Date: 2018-07-09
 *
 * Description:
 * Given a positive integer, print previous number that have the same number
 * of 1 bits in their binary representation.
 *
 * Approach:
 * 1. Find number of trailing 1s, c1.
 * 2. Find number of 0s to left of trailing 1s, c0
 * 3. Find position of rightmost non-trailing 1, p = c0 + c1.
 * 4. Clear all bits from bit position p to 0.
 * 5. Insert c1 + 1 ones to the right of bit position p.
 *
 * Complexity:
 * Time(: O(b), b number of bits in number.
 */

#include "stdio.h"

unsigned int previous_num_with_same_number_of_bits_set(unsigned int n) {
  unsigned short int c0 = 0, c1 = 0, p = 0;
  unsigned int mask = 0, c = n;

  // Counting number of trailing 1s, c1.
  while (c & 1) {
    c1++;
    c >>= 1;
  }

  // If input has all ones, solution is not possible.
  if (!c)
    return 0;

  // Counting number of 0s to left of trailing 1s, c0.
  while (!(c & 1) && c) {
    c0++;
    c >>= 1;
  }

  p = c0 + c1;  // Position of rightmost non-trailing 1.

  /* Steps to achieve result:
   * 1. Clear all bit positions to right of p.
   * 2. Insert c1 + 1 ones to right of bit position p.
   */
  n &= ((~0) << (p + 1)); // Step 1.
  mask = (1 << (c1 + 1)) - 1;
  n |= mask << (c0 - 1);  // Step 2.

  return n;
}

void binary_representation(int n) {
  unsigned short int size = sizeof(int) * 8;
  unsigned short int space = 0;
  unsigned int i = 0;
  printf("Binary representation of %d is: ", n);

  // Checking bit at individual position and printing 0 or 1.
  for (i = 1 << size - 1; i > 0; i = i >> 1) {
    if (space & 0x04) {
      space = 0;
      (n & i) ? printf(" 1") : printf(" 0");  // Add space between each nibble.
    } else {
      (n & i) ? printf("1") : printf("0");
    }
    space++;
  }
  printf("\n");
}

int main() {
  unsigned int number = 0, res = 0;
  printf("Enter a number: ");
  scanf("%d", &number);
  binary_representation(number);
  res = previous_num_with_same_number_of_bits_set(number);
  if (!res) {
    printf("\nSolution *NOT* possible\n");
    return -1;
  }

  printf("\nPrevious number with same number of bits set as in %d is: %d\n",
      number, res);
  binary_representation(res);
  return 0;
}

/*
Output:

Enter a number: 10
Binary representation of 10 is: 0000 0000 0000 0000 0000 0000 0000 1010

Previous number with same number of bits set as in 10 is: 9
Binary representation of 9 is: 0000 0000 0000 0000 0000 0000 0000 1001

Enter a number: 1
Binary representation of 1 is: 0000 0000 0000 0000 0000 0000 0000 0001

Solution *NOT* possible

Enter a number: 8
Binary representation of 8 is: 0000 0000 0000 0000 0000 0000 0000 1000

Previous number with same number of bits set as in 8 is: 4
Binary representation of 4 is: 0000 0000 0000 0000 0000 0000 0000 0100
*/
