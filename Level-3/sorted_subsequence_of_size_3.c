/*
 * Date: 2018-09-28
 *
 * Description:
 * Given an array of n integers, find the 3 elements such that
 * a[i] < a[j] < a[k] and i < j < k. If there are multiple such triplets, then
 * print any one of them.
 *
 * Approach:
 * - Take 2 arrays, smaller and larger, initialise all values with -1.
 * - smaller[i] will hold the index of element smaller than A[i] and on left
 *   side of A[i]
 * - larger[i] will hold the index of element larger than A[i] and on right
 *   side of A[i]
 * - After smaller and larger are populated, run a loop and find if there exist
 *   a index when smaller[i] and larger[i] are not equal to -1, if yes, 3 sorted
 *   values will be: A[smaller[i]], A[i] and A[larger[i]]
 *
 * Complexity:
 * O(N) Time
 * O(N) Space
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int num_of_elements = 0;
  int *p_input = NULL, *p_small = NULL, *p_large = NULL;
  int small_idx = 0;
  int large_idx = 0;

  printf("Enter number of elements: ");
  scanf("%d", &num_of_elements);

  large_idx = num_of_elements - 1;

  p_input = (int *)malloc(sizeof(int) * num_of_elements);
  p_small = (int *)malloc(sizeof(int) * num_of_elements);
  p_large = (int *)malloc(sizeof(int) * num_of_elements);

  for (i = 0; i < num_of_elements; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &p_input[i]);
    p_small[i] = -1;
    p_large[i] = -1;
  }

  for (i = 1; i < num_of_elements; i++) {
    if (p_input[i] <= p_input[small_idx]) {
      small_idx = i;
      p_small[i] = -1;
    }
    else
      p_small[i] = small_idx;
  }

  for (i = num_of_elements - 2; i >= 0; i--) {
    if (p_input[i] >= p_input[large_idx]) {
      large_idx = i;
      p_large[i] = -1;
    }
    else
      p_large[i] = large_idx;
  }

  for (i = 0; i < num_of_elements; i++) {
    if ((p_small[i] != -1) && (p_large[i] != -1)) {
      printf("\n3 sorted elements are: %d %d %d\n",
        p_input[p_small[i]], p_input[i], p_input[p_large[i]]);
      break;
    }
  }
  return 0;
}


/*
 * Output:
 * ----------------
 * Enter number of elements: 5
 * Enter element[0]: 4
 * Enter element[1]: 7
 * Enter element[2]: 2
 * Enter element[3]: 9
 * Enter element[4]: 1
 * 
 * 3 sorted elements are: 4 7 9
 */ 
