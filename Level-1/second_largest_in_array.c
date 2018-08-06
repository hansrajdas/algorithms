/*
 * Date: 2017-01-27
 *
 * Description: Find second largest number from a unsorted array.
 *
 * Complexity: O(n)
 */

#include "stdio.h"
#include "string.h"

int main()
{
  int i = 0;
  int arr[10] = {40,5,6,1,2,3,22,33,10,2};
  int n = 10;
  int first = 0;
  int second = 0;
  for (i = 0; i < n; i++)
  {
    if (arr[i] > first)
    {
      second = first;
      first = arr[i];
    }
    else if((arr[i] > second) && (arr[i] != first))
    {
      second = arr[i];
    }
  }
  printf("First largest : %d\n", first);
  printf("Second largest : %d\n", second);
  return 0;
}
