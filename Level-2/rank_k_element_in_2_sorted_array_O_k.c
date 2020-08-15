/*
 * Date: 2018-06-09
 *
 * Description:
 * There are 2 sorted arrays in ascending order (having distinct elements). Task
 * is to find element having overall rank of k or kth smallest element.
 *
 * Approach:
 * Scan linearly both arrays and stop overall traversal is done for k elements.
 * If any of the array ends, scan the other array till k.
 *
 * Complexity:
 * O(k)
 */

#include "stdio.h"

void find_element_with_rank_k(int A[], int m, int B[], int n, int rank) {
  int i = 0, j = 0, k = 0;
  while (k < rank && i < m && j < n) {
    if (k == rank - 1) {
      printf("Element with rank %d is %d\n", rank, (A[i] < B[j] ? A[i]: B[j]));
      break;
    } else {
      if (A[i] < B[j])
        i++;
      else
        j++;
      k++;
    }
  }

  // If one of the array ends and element is not found
  if (i == m) {  // If array A ends, look in array B
    for (;j < n; j++) {
      if (k == rank - 1) {
        printf("Element with rank %d is %d\n", rank, B[j]);
        break;
      }
    }
  } else if (j == n) {
    for (;i < m; i++) {
      if (k == rank - 1) {
        printf("Element with rank %d is %d\n", rank, A[i]);
        break;
      k++;
      }
    }
  }
}

int main() {
  int i = 0, j = 0, k = 0;
  int rank = 0, a_len = 0, b_len = 0;
  int A[50] = {0}, B[50] = {0};

  printf("Enter number of elements in first array: ");
  scanf("%d", &a_len);
  for (i = 0; i < a_len; i++) {
    printf("Enter element at index %d: ", i);
    scanf("%d", &A[i]);
  }

  printf("Enter number of elements in second array: ");
  scanf("%d", &b_len);
  for (i = 0; i < b_len; i++) {
    printf("Enter element at index %d: ", i);
    scanf("%d", &B[i]);
  }

  printf("Enter rank: ");
  scanf("%d", &rank);

  if (rank < 1 || rank > a_len + b_len) {
    printf("Invalid rank, should be between 1 and %d\n", a_len + b_len);
    return -1;
  }

  find_element_with_rank_k(A, a_len, B, b_len, rank);
  return 0;
}
