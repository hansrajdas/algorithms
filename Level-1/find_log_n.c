/*
 * Date: 2018-09-07
 *
 * Description:
 * Fing log(n) with some base.
 *
 * Complexity:
 * O(n/b) where n = number, b = base.
 */

#include "stdio.h"

int find_log_n(int base, int num) {
  return (num >= base ? 1 + find_log_n(base, num/base) : 0);
}

int main() {
  int num = 0, base = 0;
  printf("Enter base: ");
  scanf("%d", &base);
  printf("Enter number: ");
  scanf("%d", &num);
  printf("log(n) - %d\n", find_log_n(base, num));
  return 0;
}


/*
 * Output
 * ----------------
 * Enter base: 2
 * Enter number: 8
 * log(n) - 3
 */

