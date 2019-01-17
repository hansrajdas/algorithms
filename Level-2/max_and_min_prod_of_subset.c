/*
 * Date: 2018-10-13
 *
 * Description:
 * Given an unsorted array of integers(+ve, -ve and 0s). Find max and min
 * product from any subset of that array.
 *
 * Approach:
 * Firstly find product of all non-zero integers, call it prod_of_all.
 * Now, below are the cases:
 * - Array has all non-negative numbers, this will be max product and min
 * number in array will be min product.
 * - Array has negatives but prod_of_all is positive, this is the max prod and
 * min prod will be prod_of_all/max-negative.
 *
 * This is the basic logic, there are few other cases to handled.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0;
  int *A = NULL;
  int prod_of_all = 1;
  int num_of_negatives = 0;
  int is_zero_present = 0;
  int max_negative_num = -65535;
  int min_positive = 65536;
  int max_prod = 1, min_prod = 1;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }
  for (i = 0; i < n; i++) {
    if (!A[i]) {
      is_zero_present++;
      continue;
    }
    else if (0 > A[i]) {
      num_of_negatives++;
      if (max_negative_num < A[i])
        max_negative_num = A[i];
    }
    else {
      if (A[i] < min_positive)
        min_positive = A[i];
    }
    prod_of_all *= A[i];
  }
  if (!num_of_negatives) {
    max_prod = prod_of_all;
    min_prod = is_zero_present ? 0 : min_positive;
  } else {
    if (0 > prod_of_all) {
      max_prod = prod_of_all/max_negative_num;
      min_prod = prod_of_all;
    } else {
      max_prod = prod_of_all;
      min_prod = prod_of_all/max_negative_num;
    }
  }
  printf("Max prod: %d\nMin prod: %d\n", max_prod, min_prod);
  return 0;
}


/*
 * Output:
 * -------------------------
 * Enter number of elements: 5
 * Enter element[0]: 9
 * Enter element[1]: 1
 * Enter element[2]: 2
 * Enter element[3]: 5
 * Enter element[4]: 6
 * Max prod: 540
 * Min prod: 1
 *
 * Enter number of elements: 5
 * Enter element[0]: -9
 * Enter element[1]: -1
 * Enter element[2]: -2
 * Enter element[3]: -5
 * Enter element[4]: -6
 * Max prod: 540
 * Min prod: -540
 *
 * Enter number of elements: 5
 * Enter element[0]: 0
 * Enter element[1]: 3
 * Enter element[2]: 6
 * Enter element[3]: 1
 * Enter element[4]: 2
 * Max prod: 36
 * Min prod: 0
 */ 
