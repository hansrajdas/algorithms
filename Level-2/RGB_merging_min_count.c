/*
 * Date: 2018-10-21
 *
 * Description:
 * Given an array of characters having elements R, G and B, find the minimum
 * elements left after all possible merging. Merging happens between 2 adjacent
 * elements if they are different and becomes third type.
 *
 * Approach:
 * - If all elements are of same type i.e. either all are R or all are G or all
 *   are B, no merging possible so n should be the answer.
 * - If count of all are odd or count of all are even, they all will eventually
 *   merge to 2 items.
 * - Otherwise they will surely merge to single item.
 *
 * Consider taking few examples to have proof of above statements.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"
#include "string.h"

int main() {
  int i = 0;
  int n = 0;
  char A[50] = {'\0'};
  int r = 0, g = 0, b = 0;
  printf("Enter string of RGBs: ");
  scanf("%s", A);
  n = strlen(A);

  for (i = 0; i < n; i++) {
    if ('R' == A[i])
      r++;
    else if ('G' == A[i])
      g++;
    else if ('B' == A[i])
      b++;
    else
      printf("Invalid input\n");
      return -1;
  }

  if ((r == n) || (g == n) || (b == n))
    printf("Minimum possible value - %d\n", n);
  else if (((r & 1) && (g & 1) && (b & 1)) || (!(r & 1) && !(g & 1) && !(b & 1)))
    printf("Minimum possible value - 2\n");
  else
    printf("Minimum possible value - 1\n");
  return 0;
}

/*
 * Output:
 * ------------------------
 * Enter string of RGBs: RGB
 * Minimum possible value - 2
 *
 * Enter string of RGBs: GGG
 * Minimum possible value - 3
 *
 * Enter string of RGBs: RRGGBB
 * Minimum possible value - 2
 *
 * Enter string of RGBs: RRGB
 * Minimum possible value - 1
 */
