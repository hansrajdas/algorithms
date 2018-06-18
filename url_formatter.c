/*
 * Date: 2018-06-18
 *
 * Description:
 * Update input string to replace space(" ") with "%20".
 * 
 * Approach:
 * Effectively one character is being replaced with 3 characters so first we can
 * count the number of spaces in input string and find the effective length of
 * new string.
 * Also, start from last so that overwriting input string is not an issue.
 *
 * Complexity:
 * Time - O(n), Space - O(1)
 *
 * Note:
 * As character array is mutable (can be updated in-place) in C so we can update
 * input string(new string is not required). In other languages like python
 * where string is immutable we will have to create a new string and can be done
 * in one traversal.
 */

#include "stdio.h"
#include "string.h"

/*
 * Updates input string (in-place) to have space replaced with %20.
 * Args:
 * s: Input string.
 *
 * Returns updated string.
 */
char *url_foramtter(char s[]) {
  unsigned int new_length = 0, original_length = strlen(s);
  unsigned int i = 0, new_idx = 0, space_count = 0;
  for (i = 0; i < original_length; i++) {
    if (s[i] == ' ')
      space_count++;
  }
  new_length = original_length + 2 * space_count;
  printf("Length of original string: %d\n", original_length);
  printf("Spaces in original string: %d\n", space_count);
  printf("Length of updated string: %d\n", new_length);
  
  new_idx = new_length;
  for (i = original_length; i > 0; i--) {
    if (s[i - 1] == ' ') {
      s[--new_idx] = '0';
      s[--new_idx] = '2';
      s[--new_idx] = '%';
    } else {
      s[--new_idx] = s[i - 1];
    }
  }
  return s;
}

int main() {
  char input[100] = {'\0'};
  printf("Enter input string: ");
  fgets(input, 100, stdin);
  printf("\nUpdated string: %s\n", url_foramtter(input));
  return 0;
}
