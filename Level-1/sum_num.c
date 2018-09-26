/*
 * Date: 2018-09-26
 *
 * Description:
 * Find sum of all digits for a given number.
 *
 * Approach:
 * Take modulus of number to get trailing digit and divide by 10 have get next
 * trailing digit.
 */

#include "stdio.h"

int main() {
  int i = 0;
  int num, sum = 0, val;
  printf("Enter number: ");
  scanf("%d", &num);

  for (i = num; i > 0; val = num % 10, sum += val, num = num / 10, i = num);

  printf("Sum is: %d\n", sum);
  return 0;
}
