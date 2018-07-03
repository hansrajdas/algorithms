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
  unsigned short int space = 0;
  unsigned int i = 0;
  printf("Binary representation of %d is: ", n);

  // Checking bit at individual position and printing 0 or 1.
  for (i = 1 << size - 1; i > 0; i = i/2) {
    if (space == 4) {
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
  int n = 0;
  printf("Enter number: ");
  scanf("%d", &n);
  binary_representation(n);
  return 0;
}

/*
Enter number: 2
Binary representation of 2 is: 0000 0000 0000 0000 0000 0000 0000 0010

Enter number: 5
Binary representation of 5 is: 0000 0000 0000 0000 0000 0000 0000 0101

Enter number: 1
Binary representation of 1 is: 0000 0000 0000 0000 0000 0000 0000 0001

Enter number: -1
Binary representation of -1 is: 1111 1111 1111 1111 1111 1111 1111 1111

Enter number: 44
Binary representation of 44 is: 0000 0000 0000 0000 0000 0000 0010 1100

Enter number: 128
Binary representation of 128 is: 0000 0000 0000 0000 0000 0000 1000 0000
*/
