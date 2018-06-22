/*
 * Date: 2018-06-22
 *
 * Description:
 * Compress a given string. Add count for the consecutive repeated characters.
 * Like aaabb -> a3b2, abbbccca -> a1b3c3a.
 * If compressed string length is not smaller than original string then return
 * original string itself.
 *
 * Approach:
 * Check for previous and current character, if same keep on incrementing
 * counter otherwise copy character and count to compressed string.
 *
 * Complexity:
 * Time: O(n), Space: O(1)
 */

#include "stdio.h"
#include "string.h"
#include "stdlib.h"

#define MAX_LEN 100

char *string_compression(char s[], unsigned short int l) {
  char *compressed = (char *)malloc(sizeof(char) * MAX_LEN);
  char prev_chr = s[0], temp[5] = {'\0'};
  unsigned short int ctr = 1, idx = 1, c_idx = 0;

  while (idx < l) {
    if (prev_chr == s[idx])
      ctr++;
    else
    {
      compressed[c_idx++] = prev_chr;

      // We can also do ctr + '0' to get char from int but would fail if ctr is
      // 2 digit number (more than 9).
      sprintf(temp, "%d", ctr);
      strncpy(compressed + c_idx, temp, strlen(temp));
      c_idx += strlen(temp);
      prev_chr = s[idx];
      ctr = 1;
      memset(temp, '\0', 5);
    }
    idx++;
  }
  compressed[c_idx++] = prev_chr;
  sprintf(temp, "%d", ctr);
  strncpy(compressed + c_idx, temp, strlen(temp));
  compressed[c_idx + strlen(temp)] = '\0';

  if (l > strlen(compressed))
    return compressed;
  return s;
}

int main() {
	char input[MAX_LEN] = {'\0'};

  printf("Enter string: ");
	scanf("%s", input);
  printf("Compressed string: %s\n", string_compression(input, strlen(input)));
  return 0;
}
