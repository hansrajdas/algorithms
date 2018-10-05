/*
 * Date: 2018-10-05
 *
 * Description:
 * Given a sorted array and a sum X, find number of triplets which sums to X.
 *
 * Approach:
 * Take a number and check for other 2 numbers on left and right side of
 * reference number.
 *
 * Complexity:
 * O(N^2)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0;
  int *A = NULL;
  int left = 0, right = 0;
  int sum = 0;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);

  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  printf("Enter sum: ");
  scanf("%d", &sum);

  for (i = 0; i < n - 2; i++) {
    left = i + 1;
    right = n - 1;
    while (left < right) {
      if (A[left] + A[i] + A[right] == sum) {
        printf("Triplet set: %d %d %d\n", A[left], A[i], A[right]);
        left++;
        right--;
      }
      else if (A[left] + A[i] + A[right] > sum)
        right--;
      else
        left++;
    }
  }
  return 0;
}


/*
 * Output:
 * --------------
 * Enter number of elements: 5
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Enter element[4]: 5
 * Enter sum: 6
 * Triplet set: 2 1 3 
 */
