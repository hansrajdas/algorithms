/*
 * Date: 2018-06-23
 *
 * Description:
 * Rotate a square matrix clockwise by 90 degrees.
 * 
 * Approach used is traversing matrix layer by layer and copying elements from
 * left to top, bottom to left, right to bottom and top to right as this is a
 * clockwise rotation. Example:
 *
 * A00 A01 A02          A20 A10 A00
 * A10 A11 A12    =>    A21 A11 A01
 * A20 A21 A22          A22 A12 A02
 *
 * Complexity:
 * O(N^2)
 *
 * See approach 2: https://leetcode.com/problems/rotate-image/
 */

#include "stdio.h"

void print_matrix(int m[][10], int n, char *msg) {
  int i = 0, j = 0;
  printf("\n%s\n", msg);
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++)
      printf("%d ", m[i][j]);
    printf("\n");
  }
}

/*
 * Rotates a square matrix clockwise by 90 degrees.
 * 
 * Args:
 * m: Matrix
 * n: Size of matrix.
 */
void rotate_matrix_clockwise_by_90_degrees(int m[][10], int n) {
  int layer = 0, offset = 0, first = 0, last = 0, idx = 0, top = 0;

  for (layer = 0; layer < n/2; layer++) {
    first = layer;
    last = n - 1 - layer;
    for (idx = first; idx < last; idx++) {
      offset = idx - first;
      top = m[layer][idx];  // Save top element.

      m[layer][idx] = m[last - offset][first];  // top <- left

      m[last - offset][first] = m[last][last - offset];  // left <- bottom
      
      m[last][last - offset] = m[idx][last];  // bottom <- right

      m[idx][last] = top;  // right <- top
    }
  }
  print_matrix(m, n, "Rotated matrix:");
}

int main() {
  int matrix[10][10] = {0};
  int i = 0, j = 0, n = 0;

  printf("Enter number of rows/columns of square matrix: ");
  scanf("%d", &n);
  for (;i < n; i++) {
    for (j = 0; j < n; j++) {
      printf("Enter element matrix[%d][%d]: ", i, j);
      scanf("%d", &matrix[i][j]);
    }
  }
  print_matrix(matrix, n, "Entered matrix:");

  rotate_matrix_clockwise_by_90_degrees(matrix, n);
  return 0;
}
