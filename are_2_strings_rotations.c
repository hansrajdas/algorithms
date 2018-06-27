/*
 * Date: 2018-06-27
 *
 * Description:
 * Given 2 strings s1 and s2, check if string s2 is rotation of s1 or not.
 *
 * Approach:
 * If string s2 is rotation of s1 then, s2 must be substring of s1 + s2.
 *
 * Complexity:
 * Time: O(n), Space: O(n), n = length of string.
 */

#include "stdio.h"
#include "string.h"
#include "stdlib.h"

#define MAX_LEN 100

char *are_rotations (char *s1, char *s2, int len1, int len2) {
  char *concated_str = NULL;

  if (len1 != len2)
    return NULL;
  concated_str = (char *)malloc(sizeof(s1) * 2);
  sprintf(concated_str, "%s%s", s1, s1);  // Create s1 + s1.
  return strstr(concated_str, s2);
} 

int main() {
	char str1[MAX_LEN] = {'\0'}, str2[MAX_LEN] = {'\0'};

  printf("Enter first string: ");
	scanf("%s", str1);

  printf("Enter second string: ");
	scanf("%s", str2);

  if (are_rotations(str1, str2, strlen(str1), strlen(str2)))
    printf("Yes\n");
  else
    printf("No\n");
  return 0;
}
