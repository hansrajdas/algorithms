/*
 * Date: 2018-09-06
 *
 * Description:
 * Write a string compare function which ignores character case. Like "Hello"
 * and "HELLO" should be same.
 *
 * Approach:
 * Capital characters starts from 65 and smaller starts from 97 so there is a
 * difference of 32 between them.
 * We can check if current character is same or have a difference of 32 we will
 * consider them same.
 *
 * Complexity:
 * O(n), n = length of string.
 */

#include "stdio.h"
#include "string.h"

int my_strcmp(char *s1, char *s2) {
  int len = 0, ret_val = 1, i = 0, diff;

  if (strlen(s1) != strlen(s2))
    ret_val = 0;
  else {
    len = strlen(s1);
    while (i < len) {
      diff = s1[i] - s2[i];
      if ((s1[i] == s2[i]) || (32 == (diff > 0 ? diff : (-1 * diff))))
        i++;
      else {
        ret_val = 0;
        break;
      }
    }
  }
  return ret_val;
}

int main() {
  char str1[20] = {'\0'};
  char str2[20] = {'\0'};

  printf("Enter string 1: ");
  scanf("%s", str1);

  printf("Enter string 2: ");
  scanf("%s", str2);

  if (my_strcmp(str1, str2))
    printf("Same\n");
  else
    printf("Not same\n");
  return 0;
}
