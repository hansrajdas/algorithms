/*
 * Date: 2018-06-17
 *
 * Description:
 * Check if a string has all unique characters or not.
 * Approach used to solve this is there are 26 characters in alphabet and int
 * is of size 32 bits. So each character can be stored at one bit position of
 * character(a-z).
 * The problem is solved for only smaller case characters, to extent this for
 * upper case we can take one more variable to store upper case characters.
 *
 * Complexity:
 * Time - O(n), Space - O(1) 
 */

#include "stdio.h"
#include "string.h"

int main() {
  char input[100] = {'\0'};
  int v = 0, i = 0;
  unsigned int val = 0;
  printf("Enter input string (^[a-z]$): ");
  scanf("%s", input);
  for (i = 0; i < strlen(input); i++) {
    v = input[i] - 'a';
    if (val & (1 << v)) {
      printf("Repeated character: %c\n", input[i]);
      break;
    }
    val |= 1 << v;
  }
  if (i == strlen(input))
    printf("All characters are unique\n");
  return 0;
}
