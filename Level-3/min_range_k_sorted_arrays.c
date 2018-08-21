/*
 * Date: 2018-08-20
 *
 * Description:
 * There are k sorted arrays and we need to find the minimum range of number
 * which will have at least one element from each array. Solve for k = 3.
 * Example:
 * array-1: [4, 10, 15, 24]
 * array-2: [0, 9, 12, 20]
 * array-3: [5, 18, 22, 30]
 *
 * Minimum range would be 20 to 24 i.e 4 as range 20 to 24 contains elements
 * from all arrays. Array-1 has 24, array-2 has 20 and array-3 has 22.
 *
 * Approach:
 * Take 3 pointers starting from first element of each array, compute range
 * and save. Now increment pointer pointing to minimum element and compute range
 * again if range is less than previously saved than update range otherwise move
 * further in same fashion.
 *
 * Complexity:
 * O(n*k) time, O(1) space
 * Can be improved to O(n*log(k)) by using min heap to keep track of minimum
 * element.
 */

#include "stdio.h"

int min(int A, int B, int C) {
  if (A < B)
    return A < C ? A : C;
  else
    return B < C ? B : C;
}

int max(int A, int B, int C) {
  if (A > B)
    return A > C ? A : C;
  else
    return B > C ? B : C;
}

void minRangeKsortedArrays(int a1[], int a2[], int a3[],
                           int n1, int n2, int n3) {
  int i = 0, j = 0, k = 0;
  int rangeStart = 0, rangeEnd = 0, range = 0;
  int minRangeStart = 0, minRangeEnd = 0, minRange = 1 << 30;  // INT_MAX

  while (i < n1 && j < n2 && k < n3) {
    rangeStart = min(a1[i], a2[j], a3[k]);
    rangeEnd = max(a1[i], a2[j], a3[k]);
    range = rangeEnd - rangeStart;

    // Update min range, start and end if new min is found.
    if (range < minRange) {
      minRange = range;
      minRangeStart = rangeStart;
      minRangeEnd = rangeEnd;
    }

    // Increment pointer which points to min element among 3.
    if (rangeStart == a1[i])
      i++;
    else if (rangeStart == a2[j])
      j++;
    else
      k++;
  }
  printf("Start: %d, End: %d, Min range: %d\n",
         minRangeStart, minRangeEnd, minRange);
}

int main() {
  int i = 0;
  int n1 = 4, n2 = 4, n3 = 4;
  int a1[4] = {4, 10, 15, 24};
  int a2[4] = {0, 9, 12, 20};
  int a3[4] = {5, 18, 22, 30};

  minRangeKsortedArrays(a1, a2, a3, n1, n2, n3);
  return 0;
}
