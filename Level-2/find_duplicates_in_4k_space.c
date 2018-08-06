/*
 * Date: 2018-07-23
 *
 * Description:
 * Given an array with all numbers from 1 to N, where N is at most 32,000. The
 * array may have duplicate entries and you do not know what N is. With only
 * 4 kilobytes of memory available, how would you print all duplicate elements
 * in array.
 *
 * Approach:
 * 4 kilobytes is 2^12 byes or 2^15 bits or 32768.
 * As 32768 > 32000 so we can store whole range of inputs in a bit vector. So
 * storing each number at respective bit and checking its presence while
 * scanning other numbers.
 *
 * Complexity:
 * Time: O(n), n is the number of inputs.
 * Space: O(max), max is maximum number in array (less than 32000).
 */

#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_NUM 32000

/*
 * Prints all duplicates in an array.
 *
 * Args:
 * a: Array base address;
 * n: Number of elements in an array.
 * max: Maximum number in array a.
 */
void find_duplicates_in_4k_space(int a[], int n, int max) {
  unsigned short int bytes = (max >> 3) + 1;
  unsigned int i = 0, by_8 = 0, modulo_8 = 0;
  unsigned char *bit_vector = (unsigned char *)malloc(bytes);

  memset(bit_vector, 0, bytes);
  for (; i < n; i++) {
    by_8 = a[i] >> 3;
    modulo_8 = a[i] & 0x07;
    if (bit_vector[by_8] & (1 << modulo_8))
      printf("Duplicate found: %d\n", a[i]);
    else
      bit_vector[by_8] |= 1 << modulo_8;
  }
}

int main() {
  int *a = NULL;
  int n = 0, i = 0, max = 0;
  
  printf("Enter number of elements in array: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int) * n);
  for (; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
    if (a[i] > MAX_NUM) {
      printf("Invalid number, enter numbers not more than %d\n", MAX_NUM);
      return -1;
    }
    if (max < a[i])
      max = a[i];
  }
  find_duplicates_in_4k_space(a, n, max);
  return 0;
}
