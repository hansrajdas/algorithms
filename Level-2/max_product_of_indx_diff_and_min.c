/*
 * Date: 2018-10-14
 *
 * Description:
 * Given an unsorted array, find max value of abs(i - j)*min(a[i], a[j]).
 *
 * Approach:
 * - Take 2 pointers at start and end of array and loop until end is more than
 *   start.
 * - If A[start] < A[end], find (end - start)*A[start] and increment start.
 * - Else find (end - start)*A[end] and decrement end.
 * - Update result with new value if new value comes out to be more than result.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0;
  int *A = NULL;
  int max_prod = 0, curr_prod = 0;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  i = 0;
  j = n - 1;
  while (i < j) {
    if (A[i] < A[j]) {
      curr_prod = (j - i)*A[i];
      i++;
    }
    else {
      curr_prod = (j - i)*A[j];
      j--;
    }
    max_prod = max_prod > curr_prod ? max_prod : curr_prod;
  }
  printf("Max value of abs(i - j)*min(a[i], a[j]) is: %d\n", max_prod);
  return 0;
}


/*
 * Output:
 * --------------------
 *
 * Enter number of elements: 5
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Enter element[4]: 5
 * Max value of abs(i - j)*min(a[i], a[j]) is: 6
 *
 * Enter number of elements: 5
 * Enter element[0]: 5
 * Enter element[1]: 4
 * Enter element[2]: 3
 * Enter element[3]: 2
 * Enter element[4]: 1
 * Max value of abs(i - j)*min(a[i], a[j]) is: 6
 *
 * Enter number of elements: 7
 * Enter element[0]: 2
 * Enter element[1]: 5
 * Enter element[2]: 1
 * Enter element[3]: 4
 * Enter element[4]: 9
 * Enter element[5]: 3
 * Enter element[6]: 8
 * Max value of abs(i - j)*min(a[i], a[j]) is: 25
 */
