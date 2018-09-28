/*
 * Date: 2018-09-28
 *
 * Description:
 * Find 2 repeating numbers in an array having elements from 1 to n - 2, where
 * n is the number of elements in given array. Apart from these 2 numbers all
 * others are non repeating.
 *
 * Approach:
 * As numbers are from 1 to n - 2, we can take XOR of all elements and again XOR
 * of numbers from 1 to n - 2. This will nullify all non repeating elements and
 * consolidated XOR will only have values corresponding to 2 repeating numbers.
 *
 * Now we can find the last LSB set in consolidated XOR and accumulate all
 * numbers by again XORing all numbers and numbers from 1 to n - 2.
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
  int xor, set_bit;
  int x = 0;
  int y = 0;

  printf("Enter number of elements: ");
  scanf("%d", &num_of_elements);
  p_input = (int *)malloc(sizeof(int) * num_of_elements);

  for (i = 0; i < num_of_elements; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &p_input[i]);
  }

  xor = p_input[0];
  for (i = 1; i < num_of_elements; i++)
    xor ^= p_input[i];

  for (i = 1; i <= num_of_elements - 2; i++)
    xor ^= i;

  set_bit = xor & ~(xor - 1);
  for (i = 0; i < num_of_elements; i++) {
    if (set_bit & p_input[i])
      x ^= p_input[i];
    else
      y ^= p_input[i];
  }
  for (i = 1; i <= num_of_elements - 2; i++) {
    if (set_bit & i)
      x ^= i;
    else
      y ^= i;
  }
  printf("\nTwo repeating numbers are: %d %d\n", x, y);
  return 0;
}

/*
 * Output:
 * -------------
 * Enter number of elements: 10
 * Enter element[0]: 2
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 3
 * Enter element[4]: 1
 * Enter element[5]: 4
 * Enter element[6]: 5
 * Enter element[7]: 6
 * Enter element[8]: 7
 * Enter element[9]: 8
 *
 * Two repeating numbers are: 3 2
 */
