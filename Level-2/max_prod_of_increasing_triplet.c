/*
 * Date: 2018-10-14
 *
 * Description:
 * Given an unsorted array, find increasing subsequence of length 3 having max
 * product that is max value of a[i]*a[j]*a[k] where i < j < k and
 * a[i] < a[j] < a[k].
 *
 * Approach:
 * - Consider elements with index i = 1 to n - 2 as middle and with respect to
 *   each middle element find max on left (but less than a[i]) and max on right
 *   of a[i]
 * - If such triplet is found, check if product of 3 numbers is more than
 *   existing max product
 *
 * Complexity:
 * O(N^2)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, j = 0;
  int n = 0;
  int *a = NULL;
  int curr_prod = -1, max_prod = -1;
  int less = -1, more = -1;
  int a1 = -1, a2 = -1, a3 = -1;

  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }

  // a[i] would be middle element so looping from 1 to n - 2
  for (i = 1; i < n - 1; i++) {
    less = -1;
    more = -1;
    // Find max element to left to a[i], but less than a[i]
    for (j = 0; j < i; j++) {
      if (less < a[j] && a[j] < a[i])
        less = a[j];
    }
    
    // Find max element to right of a[i] which is more than a[i]
    for (j = i + 1; j < n; j++) {
      if (more < a[j] && a[j] > a[i])
        more = a[j];
    }
    curr_prod = less * a[i] * more;

    // Update max_prod only if we have found a required triplet and more than
    // existing max_prod
    if (less != -1 && more != -1 && curr_prod > max_prod) {
      a1 = less;
      a2 = a[i];
      a3 = more;
      max_prod = curr_prod;
    }
  }
  printf("Required elements: %d %d %d\n", a1, a2, a3);
  printf("Product: %d\n", max_prod);
  return 0;
}


/*
 * Output:
 * -------------------
 * Enter number of elements: 3
 * Enter element[0]: 2
 * Enter element[1]: 2
 * Enter element[2]: 2
 * Required elements: -1 -1 -1
 * Product: -1
 *
 * Enter number of elements: 5
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Enter element[4]: 5
 * Required elements: 3 4 5
 * Product: 60
 *
 * Enter number of elements: 7
 * Enter element[0]: 3
 * Enter element[1]: 10
 * Enter element[2]: 2
 * Enter element[3]: 5
 * Enter element[4]: 1
 * Enter element[5]: 9
 * Enter element[6]: 4
 * Required elements: 3 5 9
 * Product: 135 
 */
