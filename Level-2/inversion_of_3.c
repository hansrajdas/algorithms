/*
 * Date: 2018-09-27
 *
 * Description:
 * Find number of combinations which follows: a[i] > a[j] > a[k] with i < j < k.
 *
 * Approach:
 * Run a loop from second element to end, for each element of this loop run 2
 * inner loops:
 * - First one to count number of elements greater than current element but
 *   index less than index of current element, call it greater
 * - Second one to count number of elements smaller than current element but
 *   index greater than index of current element, call it smaller
 *
 * Product of smaller and greater will give the number of combinations possible
 * with above pattern.
 *
 * Complexity:
 * O(N^2)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int num_ele = 0;
  int *p_input = NULL;
  int inv_3 = 0, smaller = 0, greater = 0, j = 0;

  printf("Enter number of elements: ");
  scanf("%d", &num_ele);
  p_input = (int *)malloc(num_ele * sizeof(int));
  for (i = 0; i < num_ele; i++) {
    printf("Enter element %d: ", i);
    scanf("%d", &p_input[i]);
  }

  // These elements would be center or current element
  for (i = 1; i < num_ele; i++) {
    greater = 0;
    smaller = 0;

    // These would be elements greater than center so running from current
    // position i to 0
    for (j = i - 1; j >= 0; j--) {
      if (p_input[j] > p_input[i])
        greater++;
    }

    // These would be all elements smaller than center so running from current
    // to end.
    for (j = i + 1; j < num_ele; j++) {
      if (p_input[j] < p_input[i])
        smaller++;
    }
    inv_3 += greater*smaller;
  }

  printf("Combinations - %d\n",inv_3);
  free (p_input);
}
