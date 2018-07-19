/*
 * Date: 2018-06-12
 *
 * Description:
 * Search an element from rotated sorted array like [5, 1, 2, 3, 4].
 *
 * Approach:
 * Either left or right half of the array will surely be sorted so we can check
 * if element lies in sorted part or not otherwise search other half of array.
 *
 * Complexity: O(log(n))
 */

 #include "stdio.h"
 #include "stdlib.h"

/*
 * Description:
 * Finds index of element in rotated sorted array, if element not found, returns
 * -1.
 *
 * Args:
 * A: Base address of array.
 * low: low index.
 * high: high index.
 * key: Key element to be searched.
 */
int search_in_rotated_sorted_array(int A[], int low, int high, int key) {
  int mid = low + (high - low)/2;
  
  if (low > high) return -1;  // Element not found.
  if (key == A[mid]) return mid;  // Element found.

  // Check if A[low to mid] is sorted.
  if (A[low] <= A[mid]) {
    // Check if key lies between A[low to mid].
    if (key >= A[low] && key <= A[mid])
      return search_in_rotated_sorted_array(A, low, mid - 1, key);
    return search_in_rotated_sorted_array(A, mid + 1, high, key);
  }
  // If A[low to mid] is not sorted then A[mid to high] will surely be sorted.
  if (key >= A[mid] && key <= A[high])  // Check if key between A[mid to high].
    return search_in_rotated_sorted_array(A, mid + 1, high, key);
  return search_in_rotated_sorted_array(A, low, mid - 1, key);
}

int main() {
  int i = 0, n = 0, key = 0, idx = -1;
  int *A = NULL;

  printf("Enter number of elements in rotated sorted array: ");
  scanf("%d", &n);

  A = (int *)malloc(n * (sizeof (int)));
  for (i = 0; i < n; i++) {
    printf("Enter element %d: ", i);
    scanf("%d", &A[i]);
  }
  printf("Enter element to be searched: ");
  scanf("%d", &key);

  // Calling function to find index of key.
  idx = search_in_rotated_sorted_array(A, 0, n - 1, key);
  if (idx == -1)
    printf("%d not found\n", key);
  else
    printf("%d is found at index: %d\n", key, idx);
  return 0;
 }
