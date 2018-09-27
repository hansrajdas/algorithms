/*
 * Date: 2018-09-27
 *
 * Description:
 * Find the count of different elements in an array having elements from 0 to
 * n -1, where n is the number of elements in array.
 *
 * Approach:
 * Use index of auxilary array to store the counts of individual elements.
 *
 * Complexity:
 * O(N) time and space
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0;
  int num_ele = 0;
  int *p_input = NULL;
  int *p_out = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &num_ele);
  p_input = (int *)malloc(num_ele * sizeof(int));
  p_out = (int *)malloc(num_ele * sizeof(int));

  for (i = 0; i < num_ele; i++) {
    printf("Enter element(between 0 to %d) %d: ", num_ele - 1, i);
    scanf("%d", &p_input[i]);
  }
  for (i = 0; i < num_ele; i++)
    p_out[p_input[i]]++;
  for (i = 0; i < num_ele; i++)
    printf("%d->%d\n", i, p_out[i]);

  free (p_input);
  free (p_out);
}


/*
 * Output:
 * ----------
 * Enter number of elements: 5
 * Enter element(between 0 to 4) 0: 3
 * Enter element(between 0 to 4) 1: 4
 * Enter element(between 0 to 4) 2: 3
 * Enter element(between 0 to 4) 3: 2
 * Enter element(between 0 to 4) 4: 3
 * 0->0
 * 1->0
 * 2->1
 * 3->3
 * 4->1
 */
