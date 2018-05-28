/*
 * Date: 25-Nov-2017
 *
 * Description:
 * Find a peak element from an array. Peak is any element in array which is not
 * smaller than it's neighbours. For last element only one adjacent is compared.
 * Eg:
 * [1, 2, 3, 4, 5], 5 is peak
 * [4, 6, 2, 1], 6 is peak
 *
 * 
 * Approach:
 * Binary search approach is followed, compared mid element with its neigbhours
 * if smaller check same with other half of array.
 *
 * Complexity: O(logn)
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

int find_peak(int a[], int n)
{
  int low = 0, high = n - 1;
  int mid = n/2;
  int peak = a[mid];

  while (low <= high)
  {
    mid = low + (high - low)/2;
    if ((mid == 0 || a[mid] >= a[mid - 1]) && 
        (mid == n - 1 || a[mid] >= a[mid + 1]))
    {
      peak = a[mid];
      break;
    }
    else if (mid != n - 1 && a[mid] < a[mid + 1])
    {
      low = mid + 1;
    }
    else
    {
      high = mid - 1;
    }
  }
  return peak;
}

int main()
{
  int i = 0;
  int n = 0;
  int *a = NULL;
  int peak = 0;
  printf("Enter number of elements : ");
  scanf("%d",&n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++)
  {
    printf("Enter element [%d] : ", i);
    scanf("%d",&a[i]);
  }
  print_array(a, n, "Inserted Array");
  
  peak = find_peak(a, n);
  printf("Peak element is: %d\n", peak);
  return 0;
}
