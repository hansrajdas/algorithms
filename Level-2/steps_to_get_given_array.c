/*
 * Date: 2018-11-07
 *
 * Description:
 * Given an array, find the number of steps required to make an array of all
 * 0s (of size N) to given array. Steps allowed are:
 * 1. Incremental operations: Choose 1 element from the array and increment its
 *    value by 1.
 * 2. Doubling operation: Double the values of all the elements of array.
 *
 * Approach:
 * This can be solved by following the reverse approach that is, instead of
 * making an array of all 0s to given array, we will find the number of steps
 * required to make give array to all 0s.
 * Taking reverse approach, we have to consider given operations also in
 * opposite way that is increment operation will become decrement operation and
 * doubling operation will become dividing all elements by 2.
 * Now:
 * - Scan all elements, if we encounter a odd number break
 * - If no odd was encountered divide all array elements by 2
 * - If all elements has become 0, return number of steps
 * - If odd found, decrement 1 from each odd number
 *
 * Complexity:
 * O(K*N)
 * K = Some variable factor which depends on distribution of elements given
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0;
  int *A = NULL;
  int steps = 0;
  int num_zero = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(n*sizeof(int));
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  while (1) {
    num_zero = 0;
    for (i = 0; i < n; i++) {
      if (A[i] & 1)  // Found an odd number
        break;
      else if (!A[i])
        num_zero++;
    }
    if (num_zero == n) {
      printf("Number of steps required: %d\n", steps);
      return steps;
    }
    else if (i == n) {  // All elements in array even or even + 0s
      for (j = 0; j < n; j++)
        A[j] /= 2;
      steps++;
    }

    // Decrement 1 from all odd numbers to make it even
    for (j = i; j < n; j++) {
      if (A[j] & 1) {
        A[j] -= 1;
        steps++;
      }
    }
  }
  free (A);
}


/*
 * Output:
 * ------------------
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Number of steps required: 5
 *
 * Enter number of elements: 5
 * Enter element[0]: 2
 * Enter element[1]: 2
 * Enter element[2]: 2
 * Enter element[3]: 4
 * Enter element[4]: 4
 * Number of steps required: 7
 */
