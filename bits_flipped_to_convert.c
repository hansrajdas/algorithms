/*
 * Date: 2018-07-11
 *
 * Description:
 * Determine the number of bits need to flip to convert integer A to B.
 * Example
 * Input: 29 (11101), 15 (01111)
 * Output: 2
 *
 * Approach:
 * XOR of 2 numbers will give ones at places only where they have different
 * bits. So we can get solution by counting the number of set bits in A^B.
 */

#include "stdio.h"

unsigned short int bits_flipped_to_convert(int from, int dst) {
  int temp = 0;
  unsigned short int count = 0;

  /*
   * count can also be incremented using temp >>= 1 and count += count & 1 but
   * with that we will have to check all 32 bits, suppose:
   * from^dst = 10000000...31 times, in this case we will have to iterate 32
   * times to find that count = 1 but with below approach we can get count in
   * only one iteration. In general below loop will execute as many times as the
   * number of ones in from^dat.
   */
  for (temp = from^dst; temp != 0; temp = temp & (temp - 1))
    count++;
  return count;
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
  int from = 0, to = 0;
  printf("Enter first (source) number: ");
  scanf("%d", &from);
  binary_representation(from);

  printf("Enter second (destination) number: ");
  scanf("%d", &to);
  binary_representation(to);

  printf("\nNumber of bit flips required to convert %d to %d: %hu\n",
    from, to, bits_flipped_to_convert(from, to));
  return 0;
}

/*
Enter first (source) number: 2
Binary representation of 2 is: 0000 0000 0000 0000 0000 0000 0000 0010
Enter second (destination) number: 3
Binary representation of 3 is: 0000 0000 0000 0000 0000 0000 0000 0011

Number of bit flips required to convert 2 to 3: 1

Enter first (source) number: 0
Binary representation of 0 is: 0000 0000 0000 0000 0000 0000 0000 0000
Enter second (destination) number: -1
Binary representation of -1 is: 1111 1111 1111 1111 1111 1111 1111 1111

Number of bit flips required to convert 0 to -1: 32

Enter first (source) number: 0
Binary representation of 0 is: 0000 0000 0000 0000 0000 0000 0000 0000
Enter second (destination) number: 0
Binary representation of 0 is: 0000 0000 0000 0000 0000 0000 0000 0000

Number of bit flips required to convert 0 to 0: 0

Enter first (source) number: 3
Binary representation of 3 is: 0000 0000 0000 0000 0000 0000 0000 0011
Enter second (destination) number: 3
Binary representation of 3 is: 0000 0000 0000 0000 0000 0000 0000 0011

Number of bit flips required to convert 3 to 3: 0

Enter first (source) number: 4096
Binary representation of 4096 is: 0000 0000 0000 0000 0001 0000 0000 0000
Enter second (destination) number: 0
Binary representation of 0 is: 0000 0000 0000 0000 0000 0000 0000 0000

Number of bit flips required to convert 4096 to 0: 1
*/
