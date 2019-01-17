/*
 * Date: 2018-06-21
 *
 * Description:
 * Given 2 strings, check weather both strings are one or zero edit away or not.
 * Operations allowed in edits are inert, replace or delete a char.
 * Like 'abc' and 'ab", 'abc' and 'abd', 'ab' and 'abc'.
 *
 * Approach:
 * Consider insert and delete as same operation(by keeping track of smaller
 * string, if length not same) and checking accordingly.
 *
 * Complexity:
 * Time: O(n), Space: O(1)
 */

#include "stdio.h"
#include "string.h"
#include "stdlib.h"

#define MAX_LEN 100
#define FALSE 0
#define TRUE 1

void swap(unsigned short int *A, unsigned short int *B) {
  *A = *A + (*B);
  *B = *A - (*B);
  *A = *A - (*B);
}

/*
 * Checks weather 2 strings are max one edit away or not.
 * 
 * Args:
 * s1: First string
 * l1: Length of first string.
 * s2: Second string
 * l2: Length of second string.
 *
 * Returns:
 * 1 - If both strings are max one edit away.
 * 0 - If 2 strings are more than one edit away.
 */
unsigned short int are_two_strings_one_edit_away(char s1[],
                                                 unsigned short int l1,
                                                 char s2[],
                                                 unsigned short int l2) {
  unsigned short int idx_1 = 0, idx_2 = 0;
  unsigned short int one_diff_found = FALSE;
  char *temp_1 = NULL, *temp_2 = NULL;

  // If difference in string lengths are more than one, they can't be one edit
  // away.
  if (abs(l1 - l2) > 1)
    return FALSE;
  
  // Keep track of smaller and longer string, temp_1 to have smaller string and
  // temp_2 to have longer with lengths also.
  // This is done to consider delete and insert as same operation.
  // We will consider insert in temp_1 and delete from temp_2.
  if(l1 <= l2) {
    temp_1 = s1;
    temp_2 = s2;
  } else {
    temp_1 = s2;
    temp_2 = s1;
    swap(&l1, &l2);
  }

  while (idx_1 < l1 && idx_2 < l2) {
    if (temp_1[idx_1] != temp_2[idx_2]) {
      if (one_diff_found)
        return FALSE;
      one_diff_found = TRUE;  // One diff found.

      // If lengths of both strings are equal, there would be an update
      // (no insert/delete). So incrementing idx_1 here, idx_2 will be
      // incremented below.
      if (l1 == l2)
        idx_1++;
    } else
      idx_1++;  // Characters same, increment both indexes.

    // Longer string index should always be increased. Case when only idx_2 will
    // be incremented is when current characters are different and temp_1 is
    // smaller.
    idx_2++;
  }
  return TRUE;
}

int main() {
	char string_1[MAX_LEN] = {'\0'}, string_2[MAX_LEN] = {'\0'};
  unsigned short int len_1 = 0, len_2 = 0;

  printf("Enter first string: ");
	fgets(string_1, MAX_LEN, stdin);
  len_1 = strlen(string_1);

  printf("Enter second string: ");
	fgets(string_2, MAX_LEN, stdin);
  len_2 = strlen(string_2);

  // fgets also includes '\n' in string length so len - 1.
  if (are_two_strings_one_edit_away(string_1, len_1 - 1, string_2, len_2 - 1))
    printf("Yes, Both strings are one edit away!\n");
  else
    printf("No, Both strings are *NOT* one edit away!\n");
  return 0;
}
