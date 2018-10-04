/*
 * Date: 2018-10-05
 *
 * Description:
 * Convert a given ASCII string to it's corresponding integer value.
 * For example:
 * '123' => 123
 * '099' => 99
 *
 * Approach:
 * Scan string from right to left and take its 4 LSB bits(this will give us
 * integer part as '0' is 0x30 and 4 LSB would be 0 and so on for others).
 * Multiply existing result by 10 so that it gets shifted left by 1 place and
 * current digit at 0s place.
 *
 * Complexity:
 * O(n), n = Length of string given
 */


#include "stdio.h"

int main() {
  char num[10] = {'\0'};
  int result = 0, i = 0;
  printf("Enter number: ");
  scanf("%s", num);
  while ('\0' != num[i]) {
    // This multiplies result by 10 8x + 2x and takes 4 LSB of current
    // character.
    result = (result << 3) + (result << 1) + (num[i] & 15);
    i++;
  }
  printf("Number is: %d\n", result);
}


/*
 * Output:
 * --------------------
 * Enter number: 5
 * Number is: 5
 *
 * Enter number: 8365
 * Number is: 8365
 *
 * Enter number: 099
 * Number is: 99
 */
