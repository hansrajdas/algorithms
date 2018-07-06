/**
 * Date: 2018-07-06
 *
 * Description:
 * Given a fractional number between 0 to 1, print its binary representation.
 *
 * Reference:
 * http://cs.furman.edu/digitaldomain/more/ch6/dec_frac_to_bin.htm
 */

#include "stdio.h"

void decimal_fraction_to_binary(float n) {
  printf("0.");
  while (1) {
    n = n * 2;
    if (n > 1) {
      printf("1");
      n = n - 1;
    }
    else if (n < 1) {
      printf("0");
    }
    else {
      printf("1\n");
      break;
    }
  }
}

int main() {
  float number = 0.0;
  printf("Enter number between 0 and 1: ");
  scanf("%f", &number);
  if (number >= 1 || number <= 0)
    printf("Invalid input\n");
  else
    decimal_fraction_to_binary(number);
  return 0;
}

/*
Output:

Enter number between 0 and 1: 0.125
0.001

Enter number between 0 and 1: 0.0625
0.0001

Enter number between 0 and 1: 0.7
0.101100110011001100110011

Enter number between 0 and 1: 0.99
0.1111110101110000101001

Enter number between 0 and 1: 0.3
0.010011001100110011001101

Enter number between 0 and 1: 0.1
0.000110011001100110011001101
*/
