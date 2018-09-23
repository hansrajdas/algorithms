/*
 * Date: 2018-06-14
 *
 * Description:
 * Transform an array to min heap and sort in descending order. Min heap has
 * smallest element at 0th index always. In sorting we can copy 0th index
 * element to last index and run min-heapify again to have next min at 0th
 * index.
 * So min heap is used to sort array in descending order and max heap can be
 * used to sort array in ascending order.
 *
 * Complexity:
 * Building heap has O(n)
 * Sorting takes O(n*log(n))
 */

#include "stdio.h"
#include "stdlib.h"

void print_array(int arr[], int n, char *msg) {
  int i = 0;
  printf("\n************ %s ****************\n", msg);
  for (i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n");
}

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

void min_heapify(int a[], int n, int i) {
  int lowest_idx = i;
  int left = 2*i + 1;
  int right = 2*i + 2;

  // Check if current element is smallest among 3 elements(self, left and
  // right child) or not.
  if (left < n && a[lowest_idx] > a[left])
    lowest_idx = left;
  if (right < n && a[lowest_idx] > a[right])
    lowest_idx = right;

  // If current index element is not smallest than it's left and right child
  // then swap current index element with smaller element.
  if (lowest_idx != i) {
    swap(&a[i], &a[lowest_idx]);
    min_heapify(a, n, lowest_idx);
  }
}

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  printf("Enter number of elements : ");
  scanf("%d",&n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element [%d] : ", i);
    scanf("%d",&a[i]);
  }
  print_array(a, n, "Input array");

  // Building min heap. Building min heap has total complexity of O(n).
  // Refer: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
  // This loop is run from n/2 down to 0 with an assumption that lower level
  // elements (from n/2+1 to n) in heap is already heapfied.
  for (i = n/2; i >= 0; i--)
    min_heapify(a, n, i);
  print_array(a, n, "Min-heap");

  // Sort in descending order.
  for (i = n - 1; i >=0; i--) {
    swap(&a[0], &a[i]);
    min_heapify(a, i, 0);
  }
  print_array(a, n, "Sorted array(descending order)");
  return 0;
}
