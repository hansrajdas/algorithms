/*
 * Date: 1-Nov-2017
 *
 * Description:
 * John was sitting near to a fireplace in his house, trying to get some warmth
 * from the fire. Fighting his cold at the end of a freezing, Short, dark winter
 * day, he started wondering why it always had to be so cold during this season.
 * That was when he came up with an idea.
 *
 * John stated that winter is the initial pan of the year in which it is always
 * colder than in the remaining part. This latter part is called 'summer'.Then
 * he assumed that summer is always warmer than winter; that is, any temperature
 * measured in winter is colder than every temperature measured in summer.
 *
 * Then he searched the Internet and found the previous years meteorological
 * data, which contained the years temperature measurements. He began to wonder
 * if it might be possible to divide the year into winter and summer so that
 * winter comes before summer and each winter's temperature measurement is
 * smaller than any temperature measured in summer. In case there are many such
 * possible partitions, find the one in which the winter period is as short as
 * possible. (It is quite cold now; there is really no reason for winter to be
 * longer than necessary...)
 *
 * Write a function that, given a sequence T of temperature measurements
 * (specified as integer numbers), finds the partition of the year into winter
 * and summer that meets the conditions above and makes winter as short as
 * possible, then returns the length of the winter. Both winter and summer have
 * to be at least one day long. You can assume that there exists at least one
 * partition that satisfies this condition.
 *
 * For example, given: T = [5, -2, 3, 8, 6]
 *
 * the function should return 3, as after partitioning the year into
 * winter: [5, -2, 3] and summer: [8, 6], each winter's measurement is smaller
 * than each summer's temperature.
 *
 * On the other hand, for the following array: T = [-5, -5, -42, 6, 12]
 *
 * the function should return 4. The partition that minimizes the length of the
 * winter is [-5, -5, -5, -42] and [6, 12]. Winter could also have length 5,
 * but the function should return the shortest possible winter.
 *
 * Assume that:
 * N is an integer within the range [2..300,000];
 * each element of array T is an integer within the range
 * There will be at least one correct way to divide the year into winter and
 * summer.
 *
 * Complexity:
 * expected worst-case time complexity is O(N)
 *
 * In programming words:
 * Write a program to divide an array in such a way that all left side
 * elements are smaller than any right side element .i.e.
 * max of left sub-array < min of right sub-array.
 * Output should be the count of number of elements in left sub-array.
 *
 * Implementation:
 * Keep track of max number while moving from left to right, increment
 * right-sub-array-count if new number is greater than max otherwise set counter
 * to 0 and update max.
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  int left_max = -1;
  int last_max = -1;
  int right_subarray_count = 0;
  printf("Enter number of elements: ");
  scanf("%d",&n);
  a = (int *)malloc(sizeof(int)*n);
  for (; i < n; i++) {
    printf("Enter element [%d]: ", i);
    scanf("%d",&a[i]);
  }

  left_max = a[0];
  last_max = a[0];
  for (i = 1; i < n; i++) {
    if (left_max < a[i]) {
      right_subarray_count++;
      last_max = a[i];
    }
    else {
      right_subarray_count = 0;
      left_max = last_max;
    }
  }
  printf("Number of elements in right sub-array(or winter days) is: %d\n",
         n - right_subarray_count);
  return 0;
}
