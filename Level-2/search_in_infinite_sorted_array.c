/*
 * Date: 2018-07-19
 *
 * Description:
 * Given an array-like data structure Listy which lacks a size method. It does,
 * however, have an e lementAt (i) method that returns the element at index i in
 * 0(1) time. If i is beyond the bounds of the data structure, it returns - 1.
 * (For this reason, the data structure only supports positive integers.) Given
 * a Listy which contains sorted, positive integers, find the index at which an
 * element x occurs. If x occurs multiple times, you may return any index.
 *
 * Approach:
 * Find range between which element can be found and perform binary search on
 * that range.
 *
 * Complexity:
 * O(log(p)), p is position where element was found.
 */

#include "stdio.h"
#include "stdlib.h"

#define MAX 1024

/*
 * Fetches element at index idx, if idx is more than max allowed idx it returns
 * -1.
 */
int get_item_at_idx(int A[], int idx) {
  if (idx >= MAX) return -1;
  return A[idx];
}

/*
 * Performs binary search on array A (with track of overflow in array, check of
 * -1). If element is found it returns index otherwise -1.
 */
int binary_search(int A[], int l, int r, int key) {
  int m = l + (r - l)/2;
  int item = get_item_at_idx(A, m);

  if (l > r || item == -1) return -1;
  if (item == key) return m;

  if (item < key)
    return binary_search(A, l, m - 1, key);
  else
    return binary_search(A, m + 1, r, key);
}

/*
 * Description:
 * Finds index of an element in infinite sorted array. If not found it returns
 * -1;
 *
 * Args:
 * A: Base address of array.
 * key: Key element to be searched.
 */
int search_in_infinite_sorted_array(int A[], int key) {
  int left = 0, right = 1;
  int item = get_item_at_idx(A, right);

  if (A[0] > key) return -1;

  while (item < key && item != -1) {
    left = right;
    right <<= 1;
    item = get_item_at_idx(A, right);
  }
  return binary_search(A, left, right, key);
}

int main() {
  int i = 0, n = 0, key = 0, idx = -1;
  int A[MAX];

  printf("Enter number of elements in infinite sorted array: ");
  scanf("%d", &n);

  for (i = 0; i < n; i++) {
    printf("Enter element %d: ", i);
    scanf("%d", &A[i]);
  }

  // Initialize with -1 to other indexes of array.
  for (;i < MAX; i++)
    A[i] = -1;

  printf("Enter element to be searched: ");
  scanf("%d", &key);

  // Calling function to find index of key.
  idx = search_in_infinite_sorted_array(A, key);
  if (idx == -1)
    printf("%d not found\n", key);
  else
    printf("%d is found at index: %d\n", key, idx);
  return 0;
}
