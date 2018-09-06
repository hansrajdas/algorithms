/*
 * Date: 2018-09-06
 *
 * Description:
 * Check if a number is multiple of 4 or not without using / operator.
 *
 * Approach:
 * In decimal system a number is divisible by 4 if it's 2 least significant
 * digits are divisible by 4 so just masked 2 LSBs and checked.
 *
 * Complexity:
 * O(1)
 */

#include "stdio.h"

int main() {
  int i = 0;
  printf("Enter number:");
  scanf("%d", &i);

  if (!(i & 0x3))
    printf("Yes\n");
  else
    printf("No\n");
  return 0;
}
