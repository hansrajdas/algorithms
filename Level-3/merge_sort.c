/*
 * Date: 2018-09-09
 *
 * Description:
 * Implement merge sort.
 *
 * Approach:
 * Partitions array in equal half and merges them back again in sorted order.
 * This is done recursively until all array elements are sorted.
 *
 * Complexity:
 * O(nlogn)
 */

#include "stdio.h"
#include "stdlib.h"

void merge(int a[], int l, int m, int r) {
  int i = 0, j = 0, k = l;
  int n1 = m - l + 1;
  int n2 = r - m;
  int *L = (int *)malloc(sizeof(int)*n1);
  int *R = (int *)malloc(sizeof(int)*n2);

  for (i = 0; i < n1; i++)
    L[i] = a[l + i];

  for (j = 0; j < n2; j++)
    R[j] = a[m + 1 + j];

  i = 0;
  j = 0;
  k = l;
  while ((i < n1) && (j < n2)) {
    if (L[i] < R[j]) {
      a[k] = L[i];
      i++;
    }
    else {
      a[k] = R[j];
      j++;
    }
    k++;
  }
  while (i < n1) {
    a[k] = L[i];
    k++;
    i++;
  }
  while (j < n2) {
    a[k] = R[j];
    k++;
    j++;
  }
  free(L);
  free(R);
}

/*
 * If number of elements in array is 2 like [2, 1] this function does not sort
 * these 2 elements, we can handle this special case separately.
 */
void mergeSort(int a[], int l, int r) {
  int m = 0;
  if (l < r) {
    m = l + (r - l)/2;
    mergeSort(a, l, m);
    mergeSort(a, m + 1, r);
    merge(a, l, m, r);
  }
}

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d",&n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element [%d]: ", i);
    scanf("%d",&a[i]);
  }

  mergeSort(a, 0, n - 1);
  printf("Sorted array elements: \n");
  for (i = 0; i < n; i++)
    printf("a[%d]: %d\n", i, a[i]);
  return 0;
}
