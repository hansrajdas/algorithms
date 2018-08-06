/*
 * Date: 2018-07-11
 *
 * Description:
 * Swap odd and even bits in an integer. Bit 0 and bit 1 are swapped, bit 2 and
 * bit 3 are swapped, so on.
 */

#include "stdio.h"

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
  int n = 0, res = 0;
  printf("Enter number: ");
  scanf("%d", &n);
  binary_representation(n);

  /*
   * 1. Masking even bit positions and right shifting number.
   * 2. Masking odd bit positions and left shifting number.
   * 3. ORing result of step 1 and 2.
   */
  res = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1); 
  printf("\nNumber after swapping odd and even bits: %d\n", res);
  binary_representation(res);
  return 0;
}

/*
 Output:

Enter number: 2
Binary representation of 2 is: 0000 0000 0000 0000 0000 0000 0000 0010

Number after swapping odd and even bits: 1
Binary representation of 1 is: 0000 0000 0000 0000 0000 0000 0000 0001

Enter number: 4
Binary representation of 4 is: 0000 0000 0000 0000 0000 0000 0000 0100

Number after swapping odd and even bits: 8
Binary representation of 8 is: 0000 0000 0000 0000 0000 0000 0000 1000

Enter number: 5
Binary representation of 5 is: 0000 0000 0000 0000 0000 0000 0000 0101

Number after swapping odd and even bits: 10
Binary representation of 10 is: 0000 0000 0000 0000 0000 0000 0000 1010

Enter number: 10
Binary representation of 10 is: 0000 0000 0000 0000 0000 0000 0000 1010

Number after swapping odd and even bits: 5
Binary representation of 5 is: 0000 0000 0000 0000 0000 0000 0000 0101 
*/
