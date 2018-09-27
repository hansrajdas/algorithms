/*
 * Date: 2018-09-27
 *
 * Description:
 * Find majority element from an array, majority element in array is one that
 * occurs more than n/2 times. It is guaranteed that array will surely have one
 * such element which occurs more than n/2 times.
 *
 * Approach:
 * - Assume first element as max occurring element, taking count = 1
 * - Scan further in array, if same element appears, increment count by 1
 *   otherwise decrement count by 1
 * - If count becomes 0, consider new element as max occurring element and
 *   reset count to 1
 *
 * This cancellation algorithm is called Moore's voting algorithm.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

int find_max_occuring_num (int arr[], int n) {
  int i = 0;
  int count = 1;
  int maj_idx = 0;

  for (i = 1; i < n; i++) {
    if (arr[maj_idx] == arr[i])
      count++;
    else
      count--;

    if (!count) {
      maj_idx = i;
      count = 1;
    }
  }
  return arr[maj_idx];
}

int main() {
  int i = 0;
  int n = 0, num_max_times = 0, ctr = 0;
  int *a = NULL;
  
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  num_max_times = find_max_occuring_num(a, n);
  printf("Number occurring maximum times is: %d\n", num_max_times);
  return 0;
}


/*
 * Output:
 * -----------------
 * Enter number of elements: 10
 * Enter element[0]: 4
 * Enter element[1]: 4
 * Enter element[2]: 2
 * Enter element[3]: 3
 * Enter element[4]: 6
 * Enter element[5]: 6
 * Enter element[6]: 4
 * Enter element[7]: 4
 * Enter element[8]: 4
 * Enter element[9]: 15
 * Number occurring maximum times is: 4
 */
