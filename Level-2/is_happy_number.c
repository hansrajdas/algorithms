/*
 * Date: 2018-09-17
 *
 * Description:
 * Check is a number is happy or not. A number is said to happy if sum of
 * squares of digits reaches 1 by repeating this any number of times.
 * https://en.wikipedia.org/wiki/Happy_number
 *
 * Approach:
 * Use same approach as used to detect loop in a linked list(rabbit rat
 * problem).
 * Slow variable will perform sum of squares of digit once and fast will do this
 * twice. If both becomes same at any point of time it means that there is some
 * number which is getting repeated so number can't be a happy number.
 *
 * Complexity:
 * Linear
 */

#include "stdio.h"

#define TRUE 1
#define FALSE 0

int get_sum_of_squares(unsigned long int n) {
  int sum = 0, d = 0;
  while (n) {
    d = n % 10;
    n = n / 10;
    sum += d * d;
  }
  return sum;
}

int is_happy_number(unsigned long int n) {
  unsigned long slow = n;
  unsigned long fast = n;

  while (TRUE) {
    slow = get_sum_of_squares(slow);
    fast = get_sum_of_squares(get_sum_of_squares(fast));

    // Found a sum of 1, it is a happy number.
    if (slow == 1)
      return TRUE;

    // Both fast and slow reach to same number, can't be a happy number.
    if (slow == fast)
      return FALSE;
  }
}

int main() {
  unsigned long int n = 0;
  printf("Enter number: ");
  scanf("%ld", &n);

  if (is_happy_number(n))
    printf("%ld is a happy number\n", n);
  else
    printf("%ld is not a happy number\n", n);
  return 0;
}
