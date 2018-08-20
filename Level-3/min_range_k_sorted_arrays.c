/*
 * Date: 2018-08-20
 *
 * Description:
 * There are k sorted arrays and we need to find the minimum range of number
 * which will have at least one element from each array. Solve for k = 3.
 * Example:
 * array-1: [4, 10, 15, 24]
 * array-2: [0, 9, 12, 20]
 * array-3: [5, 18, 22, 30]
 *
 * Minimum range would be 20 to 24 i.e 4 as range 20 to 24 contains elements
 * from all k(=3) arrays. array-1 has 24, array-2 has 20 and array-3 has 22.
 *
 * Approach:
 * Take 3 pointers starting from first element of each array and compute range
 * and save. Now increment pointer pointing to minimum element and compute range
 * again if range is less than previously saved than update range otherwise move
 * further in same fashion.
 *
 * Complexity:
 * O(n*k) time, O(1) space
 * Can be improved to O(n*log(k)) by using min heap to keep track of minimum
 * element.
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n1 = 0, n2 = 0, n3 = 0;
  int *a1 = NULL, *a2 = NULL, *a3 = NULL;
  printf("Enter number of elements in first array: ");
  scanf("%d", &n1);
  a = (int *)malloc(sizeof(int) * n1);
  for (i = 0; i < n1; i++)
  {
    printf("Enter element [%d]: ", i);
    scanf("%d",&a1[i]);
  }
  return 0;
}
