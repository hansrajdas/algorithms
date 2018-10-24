/*
 * Date: 2018-10-24
 *
 * Description:
 * Given an unsorted array, find the number of subarrays whose sum is even.
 *
 * Approach:
 * If we do compute the cumulative sum array in temp[] of our input array, then
 * we can see that the sub-array starting from i and ending at j, has an even
 * sum if temp[] if (temp[j] – temp[i]) % 2 = 0. So, instead of building a
 * cumulative sum array we build a cumulative sum modulo 2 array, and find how
 * many times 0 and 1 appears in temp[] array using handshake formula:
 * [n * (n-1) /2]
 *
 * Reference:
 * https://www.geeksforgeeks.org/find-number-subarrays-even-sum/
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  int result = 0, sum = 0;

  /*
   * A temporary array of size 2. temp[0] is going to store count of even
   * subarrays and temp[1] count of odd.
   * temp[0] is initialized as 1 because a single even element is also counted
   * as a subarray with even sum.
   */
  int temp[2] = {1, 0};

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  /*
   * i'th iteration computes sum of arr[0..i] under modulo 2 and increments
   * even/odd count according to sum's value.
   */
  for (i = 0; i < n; i++) {
    sum = ((sum + a[i]) % 2 + 2) %2;  // 2 is added to handle negative numbers
    temp[sum]++;
  }

  /*
   * Use handshake lemma to count even subarrays (Note that an even cam be
   * formed by two even or two odd)
   */
  result += temp[0]*(temp[0] - 1)/2;
  result += temp[1]*(temp[1] - 1)/2;

  printf("Result: %d\n",result);
  return 0;
}


/*
 * Output:
 * ---------------------
 * Enter number of elements: 3
 * Enter element[0]: 3
 * Enter element[1]: 2
 * Enter element[2]: 1
 * Result: 2
 *
 * Enter number of elements: 6
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 2
 * Enter element[3]: 3
 * Enter element[4]: 4
 * Enter element[5]: 1
 * Result: 9
 */
