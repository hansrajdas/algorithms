/*
 * Date: 2018-07-29
 *
 * Description:
 * A magic index in an array A[0...n-1] is defined to be an index such that
 * A[i] = i. Given a sorted array of *distinct* integers, write a method to find
 * a magic index, if one exists in array A.
 * Like A = [-3, -1, 2, 5, 10], magic index = 2.
 *            0   1  2  3  4
 * Approach:
 * Search left half value at mid is larger than mid otherwise right half as
 * array is sorted and has distinct elements.
 *
 * Note:
 * This solution does not work if array has duplicates as we cannot be sure that
 * if value at mid is larger then magic index will be on left half. Like in
 * below example:
 * A = [-10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13], magic index = 2
 *        0   1  2  3  4  5  6  7  8  9   10
 *
 * Complexity:
 * O(log(n))
 */

#include "stdio.h"
#include "stdlib.h"

int findMagicIdx(int A[], int l, int r) {
  int m = l + (r - l)/2;
  
  if (A[m] == m) return m;
  if (l >= r) return -1;

  // If value is greater than index then magic index can be in left half
  // otherwise on right half.
  if (A[m] > m)
    return findMagicIdx(A, l, m - 1);
  return findMagicIdx(A, m + 1, r);
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
Enter number of elements: 3
Enter element [0]: -2
Enter element [1]: 1
Enter element [2]: 3
Magic index: 1
./a.out 
Enter number of elements: 4
Enter element [0]: -4
Enter element [1]: 1
Enter element [2]: 2
Enter element [3]: 3
Magic index: 1
./a.out 
Enter number of elements: 4
Enter element [0]: -4
Enter element [1]: -2
Enter element [2]: 1
Enter element [3]: 3
Magic index: 3
./a.out 
Enter number of elements: 4
Enter element [0]: 0
Enter element [1]: 2
Enter element [2]: 3
Enter element [3]: 5
Magic index: 0
./a.out 
Enter number of elements: 1
Enter element [0]: 1
Magic index does *NOT* exist in given array
./a.out 
Enter number of elements: 2
Enter element [0]: 2
Enter element [1]: 3
Magic index does *NOT* exist in given array
./a.out 
Enter number of elements: 2
Enter element [0]: -1
Enter element [1]: 1
Magic index: 1 
*/
