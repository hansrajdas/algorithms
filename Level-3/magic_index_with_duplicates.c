/*
 * Date: 2018-07-29
 *
 * Description:
 * A magic index in an array A[0...n-1] is defined to be an index such that
 * A[i] = i. Given a sorted array of integers which may have *duplicates*, write
 * a method to find a magic index, if one exists in array A.
 * Like A = [-10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13], magic index = 2
 *             0   1  2  3  4  5  6  7  8  9   10
 * Approach:
 * Search both left and right sub array if not found at mid.
 *
 * Complexity:
 * Average case: O(log(n))
 * Worst case: O(n)
 */

#include "stdio.h"
#include "stdlib.h"

int min(int A, int B) {
  return A < B ? A : B;
}

int max(int A, int B) {
  return A > B ? A : B;
}

int findMagicIdx(int A[], int start, int end) {
  int mid = start + (end - start)/2;
  int leftIdx = -1, rightIdx = -1, left = -1, right = -1;
  
  if (A[mid] == mid) return mid;
  if (start >= end) return -1;

  // Search left but only selective part .i.e. from start to min of value at mid
  // index. This is the example where this condition helps:
  // A = [-10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13]
  //        0   1  2  3  4  5  6  7  8  9   10
  // If mid = 5, A[mid] = 3 so we will search for 0 to 3 in left half as index
  // and value cannot match at index 4 as 3(value) < 4(index).
  leftIdx = min(mid - 1, A[mid]);
  left = findMagicIdx(A, start, leftIdx);
  if (left >= 0) return left;
  
  // Search right.
  rightIdx = max(mid + 1, A[mid]);
  right = findMagicIdx(A, rightIdx, end);
  if (right >= 0) return right;
}

int main()
{
  int i = 0, magicIdx = -1;
  int n = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d",&n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++)
  {
    printf("Enter element [%d]: ", i);
    scanf("%d",&a[i]);
  }
  magicIdx = findMagicIdx(a, 0, n - 1);
  if (magicIdx == -1) {
    printf("Magic index does *NOT* exist in given array\n");
  } else {
    printf("Magic index: %d\n", magicIdx);
  }
  return 0;
}

/*
Output:
**************************
./a.out 
Enter number of elements: 1
Enter element [0]: 1
Magic index does *NOT* exist in given array
./a.out 
Enter number of elements: 1
Enter element [0]: 0
Magic index: 0
./a.out 
Enter number of elements: 11
Enter element [0]: -10
Enter element [1]: -5
Enter element [2]: 2
Enter element [3]: 2
Enter element [4]: 2
Enter element [5]: 3
Enter element [6]: 4
Enter element [7]: 8
Enter element [8]: 9
Enter element [9]: 12
Enter element [10]: 13
Magic index: 2
*/
