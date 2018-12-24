/*
 * Date: 2018-09-23
 *
 * Description:
 * Find pairs in array having given sum.
 *
 * Approach:
 * Use a hashmap to keep track of what all numbers are already traversed.
 *
 * Complexity:
 * O(n) time and space
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int num_of_elements = 0;
  int *p_input = NULL;
  int *p_tmp = NULL;
  int required_sum = 0;

  printf("Enter number of elements: ");
  scanf("%d", &num_of_elements);
  p_input = (int *)malloc(sizeof(int) * num_of_elements);
  p_tmp = (int *)malloc(sizeof(int) * num_of_elements);

  for (i = 0; i < num_of_elements; i++) {
    scanf("%d", &p_input[i]);
    p_tmp[i] = 0;
  }
  printf("Enter required sum: ");
  scanf("%d", &required_sum);
  for (i = 0; i < num_of_elements; i++) {
    if (p_tmp[required_sum - p_input[i]] == 1) {
      printf("SUM[%d] -  NUM1[%d], NUM2[%d]\n",
        required_sum, p_input[i], (required_sum - p_input[i]));
    }
    else
    {
      p_tmp[p_input[i]] = 1;
    }
  }
  return 0;
}


/* Output:
 * ------------------------
 * [1,2,3,4,2,3], sum  = 4
 * [0,1,1,0,0,0]
 */
