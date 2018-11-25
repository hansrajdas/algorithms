/*
 * Date: 2017-11-21
 *
 * Description:
 * Implement radix sort.
 *
 * Approach:
 * It is application of counting sort, as range of input element(k) becomes
 * larger radix sort is still able sort the array with O(n) complexity.
 * This sorts on basis of number places that is first starts from least
 * significant digit and then moves to most significant. When sorting is done
 * for all digit places final array is sorted.
 *
 * Reference:
 * http://www.geeksforgeeks.org/radix-sort/
 *
 * Limitation:
 * Only for numbers as it is not comparison sort.
 *
 * Complexity:
 * Time
 *   O(d*(n + b)), n = number of elements, d = digits in max number,
                   b = base in which number is represented, 10 for decimal.
 * Space
 *   O(n + b)
 */

#include "stdio.h"
#include "stdlib.h"

void print_array(int arr[], int n, char *msg) {
  int i = 0;
  printf("*********** %s *****************\n", msg);
  for (i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n\n");
}

int get_max(int a[], int n) {
  int max = a[0];
  int i = 0;
  for (i = 1; i < n; i++) {
    if (max < a[i])
      max = a[i];
  }
  return max;
}

void count_sort(int a[], int n, int place) {
  int i = 0;
  int count[10] = {0};
  int *out = (int *)malloc(sizeof(int) * n);

  for (i = 0; i < n; i++)
    count[(a[i]/place)%10]++;

  // This count is used to keep the numbers in order as per the order of input
  // elements. Like if place = 1 and array is [2, 200, 100, 30] so 200 should
  // appear first then 100 then 30 then 2 as 200 was ahead of 100 and 30 in
  // original array.
  for (i = 1; i < 10; i++)
    count[i] += count[i - 1];

  // Starting from last to maintain order(as per input array) by decrementing
  // the value of count.
  for (i = n - 1; i >= 0; i--) {
    out[count[(a[i]/place)%10] - 1] = a[i];
    count[(a[i]/place)%10]--;
  }

  for (i = 0; i < n; i++)
    a[i] = out[i];
}

int main() {
  int i = 0;
  int n = 0;
  int max = 0, exp = 1;
  int *a = NULL;
  char str[50];
  printf("Enter number of elements: ");
  scanf("%d",&n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d",&a[i]);
  }
  print_array(a, n, "Inserted Array");

  // Find max in array to find the number of digits for which we need to sort.
  max = get_max(a, n);

  // Run counting sort for each decimal place.
  for (exp = 1; max/exp > 0; exp *= 10) {
    count_sort(a, n, exp);
    sprintf(str, "After sorting with exp: %d", exp);
    print_array(a, n, str);
  }
  return 0;
}
