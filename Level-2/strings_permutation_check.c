/*
 * Date: 2018-06-17
 *
 * Description:
 * Check if two strings are permutation of each other or not.
 * 2 strings can be permutation of each other if both strings have same number
 * of all characters in same or different order like 'abc' and 'cba' and 'aabbc'
 * and 'bbcaa' and both strings must have same length.
 *
 * Complexity:
 * Time - O(n), Space - O(1) 
 */

#include "stdio.h"
#include "string.h"

/*
 * Checks if 2 strings are permutation of each other or not.
 * - Both strings must have same length.
 * - Occurence of all characters in both strings must be same.
 *
 * Args:
 * s: First string.
 * t: Second string.
 */
int both_strings_permutation(char *s, char *t) {
  int len = strlen(s);
  int i = 0, map[256] = {0};

  if (len != strlen(t))
    return 0;
  for (i = 0; i < len; i++) {
    map[s[i]]++;  
  }
  for (i = 0; i < len; i++) {
    map[t[i]]--;
    if (map[t[i]] < 0)
      return 0;
  }
  return 1;
}

int main() {
  char string_1[100] = {'\0'}, string_2[100] = {'\0'};

  printf("Enter first string: ");
  scanf("%s", string_1);
  printf("Enter second string: ");
  scanf("%s", string_2);

  if (both_strings_permutation(string_1, string_2))
    printf("Both strings are permutation of each other\n");
  else
    printf("Both strings are NOT permutation of each other\n");
  return 0;
}
