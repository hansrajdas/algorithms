/**
 * Date: 2018-07-08
 *
 * Description:
 * Given a positive integer, print next largest number that have the same number
 * of 1 bits in their binary representation.
 *
 * Approach:
 * 1. Find position of rightmost non-trailing 0, p.
 * 2. Set that bit position, p.
 * 3. Clear all bits to right of non-trailing zero, p - 1 to 0.
 * 4. Insert as many 1s to right of p that was cleared in step 3.
 *
 * Complexity:
 * Time(: O(b), b number of bits in number.
 */

#include "stdio.h"

unsigned int next_largest_with_number_of_bits_set(unsigned int n) {
  unsigned short int c0 = 0, c1 = 0, p = 0;
  unsigned int c = n;

  // Counting number of trailing 0s.
  while (!(c & 1) && c) {
    c0++;
    c >>= 1;
  }

  // Counting number of 1s in sequence after trailing 0s.
  while (c & 1) {
    c1++;
    c >>= 1;
  }

  p = c0 + c1;  // Position of rightmost non-trailing 0.

  // Next largest with same number of bits set as in n is not possible if there
  // no non trailing 0 in n like all 0s or 11..11..0000 will not have a
  // solution.
  if ((p == (sizeof(n) * 8) - 1) || !p)
    return 0;

  /* Steps to achieve result:
   * 1. Set rightmost non-trailing 0 bit position.
   * 2. Clear all bit positions to right of p.
   * 3. Set all bit positions from c1 - 1 to 0.
   */
  n |= (1 << p);  // Step 1.
  n &= ~((1 << p) - 1); // Step 2.
  n |= (1 << (c1 - 1)) - 1;  // Step 3.

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
  res = next_largest_with_number_of_bits_set(number);
  if (!res)
    return -1;

  printf("\nNext largest number with same number of bits set as in %d is: %d\n",
      number, res);
  binary_representation(res);
  return 0;
}

/*
Output:
Enter a number: 2
Binary representation of 2 is: 0000 0000 0000 0000 0000 0000 0000 0010

Next largest number with same number of bits set as in 2 is: 4
Binary representation of 4 is: 0000 0000 0000 0000 0000 0000 0000 0100


Enter a number: 15
Binary representation of 15 is: 0000 0000 0000 0000 0000 0000 0000 1111

Next largest number with same number of bits set as in 15 is: 23
Binary representation of 23 is: 0000 0000 0000 0000 0000 0000 0001 0111


Enter a number: 1
Binary representation of 1 is: 0000 0000 0000 0000 0000 0000 0000 0001

Next largest number with same number of bits set as in 1 is: 2
Binary representation of 2 is: 0000 0000 0000 0000 0000 0000 0000 0010


Enter a number: 13948
Binary representation of 13948 is: 0000 0000 0000 0000 0011 0110 0111 1100

Next largest number with same number of bits set as in 13948 is: 13967
Binary representation of 13967 is: 0000 0000 0000 0000 0011 0110 1000 1111
*/
