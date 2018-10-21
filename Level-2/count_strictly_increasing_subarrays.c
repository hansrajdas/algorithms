/*
 * Date: 2018-10-21
 *
 * Description:
 * Given an array of integers, count number of subarrays (of size more than one)
 * that are strictly increasing.
 * Example:
 * Input: arr[] = {1, 4, 3}
 * Output: 1, There is only one subarray {1, 4}
 *
 * Input: arr[] = {1, 2, 2, 4}
 * Output: 2, There are 2 subarrays {1, 2} and {2, 4}
 *
 * Approach:
 * Uses maths formula, if there are N increasing numbers we can have N*(N-1)/2
 * total sets possible.
 *
 * So, scan array from starting and increment a temp counter as elements are in
 * increasing order. As element decrements update total-sets with
 * temp*(temp-1)/2
 *
 * Don't forget to update total-sets outside loop, this will take care of last
 * increasing subarray.
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
  int tmp_len = 1;
  int total_sets = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  for (i = 0; i < (n - 1); i++) {
    if (A[i] < A[i + 1])
      tmp_len++;
    else {
      total_sets += (tmp_len * (tmp_len - 1))/2;
      tmp_len = 1;
    }
  }
  total_sets += (tmp_len * (tmp_len - 1))/2;  // Take care of last incr numbers
  printf("Total sets: %d\n", total_sets);
  return 0;
}


/*
 * Output:
 * -------------------
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 4
 * Enter element[2]: 3
 * Total sets: 1
 *
 * Enter number of elements: 4
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Total sets: 6
 *
 * Enter number of elements: 4
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 2
 * Enter element[3]: 4
 * Total sets: 2
 *
 * Enter number of elements: 4
 * Enter element[0]: 5
 * Enter element[1]: 4
 * Enter element[2]: 3
 * Enter element[3]: 2
 * Total sets: 0
 */
