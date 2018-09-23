/*
 * Date: 2017-11-03
 *
 * Description:
 * Transform an array to max heap and sort in ascending order. Max heap has
 * largest element at 0th index always. In sorting we can copy 0th index element
 * to last and run max-heapify again to have next max at 0th index.
 * So max heap is used to sort array in ascending order and min heap can be used
 * to sort array in descending order.
 *
 * Complexity:
 * Building heap has O(n)
 * Sorting takes O(n*log(n))
 */

#include "stdio.h"
#include "stdlib.h"

void print_array(int arr[], int n) {
  int i = 0;
  printf("****************************\n");
  for (i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n****************************\n");
}

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

// This function has a complexity of O(logn).
void max_heapify(int arr[], int n, int i) {
  // In array[0 to n] as max heap any node at index i has it's left element at
  // index 2*i + 1 and right at 2*i + 2.
  int largest_idx = i;
  int left_idx = 2*i + 1;
  int right_idx = 2*i + 2;

  // Check if current element is larger than it's left and right child.
  // If not take index of largest element between left and right child as
  // largest index. Also larger among left and right child should become parent
  // of current node so 2 if used instead of if..else if.
  if (left_idx < n && arr[largest_idx] < arr[left_idx])
    largest_idx = left_idx;
  if (right_idx < n && arr[largest_idx] < arr[right_idx])
    largest_idx = right_idx;

  if (largest_idx != i) {
    swap(&arr[i], &arr[largest_idx]);
    max_heapify(arr, n, largest_idx);
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
  print_array(a, n);

  // Build heap from an array, loop is ran from n/2 to 0 as elements from
  // n/2 + 1 to n are leaf nodes and assumed to already heapified.
  // Building heap has a complexity of O(n) although hepify has O(logn)
  // complexity and it loops from n/2 to 0.
  for (i = n/2; i >= 0; i--) {
    max_heapify(a, n, i);
  }
  print_array(a, n);

  
  // Extract nodes from max heap, in each iteration keep largest element at
  // last index of array and decrease heap size.
  for (i = n - 1; i >= 0; i--) {
    swap(&a[0], &a[i]);
    max_heapify(a, i, 0);
  }
  print_array(a, n);
  return 0;
}
