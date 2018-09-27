/*
 * Date: 2018-09-26
 *
 * Description:
 * Given a float number, round it off to the nearest integer
 * -3.7 should be 4
 *  3.7 should be 5
 *
 * Approach:
 * For positive add 0.5, for negative subtract 0.5 and take integral part
 *
 * Complexity:
 * O(1)
 */

#include "stdio.h"

int main() {
  int i = 0;
  float f = -3.7;
  i = f > 0 ? f + 0.5 : f - 0.5;
  printf("%d\n", i);
  return 0;
}
