/*
 * Date: 2017-xx-xx
 *
 * Description:
 * Print first n finonacci numbers.
 *
 * Complexity:
 * O(n)
 */

#include "stdio.h"

int main() {
  int n = 1;
  int i = 0;
  int val1 = 0;
  int val2 = 1;
  int prev;
  printf("Enter n: ");
  scanf("%d", &n);
  for (; i < n; i++) {
    if (!i)
      printf("%d", val1);
    else if(1 == i)
      printf(" %d", val2);
    else {
      printf(" %d", (val1 + val2));
      prev = val1;
      val1 = val2;
      val2 = prev + val2;
    }
  }
  printf("\n");
  return 0;
}
