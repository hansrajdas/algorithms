/*
 * Date: 2018-10-05
 *
 * Description:
 * Given a sorted array and a sum, find the number triplets whose sum is less
 * than given sum.
 *
 * Approach:
 * Take a element as reference and find other 2 numbers using 2 pointers, left
 * and right.
 *
 * Complexity:
 * O(N^2)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, left = 0, right = 0;
  int n = 0;
  int *A = NULL;
  int count = 0, sum = 0;
  printf("Enter sum: ");
  scanf("%d", &sum);

  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  for (i = 0; i < n - 1; i++) {
    left = i + 1;
    right = n - 1;
    while (left < right) {
      if(A[i] + A[left] + A[right] >= sum)
        right--;
      else {
        // If A[left] + A[i] + A[right] is less than sum, then all right
        // elements greater than A[left] will also have sum less than given
        // sum so adding right - left to count.
        count += (right - left);
        left++;
      }
    }
  }
  printf("Triplets with sum less than %d is: %d\n", sum, count);
  return 0;
}


/*
 * Output:
 * -------------------
 * Enter sum: 10
 * Enter number of elements: 5
 * Enter element[0]: 3
 * Enter element[1]: 4
 * Enter element[2]: 5
 * Enter element[3]: 6
 * Enter element[4]: 7
 * Triplets with sum less than 10 is: 0
 *
 * Enter sum: 10
 * Enter number of elements: 5
 * Enter element[0]: 2
 * Enter element[1]: 3
 * Enter element[2]: 4
 * Enter element[3]: 5
 * Enter element[4]: 6
 * Triplets with sum less than 10 is: 1
 */
