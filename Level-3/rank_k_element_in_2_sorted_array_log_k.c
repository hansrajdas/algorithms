/*
 * Date: 2018-06-11
 *
 * Description:
 * There are 2 sorted arrays in ascending order (having distinct elements). Task
 * is to find element having overall rank of k or kth smallest element.
 *
 * Approach:
 * Modified binary search is used. We can discard elements from array for which
 * element at index rank/2 is smaller than other array (Can now search in
 * A[0...m] and B[k/2....n] for rank k - k/2).
 *
 * Complexity:
 * O(log(k))
 */

#include "stdio.h"

int min(int a, int b) {
  return a < b ? a : b;
}

/*
 * Returns element with rank from 2 sorted arrays.
 * Args:
 *  A: First array
 *  B: Second array
 *  m: Length of first array
 *  n: Length of second array
 *  k: Rank
 */
int find_element_with_rank_k_log_k(int A[], int m, int B[], int n, int k) {
  int i = 0, j = 0;
  if (!m) return B[k - 1];
  if (!n) return A[k - 1];
  if (k == 1) return min(A[0], B[0]);

  i = min(m, k/2);
  j = min(n, k/2);
  // If A[k/2] > B[k/2], then we can discard B[0...k/2] elements as element with
  // rank k can't be in in B[0...k/2]. Taking this into consideration we now
  // has to find element with rank: k - k/2.
  if (A[i - 1] > B[j - 1])
    return find_element_with_rank_k_log_k(A, m, B + j, n - j, k - j);
  else
    return find_element_with_rank_k_log_k(A + i, m - i, B, n, k - i);
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

  printf("Element with rank %d is %d\n", rank,
    find_element_with_rank_k_log_k(A, a_len, B, b_len, rank));
  return 0;
}
