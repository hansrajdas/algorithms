/*
 * Date: 2018-10-20
 *
 * Description:
 * Given an array arr[0 … n-1] containing integers, a subsequence of arr[] is
 * called Bitonic if it is first increasing, then decreasing.
 * Write a function that takes an array as argument and returns the length of
 * the longest bitonic subsequence.
 * A sequence, sorted in increasing order is considered Bitonic with the
 * decreasing part as empty. Similarly, decreasing order sequence is considered
 * Bitonic with the increasing part as empty.
 *
 * Examples:
 * Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
 * Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)
 *
 * Approach:
 * Take 2 auxiliary arrays inc[] and dec[], such that inc[i] and dec[i] keeps
 * track of number of elements in increasing order from 0 to a[i] and decreasing
 * from a[i] to a[n-1] respectively.
 * Max bitonic length would be max of inc[i] + dec[i] - 1.
 * -1 is done as a[i] would be part of both inc[i] and dec[i]
 *
 * Complexity:
 * Time - O(N)
 * Space - O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  int *inc = NULL, *dec = NULL;
  int max = 1;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  inc = (int *)malloc(sizeof(int)*n);
  dec = (int *)malloc(sizeof(int)*n);

  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
    inc[i] = 1;
    dec[i] = 1;
  }

  for (i = 1; i < n; i++) {
    inc[i] = a[i] > a[i - 1] ? inc[i - 1] + 1 : 1;
    printf("%d ", inc[i]);
  }

  printf ("\n");
  for (i = n - 2; i >= 0; i--) {
    dec[i] = a[i] > a[i + 1] ? dec[i + 1] + 1 : 1;
    printf("%d ", dec[i]);
  }

  for (i = 0; i < n; i++) {
    if (max < inc[i] + dec[i])
      max = inc[i] + dec[i];
  }
  printf("\nMax biotic length is: %d\n", max - 1);
  return 0;
}


/*
 * Output:
 * ---------------------
 * Enter number of elements: 5
 * Enter element[0]: 2
 * Enter element[1]: 3
 * Enter element[2]: 4
 * Enter element[3]: 1
 * Enter element[4]: 0
 * 2 3 1 1 
 * 2 3 1 1 
 * Max biotic length is: 5 
 *
 * Enter number of elements: 9
 * Enter element[0]: 2
 * Enter element[1]: 3
 * Enter element[2]: 5
 * Enter element[3]: 1
 * Enter element[4]: 0
 * Enter element[5]: 9
 * Enter element[6]: 4
 * Enter element[7]: 5
 * Enter element[8]: 7
 * 2 3 1 1 2 1 2 3 
 * 1 1 2 1 2 3 1 1 
 * Max biotic length is: 5 
 */
