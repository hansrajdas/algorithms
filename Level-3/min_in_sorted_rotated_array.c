/*
 * Date: 2018-07-28
 *
 * Description:
 * Find minimum element from sorted rotated array like [5, 1, 2, 3, 4].
 *
 * Approach:
 * Minimum element will be present at pivot point .i.e. point where array is
 * rotated so check around mid if it is rotation point otherwise recurse over
 * array half which is not sorted .i.e. half which contains pivot point.
 *
 * Complexity: O(log(n))
 */

 #include "stdio.h"
 #include "stdlib.h"

/*
 * Finds and returns minimum element from sorted rotated array.
 *
 * Args:
 * A: Base address of array.
 * low: low index.
 * high: high index.
 *
 * Returns minimum element in array A.
 */
int minInSortedRotatedArray(int A[], int l, int r) {
  int m = l + (r - l)/2;

  // Handles case when array is not rotated or only element left in array.
  if (l >= r)
    return A[m];

  // Case: A = [3, 4, 5, 1, 2], m = 2, r = 4
  if (m < r && A[m + 1] < A[m])
    return A[m + 1];
  
  // Case: A = [4, 5, 1, 2, 3], m = 2, l = 0
  if (m > l && A[m - 1] > A[m])
    return A[m];

  // If right half is sorted, pivot will be on left half and min element will
  // also be pivot part only.
  if (A[m] < A[r])
    return minInSortedRotatedArray(A, l, m - 1);
  return minInSortedRotatedArray(A, m + 1, r);
}

int main() {
  int i = 0, n = 0;
  int *A = NULL;

  printf("Enter number of elements in rotated sorted array: ");
  scanf("%d", &n);

  A = (int *)malloc(n * (sizeof (int)));
  for (i = 0; i < n; i++) {
    printf("Enter element %d: ", i);
    scanf("%d", &A[i]);
  }
  printf("Minimum element is: %d\n", minInSortedRotatedArray(A, 0, n - 1));
  return 0;
 }

/*
Output:
*****************
hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ ./a.out 
Enter number of elements in rotated sorted array: 6
Enter element 0: 5
Enter element 1: 6
Enter element 2: 1
Enter element 3: 2
Enter element 4: 3
Enter element 5: 4
Minimum element is: 1
hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ ./a.out 
Enter number of elements in rotated sorted array: 4
Enter element 0: 1
Enter element 1: 2
Enter element 2: 3
Enter element 3: 4
Minimum element is: 1
hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ ./a.out 
Enter number of elements in rotated sorted array: 2
Enter element 0: 1
Enter element 1: 2
Minimum element is: 1
hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ ./a.out 
Enter number of elements in rotated sorted array: 2
Enter element 0: 2
Enter element 1: 1
Minimum element is: 1
hansraj@hansraj-Inspiron-3542:~/Desktop/Interviews/programs/algorithms$ ./a.out 
Enter number of elements in rotated sorted array: 5
Enter element 0: 3
Enter element 1: 4
Enter element 2: 5
Enter element 3: 1
Enter element 4: 2
Minimum element is: 1 
*/
