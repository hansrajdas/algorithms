/*
 * Date: 2018-09-23
 *
 * Description:
 * Given an array having positive and negative numbers, separate positive and
 * negative numbers. Update array such that first we have all positive numbers
 * then negatives, 0s should be with positive numbers.
 * Like if array is [-2, 0, -4, 9, -3, 4]
 * Output array should be: [0, 9, 4, -2, -3, -4] or in any other internal
 * ordering of positives and negatives but all positives/zeros and then
 * negatives.
 *
 * This problem is originally adapted from sorting an array having 0s and 1s in
 * single iteration.
 *
 * Approach:
 * Take 2 pointers one at starting of array and pointing to end, keep on
 * comparing if there is a negative number at starting pointer, if found stop
 * there and scan from end towards start to check if there is an positive number
 * once found stop and swap 2 numbers.
 *
 *
 * Complexity:
 * O(n)
 */

#include "stdio.h"
#include "stdlib.h"

void printArray(int arr[], int n, char *msg) {
  int i = 0;
  printf("*********** %s *****************\n", msg);
  for (i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n\n");
}

void separate_positives_and_negatives(int a[], int n) {
  int low = 0;
  int high = n - 1;
  int temp = 0;

  while (low < high) {
    while (low < high && a[low] >= 0)
      low += 1;

    while (low < high && a[high] < 0)
      high -= 1;

    if (low != high) {  // Swap
      temp = a[low];
      a[low] = a[high];
      a[high] = temp;
    }
  }
}

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element [%d]: ", i);
    scanf("%d",&a[i]);
  }
  printArray(a, n, "Inserted Array");

  separate_positives_and_negatives(a, n);

  printArray(a, n, "Positive and negative separated");
  return 0;
}


/*
 * Output:
 * -------------
 * Enter number of elements: 4
 * Enter element [0]: 2
 * Enter element [1]: 3
 * Enter element [2]: -2
 * Enter element [3]: 5
 * *********** Inserted Array *****************
 * 2 3 -2 5
 *
 * *********** Positive and negative separated *****************
 * 2 3 5 -2
 *
 * Enter number of elements: 7
 * Enter element [0]: -1
 * Enter element [1]: -2
 * Enter element [2]: -3
 * Enter element [3]: 4
 * Enter element [4]: 5
 * Enter element [5]: 7
 * Enter element [6]: -5
 * *********** Inserted Array *****************
 * -1 -2 -3 4 5 7 -5
 *
 * *********** Positive and negative separated *****************
 * 7 5 4 -3 -2 -1 -5
 *
 * Enter number of elements: 5
 * Enter element [0]: 3
 * Enter element [1]: -5
 * Enter element [2]: 0
 * Enter element [3]: -2
 * Enter element [4]: 5
 * *********** Inserted Array *****************
 * 3 -5 0 -2 5
 *
 * *********** Positive and negative separated *****************
 * 3 5 0 -2 -5
 */
