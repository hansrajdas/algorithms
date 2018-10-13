/*
 * Date: 2018-10-13
 *
 * Description:
 * Given an array consisting of n positive integers, and an integer k. Find the
 * largest product subarray of size k, i.e., find maximum produce of k
 * contiguous elements in the array where k <= n.
 *
 * Approach:
 * Initially find product of first k numbers then starting from kth index
 * multiply kth element and divide first element(i - k) check if new product
 * is more than max already calculated.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0, k = 0;
  int *A = NULL;
  int start_idx, max_product = 1, tmp_prod = 1;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }
  printf("Enter subarray size(k): ");
  scanf("%d", &k);
  for (i = 0; i < k; i++)
    max_product = max_product * A[i];

  start_idx = 0;
  tmp_prod = max_product;
  for (i = k; i < n; i++) {
    if (A[i - k])
      tmp_prod = (tmp_prod * A[i]) / A[i - k];
    else
      tmp_prod = A[i];

    if (max_product < tmp_prod) {
      max_product = tmp_prod;
      start_idx = i - k + 1;
    }
  }
  printf("Max product is: %d\n", max_product);
  printf("Elements are: ");
  for (i = start_idx; i < start_idx + k; i++)
    printf("%d ", A[i]);
  printf("\n");
  return 0;
}

/*
 * Output:
 * -----------------------------
 * Enter number of elements: 10
 * Enter element[0]: 1
 * Enter element[1]: 5
 * Enter element[2]: 9
 * Enter element[3]: 8
 * Enter element[4]: 2
 * Enter element[5]: 4
 * Enter element[6]: 1
 * Enter element[7]: 8
 * Enter element[8]: 1
 * Enter element[9]: 2
 * Enter subarray size(k): 6
 * Max product is: 4608
 * Elements are: 9 8 2 4 1 8 
 *
 * Enter number of elements: 6
 * Enter element[0]: 2
 * Enter element[1]: 5
 * Enter element[2]: 8
 * Enter element[3]: 1
 * Enter element[4]: 1
 * Enter element[5]: 3
 * Enter subarray size(k): 3
 * Max product is: 80
 * Elements are: 2 5 8 
 */ 
