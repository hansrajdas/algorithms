/*
 * Date: 2018-10-06
 *
 * Description:
 * Given an unsorted array, find the number of distinct pairs possible.
 *
 * Approach:
 * Used a temp array to store elements already found in original array. Also
 * used 2 pointers left and right, always maintained unique elements between
 * left and right pointers, so that count is updated as right - left.
 *
 * Limitation:
 * Will not work if range of elements is more than number of element as temp
 * array is taken of size N.
 *
 * Complexity:
 * O(N) Time and space
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0, num_of_pairs = 0;
  int *A = NULL, *p_tmp = NULL;
  int left = 0, right = 0;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);
  p_tmp = (int *)malloc(sizeof(int) * n);

  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
    p_tmp[i] = 0;
  }

  while (right < n) {
    while ((right < n) && (!p_tmp[A[right]])) {
      num_of_pairs += (right - left);
      p_tmp[A[right]] = 1;
      right++;
    }
    // Move left pointer ahead as many times as there are repeated elements.
    while (p_tmp[A[left]]) {
      p_tmp[A[left]] = 0;
      left++;
    }
  }
  printf("Number of pairs: %d\n", num_of_pairs);
  return 0;
}

/*
 * Output:
 * -----------------------
 * Enter number of elements: 2
 * Enter element[0]: 1
 * Enter element[1]: 1
 * Number of pairs: 0
 *
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 1
 * Number of pairs: 1
 *
 * Enter number of elements: 4
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 1
 * Number of pairs: 3
 *
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Number of pairs: 3
 */
