/*
 * Date: 2018-07-24
 *
 * Description:
 * Given an M*N matrix in which each row and each column is sorted in ascending
 * order, write a method to find an element.
 *
 * Approach:
 * - If the start of a column is greater than x, then x is to the left of that
 *   column.
 * - If a row element is less than x, then x will be below that row.
 *
 * So in each comparison, either a row or a column of matrix is discarded.
 *
 * Complexity:
 * O(M + N)
 *
 * Note:
 * Another simple solution would be to do a binary search on each row, this will
 * have complexity of O(M*log(N)). Drawback will be, it will not utilize the
 * fact that columns are also sorted.
 */

#include "stdio.h"

#define TRUE 1
#define FALSE 0

#define M 4  // Rows.
#define N 4  // Columns.

int sorted_search_matrix(int matrix[][N], int elem) {
  int row = 0, col = N - 1;
  while (row < M && col >= 0) {
    if (matrix[row][col] == elem)
      return TRUE;
    else if(matrix[row][col] > elem)
      col--;
    else
      row++;
  }
  return FALSE;
}

int main() {
  int matrix[M][N] = {
                      {1,  2,  3,  10},
                      {4,  5,  6,  11},
                      {7,  8,  9,  13},
                      {12, 15, 16, 17}
                     };
  int elem = 0;
  printf("Enter element to be search in sorted matrix: ");
  scanf("%d", &elem);
  
  if (sorted_search_matrix(matrix, elem))
    printf("%d, found in matrix!\n", elem);
  else
    printf("%d, *NOT* found in matrix!\n", elem);
  return 0;
}
