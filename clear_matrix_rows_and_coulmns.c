/*
 * Date: 2018-06-25
 *
 * Description:
 * If an element in a matrix is 0, its entire row and column are set to 0.
 *
 * Approach:
 * Use first row and column in matrix to store indexes where in matrix we have
 * 0 and scan first row and column in next iteration to clear corresponding
 * row/column.
 * Also, check initially if first row and column had a 0, need to clear first
 * row/column also.
 *
 * Complexity:
 * Time: O(MxN), Space: O(1)
 */

#include "stdio.h"

typedef unsigned short int SHORT;

void print_matrix(SHORT M[][10], SHORT m, SHORT n, char *msg) {
  SHORT i = 0, j = 0;
  printf("\n%s\n", msg);
  for (i = 0; i < m; i++) {
    for (j = 0; j < n; j++)
      printf("%hu\t", M[i][j]);
    printf("\n");
  }
}

/*
 * Clears all elements in a row with given row index.
 *
 * Args:
 * M: Matrix
 * row_idx: Index of row which needs to be cleared.
 * columns_in_matrix: Number of columns in matrix.
 */
void clear_row(SHORT M[][10], SHORT row_idx, SHORT columns_in_matrix) {
  SHORT i = 0;
  for (i = 0; i < columns_in_matrix; i++) {
    M[row_idx][i] = 0;
  }
}

/*
 * Clears all elements in a column with given column index.
 *
 * Args:
 * M: Matrix
 * column_idx: Index of column which needs to be cleared.
 * rows_in_matrix: Number of rows in matrix.
 */
void clear_column(SHORT M[][10], SHORT column_idx, SHORT rows_in_matrix) {
  SHORT i = 0;
  for (i = 0; i < rows_in_matrix; i++) {
    M[i][column_idx] = 0;
  }
}

/*
 * If 0 is found in a matrix, it clears corresponding row and column.
 * 
 * Args:
 * M: Matrix
 * m: Number of rows in matrix.
 * n: Number of columns in matrix.
 */
void clear_matrix_rows_and_cols(SHORT M[][10], SHORT m, SHORT n) {
  SHORT first_row_has_zero = 0, first_col_has_zero = 0;
  SHORT i = 0, j = 0;

  // Scan first column and check, if there is a zero.
  for (i = 0; i < m; i++) {
    if (!M[i][0])
      first_col_has_zero = 1;
  }

  // Scan first row and check, if there is a zero.
  for (j = 0; j < n; j++) {
    if (!M[0][j])
      first_row_has_zero = 1;
  }

  // Scan matrix excluding first row and column to check for zeros. If found
  // store in first row and column.
  for (i = 1; i < m; i++) {
    for (j = 1; j < n; j++) {
      if (!M[i][j]) {
        M[i][0] = 0;
        M[0][j] = 0;
      }
    }
  }

  // Check which rows needs to be cleared, scan first column for this.
  for (i = 1; i < m; i++) {
    if (!M[i][0])
      clear_row(M, i, n);
  }

  // Check which column needs to be cleared, scan first row for this.
  for (j = 1; j < n; j++) {
    if (!M[0][j])
      clear_column(M, j, m);
  }

  // If first row and column had zero, then clear first row and column
  // respectively.
  if (first_row_has_zero)
    clear_row(M, 0, n);

  if (first_col_has_zero)
    clear_column(M, 0, m);
  
  print_matrix(M, m, n, "Output matrix: ");
}

int main() {
  SHORT matrix[10][10] = {0};
  SHORT i = 0, j = 0, rows = 0, cols = 0;

  printf("Enter number of rows in matrix: ");
  scanf("%hu", &rows);
  printf("Enter number of cols in matrix: ");
  scanf("%hu", &cols);
  for (;i < rows; i++) {
    for (j = 0; j < cols; j++) {
      printf("Enter element matrix[%d][%d]: ", i, j);
      scanf("%hu", &matrix[i][j]);
    }
  }
  print_matrix(matrix, rows, cols, "Entered matrix: ");

  clear_matrix_rows_and_cols(matrix, rows, cols);
  return 0;
}
