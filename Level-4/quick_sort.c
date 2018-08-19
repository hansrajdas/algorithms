/*
 * Date: 2017-xx-xx
 *
 * Description:
 * Implement quick sort.
 *
 * Implementation:
 * Uses divide and conquer approach. It divides the array in 2 parts lower part
 * has all elements lesser than all elements at higher part. Partitioning is
 * done across an element called pivot. So after each iteration selected pivot
 * gets placed at correct position in array.
 * In below program last element of sub array is taken as pivot and that is
 * placed at correct place after each call to partition function.
 *
 * Complexity:
 * O(nlogn) time, Best and average case
 * O(n^2) time, Worst case, when array is already sorted in asc or dsc order
 * O(1) space
 */

#include "stdio.h"
#include "stdlib.h"

void swap(int *a, int *b) {
  int t;
  t = *a;
  *a = *b;
  *b = t;
}

/*
 * Partitions the array in 2 parts and places the pivot at correct place in
 * array. Last element is taken as pivot in every call to this function and it
 * is placed at correct position in array.
 *
 * This function has a complexity of O(n).
 *
 * Args:
 * a: Array
 * low: Start index of array
 * high: Last index of array
 *
 * Returns: Partitioning index of array.
 */
int partition(int a[], int low, int high) {
  int i = low;  // Holds counter for smaller values than pivot.
  int j = 0;  // For iterating over array.
  int pivot = a[high];

  for (j = low; j < high; j++) {
    if (a[j] <= pivot) {
      swap(&a[i], &a[j]);
      i++;
    }
  }
  swap(&a[i], &a[high]);
  return i;
}

/*
 * This function does the divide and conquer part. Calls itself recursively with
 * each and every partition of the array.
 *
 * This is the function which governs the complexity of quick sort. For random
 * array this takes O(logn) as array is divided by 2 in each call to this
 * function via pivot from partition function.
 *
 * If input array is sorted (increasing or decreasing) array is not evenly
 * divided, it gets divided with 1 element on left and n - 1 on right side so
 * becomes skewed kind of tree which takes complexity of O(n) instead of
 * O(logn).
 *
 * Args:
 * a: Array
 * low: Start index of array
 * high: End index of array
 */
void quickSort(int a[], int low, int high) {
  int pivot = 0;
  if (low < high) {
    pivot = partition(a, low, high);
    quickSort(a, low, pivot - 1);
    quickSort(a, pivot + 1, high);
  }
}

int main() {
  int i = 0, n = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element [%d]: ", i);
    scanf("%d", &a[i]);
  }
  quickSort(a, 0, n - 1);

  printf("Sorted array elements:\n");
  for (i = 0; i < n; i++)
    printf("a[%d] : %d\n", i, a[i]);
  return 0;
}
