/*
 * Date: 25-Nov-2017
 *
 * Description:
 * Find 2D peak element in a matrix. An element is a 2D peak if it is not
 * smaller than its neighbours.
 *
 * Approach:
 * Find local maxima for a column and compare its right and left neigbhours, if
 * they are not larger then local maxima is the peak otherwise do same other
 * half of matrix. For corner cases just compare left or right.
 *
 * Complexity: O(nlogn)
 */

#include "stdio.h"
#include "stdlib.h"

#define MAX 100

/*
 * Inputs
 */
int row = 4, col = 4;
int a[][MAX] = {
        {10, 8, 10, 10},
        {14, 13, 12, 11},
        {15, 9, 11, 21},
        {16, 17, 19, 20}
};

/*
 * Find maximum element in a column.
 */
int find_max(int col, int *idx)
{
  int max = a[0][col];
  int i = 0;
  for (i = 1; i < row; i++)
  {
    if (max < a[i][col])
    {
      max = a[i][col];
      *idx = i;
    }
  }
  return max;
}

int main()
{
  int i = 0;
  int low = 0, high = col - 1;
  int mid = low + (high - low)/2;
  int row_idx = 0;
  int peak = a[0][0];
  int max_in_col;
  
  while (low <= high)
  {
    mid = low + (high - low)/2;

    // Find local maxima in a column. Here if we had found 1-D peak in a column
    // instead of maxima then also it may work but not in all cases.
    max_in_col = find_max(mid, &row_idx);
    
    if ((mid == 0 || max_in_col >= a[row_idx][mid - 1]) &&
        (mid == row - 1 || max_in_col >= a[row_idx][mid + 1]))
    {
      peak = max_in_col;
      break;
    }
    else if (mid != 0 && max_in_col <= a[row_idx][mid - 1])
    {
      high = mid - 1;
    }
    else
    {
      low = mid + 1;
    }
  }
  printf("2-D peak is: %d\n", peak);
  return 0;
}
