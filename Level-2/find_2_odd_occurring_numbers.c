/*
 * Date: 2018-09-28
 *
 * Description:
 * Given an array in which 2 numbers has odd number of occurrence and all other
 * has even number of occurrences. Find 2 numbers which occurred odd number of
 * times.
 *
 * Approach:
 * - Take XOR of all numbers, this will nullify(0) all bits corresponding to
 *   all even occurring numbers and will contain set bits only at positions
 *   where bit is set for only of the 2 numbers like 01^10 = 11, 111^100 = 011
 *
 * - Now we can first(LSB) set bit in consolidated XOR using:
 *   xor & ~(xor - 1) like 6 = 110, set bit = 110 & ~(101) = 110 & 010 = 010
 *   which has second LSB as set and 6 also has first LSB set second position.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int num_of_elements = 0;
  int *p_input = NULL;
  int xor = 0;
  int set_bit = 0;
  int x = 0, y = 0;

  printf("Enter number of elements: ");
  scanf("%d", &num_of_elements);
  p_input = (int *)malloc(sizeof(int) * num_of_elements);

  for (i = 0; i < num_of_elements; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d",&p_input[i]);
  }

  xor = p_input[0];
  for (i = 1; i < num_of_elements; i++)
    xor ^= p_input[i];

  set_bit = xor & ~(xor - 1);
  for (i = 0; i < num_of_elements; i++) {
    if (set_bit & p_input[i])
      x ^= p_input[i];
    else
      y ^= p_input[i];
  }
  printf("Two numbers occurring odd number of times is: %d %d\n", x, y);
  return 0;
}


/*
 * Output:
 * -----------------
 * Enter number of elements: 6
 * Enter element[0]: 7
 * Enter element[1]: 7
 * Enter element[2]: 7
 * Enter element[3]: 7
 * Enter element[4]: 15
 * Enter element[5]: 31
 * Two numbers occurring odd number of times is: 31 15
 */
