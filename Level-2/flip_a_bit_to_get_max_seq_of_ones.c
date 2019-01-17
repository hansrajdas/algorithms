/**
 * Date: 2018-07-07
 *
 * Description:
 * Given a number, flip a bit to get max sequence of 1s.
 *
 * Approach:
 * Scan from LSB to MSB and keep track of 0s and 1s. If current bit is 1
 * increment length otherwise check one previous bit if it is 0 sequence can't
 * be combined (more than one 0 case). If previous bit is 1 set previous length
 * to current length.
 *
 * Complexity:
 * Time(: O(b), b number of bits in number
 */

#include "stdio.h"

unsigned short int max(unsigned short int A, unsigned short int B) {
  return A > B ? A : B;
}

unsigned int flip_a_bit_to_get_max_seq_of_ones(int n) {
  unsigned short int current_len = 0, previous_len = 0, max_len = 1;

  // If -1, all bits set as 1, return max bits in integer.
  if (~0 == n)  
    return sizeof(int) * 8;

  while (n) {
    if (n & 1)
      current_len++;
    else {
      // If LSB is 0, check next bit (left side), if it is 0 then previous
      // length will be 0 as we can't combine these 2 sequence because there are
      // more than one 0 between 2 sequence of 1s.
      previous_len = n & 2 ? current_len : 0;
      current_len = 0;
    }
    n = n >> 1; 
    max_len = max(max_len, previous_len + current_len + 1);
  }
  return max_len;
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
  int number = 0;
  printf("Enter a number: ");
  scanf("%d", &number);
  binary_representation(number);
  printf("Max number of 1s in sequence after flipping bit is: %d\n",
      flip_a_bit_to_get_max_seq_of_ones(number));
  return 0;
}

/*
Output:

Enter a number: 8000
Binary representation of 8000 is: 0000 0000 0000 0000 0001 1111 0100 0000
Max number of 1s in sequence after flipping bit is: 7

Enter a number: 7
Binary representation of 7 is: 0000 0000 0000 0000 0000 0000 0000 0111
Max number of 1s in sequence after flipping bit is: 4

Enter a number: 17
Binary representation of 17 is: 0000 0000 0000 0000 0000 0000 0001 0001
Max number of 1s in sequence after flipping bit is: 2
*/
