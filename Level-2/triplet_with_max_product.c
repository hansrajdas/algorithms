/*
 * Date: 2018-10-13
 *
 * Description:
 * Given an unsorted array, find triplet having max product.
 *
 * Approach:
 * Max triplet product is possible by multiplying max 3 numbers or one max
 * positive and 2 min negative numbers. So scan array once and find these 5
 * numbers and check which combination is giving max.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

#define MAX_INT 1 << 30
#define MIN_INT 1 << 31

int main() {
  int i = 0;
  int n = 0;
  int *A = NULL;
  int max = MIN_INT, secondMax = MIN_INT, thirdMax = MIN_INT;
  int min = MAX_INT, seconsMin = MAX_INT;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  for (i = 0; i < n; i++) {

    // Compute first, second and third max
    if (max < A[i]) {
      thirdMax = secondMax;
      secondMax = max;
      max = A[i];
    }
    else if (secondMax < A[i]) {
      thirdMax = secondMax;
      secondMax = A[i];
    }
    else if (thirdMax < A[i])
      thirdMax = A[i];

    // Compute min and second min
    if (min > A[i]) {
      seconsMin = min;
      min = A[i];
    }
    else if (seconsMin > A[i])
      seconsMin = A[i];
  }

  /*
   * 2 case possible to get max product:
   * - Multiply max 3 numbers(all positive)
   * - Multiply max positive and 2 mins(negative)
   */
  if (max * secondMax * thirdMax > max * min * seconsMin) {
    printf("Triplet having max product is: %d %d %d\n",
      max, secondMax, thirdMax);
    printf("Max product: %d\n", max * secondMax * thirdMax);
  }
  else {
    printf("Triplet having max product is: %d %d %d\n", max, min, seconsMin);
    printf("Max product: %d\n", max * min * seconsMin);
  }
  return 0;
}


/*
 * Output:
 * ----------------------------
 * Enter number of elements: 5
 * Enter element[0]: 2
 * Enter element[1]: 3
 * Enter element[2]: -4
 * Enter element[3]: 5
 * Enter element[4]: 6
 * Triplet having max product is: 6 5 3
 * Max product: 90
 *
 * Enter number of elements: 5
 * Enter element[0]: -2
 * Enter element[1]: -3
 * Enter element[2]: 5
 * Enter element[3]: 6
 * Enter element[4]: 2
 * Triplet having max product is: 6 5 2
 * Max product: 60
 *
 * Enter number of elements: 5
 * Enter element[0]: -10
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 6
 * Enter element[4]: -20
 * Triplet having max product is: 6 -20 -10
 * Max product: 1200
 */ 
