/*
 * Date: 2018-10-06
 *
 * Description:
 * Given an unsorted array, find the number of merge operations(merging adjacent
 * elements) required to make array as palindrome.
 * Like if array is: [3, 2, 1], count - 1, we can merge 2 + 1 to make array
 * palindrome [3, 3].
 *
 * Approach:
 * All arrays can be made palindrome(at least of size 1) so scan from both ends
 * and merge adjacent elements whichever side element is smaller and move that
 * side pointer closer to center.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0;
  int *A = NULL;
  int count = 0;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  i = 0;  // Left pointer
  j = n - 1;  // Right pointer
  while (i < j) {
    if (A[i] == A[j]) {
      i++;
      j--;
    }
    else if (A[i] > A[j]) {
      count++;
      A[j - 1] = A[j] + A[j - 1];
      j--;

    }
    else {
      count++;
      A[i + 1] = A[i] + A[i + 1];
      i++;
    }
  }
  printf("Merge operations required to make array palindrome: %d\n", count);
  return 0;
}


/*
 * Output:
 * -----------------------------
 * Enter number of elements: 5
 * Enter element[0]: 4
 * Enter element[1]: 2
 * Enter element[2]: 4
 * Enter element[3]: 5
 * Enter element[4]: 1
 * Merge operations required to make array palindrome: 2
 */ 
