/*
 * Date: 2018-07-17
 *
 * Description:
 * Given 2 sorted arrays, A and B, where A has a large enough buffer at the end
 * to hold B. Write a method to merge B into A in sorted order.
 *
 * Approach:
 * Start scanning from last elements and put larger ones at end of array A.
 * This way we don't have to shift all elements to right.
 *
 * Complexity:
 * O(A.length + B.length)
 */

#include "stdio.h"
#include "stdlib.h"

void print_array(int arr[], int n, char *msg)
{
  int i = 0;
  printf("*********** %s *****************\n", msg);
  for (i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n\n");
}

void merged_2_sorted_arrays_in_place(int A[], int a_len, int B[], int b_len) {
  int a_idx = a_len - 1;
  int b_idx = b_len - 1;
  int merged_idx = a_len + b_len - 1;

  while (b_idx >= 0) {
    if (a_idx >= 0 && A[a_idx] > B[b_idx])
      A[merged_idx--] = A[a_idx--];
    else
      A[merged_idx--] = B[b_idx--];
  }
}

int main() {
  int i = 0, j = 0;
  int a_len = 0, b_len = 0;
  int *A = NULL, *B = NULL;

  printf("Enter number of elements in array B: ");
  scanf("%d", &b_len);
  B = (int *)malloc(sizeof(int) * b_len);
  for (i = 0; i < b_len; i++) {
    printf("Enter element at index %d: ", i);
    scanf("%d", &B[i]);
  }

  printf("Enter number of elements in array A: ");
  scanf("%d", &a_len);
  A = (int *)malloc(sizeof(int) * (a_len + b_len));
  for (i = 0; i < a_len; i++) {
    printf("Enter element at index %d: ", i);
    scanf("%d", &A[i]);
  }
  merged_2_sorted_arrays_in_place(A, a_len, B, b_len);
  print_array(A, a_len + b_len, "Merged sorted array");
  return 0;
}

/*
Output:

hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ gcc -g merge_2_sorted_array_in_place.c ; ./a.out 
Enter number of elements in array B: 2
Enter element at index 0: 2
Enter element at index 1: 3
Enter number of elements in array A: 2
Enter element at index 0: 4
Enter element at index 1: 5
*********** Merged sorted array *****************
2 3 4 5 

hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ gcc -g merge_2_sorted_array_in_place.c ; ./a.out 
Enter number of elements in array B: 3
Enter element at index 0: 1
Enter element at index 1: 5
Enter element at index 2: 10
Enter number of elements in array A: 3
Enter element at index 0: 2
Enter element at index 1: 3
Enter element at index 2: 7
*********** Merged sorted array *****************
1 2 3 5 7 10 

hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ gcc -g merge_2_sorted_array_in_place.c ; ./a.out 
Enter number of elements in array B: 3
Enter element at index 0: 10
Enter element at index 1: 15
Enter element at index 2: 20
Enter number of elements in array A: 5
Enter element at index 0: 5
Enter element at index 1: 12
Enter element at index 2: 17
Enter element at index 3: 21
Enter element at index 4: 23
*********** Merged sorted array *****************
5 10 12 15 17 20 21 23 
*/
