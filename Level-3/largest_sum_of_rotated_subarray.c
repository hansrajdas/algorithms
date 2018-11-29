/*
 * Date: 2018-10-06
 *
 * Description:
 * Consider a unsorted rotated array(having +ve and -ve numbers), find the max
 * sum possible for a subarray if array was not rotated.
 * Example:
 * A = [2, -1, 2, -5, 7], max sum will be 10 considering elements [7, 2, -1, 2]
 *
 * Approach:
 * 1. Find max sum of a subarray using kadane algo, call it max1.
 * 2. Find total sum of array.
 * 3. Negate all array elements and again run kadane for max sum of subarray,
 *    call it max 2.
 * 4. Max sum would be maxOf(max1, max2 + total_sum)
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int kadane(int a[], int n) {
  int i = 0, max = 0, max_so_far = 0;

  for (i = 0; i < n; i++) {
    max_so_far += a[i];
    if (0 > max_so_far)
      max_so_far = 0;
    if (max < max_so_far)
      max = max_so_far;
  }
  return max;
}

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  int total_sum = 0, max_circular_sum = 0;
  int max1 = 0, max2 = 0;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);

  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  max1 = kadane(a, n);
  for (i = 0; i < n; i++) {
    total_sum += a[i];
    a[i] = -a[i];
  }
  max2 = kadane(a, n);
  max_circular_sum = (max1 > (max2 + total_sum)) ? max1 : (max2 + total_sum);
  printf("Max circular sum: %d\n", max_circular_sum);
  return 0;
}

/*
 * Output:
 * -----------------------------
 * Enter number of elements: 5
 * Enter element[0]: 2
 * Enter element[1]: -1
 * Enter element[2]: 2
 * Enter element[3]: -5
 * Enter element[4]: 7
 * Max circular sum: 10
 */
