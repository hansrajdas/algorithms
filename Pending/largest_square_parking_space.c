/*
 * Date: 2018-08-08
 *
 * Description:
 * There is a parking lot represented by NxN 2-D array matrix
 * (if matrix[i][j] = 0 is occupied and matrix[i][j] = 1 is vacant space).
 * Task is to find largest square matrix having vacant space. In other words
 * find largest k such that there exists a k*k square in matrix containing all
 * 1s and no 0s.
 *
 * Refer: Second problem from https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec24.pdf
 *
 * Approach:
 *
 * Complexity:
 * O(n^2)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++)
  {
    printf("Enter element [%d]: ", i);
    scanf("%d",&a[i]);
  }
  return 0;
}
