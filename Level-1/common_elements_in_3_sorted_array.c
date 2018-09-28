/*
 * Date: 2018-09-28
 *
 * Description:
 * Given 3 sorted arrays, print all common elements in them.
 *
 * Approach:
 * Scan all 3 arrays simultaneously, if elements are same print them otherwise
 * increase the counter for array who has minimum element at current index.
 *
 * Complexity:
 * O(n1 + n2 + n3)
 */

#include "stdio.h"

int main() {
  int i = 0, j = 0, k = 0;
  int num_of_elements = 0;
  int n1 = 4;
  int n2 = 5;
  int n3 = 5;
  int arr1[10] = {1, 2, 3, 4};
  int arr2[10] = {1, 3, 6, 7, 8};
  int arr3[10] = {1, 3, 6, 8, 10};
  while ((i < n1) && (j < n2) && (k < n3)) {
    if ((arr1[i] == arr2[j]) && (arr2[j] == arr3[k])) {
      printf("Common element: %d\n", arr1[i]);
      i++;
      j++;
      k++;
    }
    else if ((arr1[i] <= arr2[j]) && (arr1[i] <= arr3[k]))
      i++;
    else if ((arr2[j] <= arr1[i]) && (arr2[j] <= arr3[k]))
      j++;
    else
      k++;
  }
  return 0;
}


/*
 * Output:
 * ---------------
 * Common element: 1
 * Common element: 3
 */
