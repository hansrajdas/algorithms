/*
 * Date: 2018-09-27
 *
 * Description:
 * There is an unsorted array having elements from 1 to n, n is the number of
 * elements in array. Count the frequency of each element from that array.
 *
 * Approach:
 * We can decrement array elements by 1 to make elements from 0 to n - 1
 * instead of 1 to n and use array elements as array index. While iterating we
 * can take modulus with number of elements and add number of elements to that
 * array element.
 * So at the end we will add number of elements to a number as many times as
 * it was repeated. Later we can divide by number of elements to get the actual
 * count.
 * Example - [3, 3, 3]
 * Decrement 1 from each element - [2, 2, 2]
 *
 * After first iteration of % loop ends:
 * A[A[0] % 3] = A[A[0] % 3] + 3, A[2] = 2 + 3 = 5 which indicates that 2 + 1
 * .i.e 3 has been encountered 5/3 = 1 times.
 *
 * Complexity:
 * O(N) Time
 * O(1) Space
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int num_ele = 0;
  int *p_input = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &num_ele);
  p_input = (int *)malloc(num_ele * sizeof(int));
  for (i = 0; i < num_ele; i++) {
    printf("Enter element(1 to %d) %d: ", num_ele, i);
    scanf("%d", &p_input[i]);
  }

  // Make elements from 0 to n - 1 to accommodate in array indexes.
  for (i = 0; i < num_ele; i++)
    p_input[i] = p_input[i] - 1;

  // Add num_ele to index as many times same number has occurred.
  for (i = 0; i < num_ele; i++)
    p_input[p_input[i] % num_ele] = p_input[p_input[i] % num_ele] + num_ele;

  // Print counts to numbers from 1 to n, now count would be array
  // element/num_ele as we have added num_ele as many times as number has
  // occurred.
  for (i = 0; i < num_ele; i++)
    printf("%d -> %d\n", i + 1, p_input[i] / num_ele);

  free (p_input);
}

/*
 * Output:
 * ------------------------
 * Enter number of elements: 5
 * Enter element 0: 3
 * Enter element 1: 4
 * Enter element 2: 4
 * Enter element 3: 5
 * Enter element 4: 5
 * 1 -> 0
 * 2 -> 0
 * 3 -> 1
 * 4 -> 2
 * 5 -> 2
 */
