/*
 * Date: 2018-11-07
 *
 * Description:
 * Given an array of size n and a number k. We must modify array K number of
 * times. Here modify array means in each operation we can replace any array
 * element arr[i] by -arr[i].
 *
 * Approach:
 * We need to find min element k times and negate and save it in array again.
 *
 * Complexity:
 * O(K*N)
 *
 * Note:
 * This can be solved in better complexity, using min heap. First we can create
 * a min heap with elements then fetch min k times negate it and insert in to
 * heap again. This would take O(n + k*log(n))
 * https://www.geeksforgeeks.org/maximize-array-sum-k-negations-set-2/
 */

#include "stdio.h"
#include "stdlib.h"

#define INT_MAX 1 << 30

int main() {
  int i = 0, j = 0, idx = 0;
  int n = 0, k = 0, sum = 0;
  int *a = NULL;
  int min = 65535;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }
  printf("\nEnter value of k: ");
  scanf("%d", &k);

  for (i = 0; i < k; i++) {
    for (j = 0; j < n; j++) {
      if (min > a[j]) {
        min = a[j];
        idx = j;
      }
    }
    if (!min)
      break;
    else {
      a[idx] = -1*a[idx];
      min = INT_MAX;
    }
  }

  // Find sum after negating k elements
  for (j = 0; j < n; j++)
    sum += a[j];

  printf("Max sum after k negations: %d\n", sum);
  return 0;
}


/*
 * Output:
 * -------------------------
 * Enter number of elements: 3
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * 
 * Enter value of k: 2
 * Max sum after k negations: 6
 *
 * Enter number of elements: 5
 * Enter element[0]: -2
 * Enter element[1]: -1
 * Enter element[2]: 2
 * Enter element[3]: 3
 * Enter element[4]: -10
 * 
 * Enter value of k: 2
 * Max sum after k negations: 16 
 */
