/*
 * Date: 2018-06-30
 *
 * Description:
 * Find length of longest increasing subsequence from an unsorted array.
 * LIS in array: [3, 4, 1, 2, 5] is 3, [3, 4, 5].
 *
 * Approach:
 * This is solved using bottom up approach, a temporary array p_lis is used to
 * store LIS till array element p_list[i], which is updated based on previous
 * values in array that is 0 to i - 1, in every iteration.
 *
 * Complexity:
 * Time - O(N^2), Space: O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0, max = 0;
  int num_of_elements = 0;
  int *p_input = NULL, *p_lis = NULL;

  printf("Enter number of elements: ");
  scanf("%d", &num_of_elements);
  
  p_input = (int *)malloc(sizeof(int) * num_of_elements);
  p_lis = (int *)malloc(sizeof(int) * num_of_elements);
  
  for (i = 0; i < num_of_elements; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &p_input[i]);
    p_lis[i] = 1;
  }

  // Solve problem using bottom up manner.
  // p_lis[i] holds LIS ending at index i such that p_input[i] is the last
  // element of the LIS.
  for (i = 1; i < num_of_elements; i++) {
    for (j = 0; j < i; j++) {
      // Second part of if condition is important as it saves us from
      // eliminating smaller number which are not part of LIS like:
      // [10, 22, 9, 33] as last element 33 is greater than all elements it will
      // give LIS as 4 (with second part of if condition) which is wrong.
      // Correct LIS is 3
      if ((p_input[i] > p_input[j]) && (p_lis[i] < p_lis[j] + 1))
        p_lis[i] = p_lis[j] + 1;
    }
  }

  max = p_lis[0];
  for (i = 1; i < num_of_elements; i++) {
    if (max < p_lis[i])
      max = p_lis[i];
  }
  printf("LIS - %d\n",max);
  free(p_input);
  free(p_lis);
  return 0;
}
