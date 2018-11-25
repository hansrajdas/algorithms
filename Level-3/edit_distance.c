/*
 * Date: 2018-05-07
 *
 * Description:
 * Find operations required to change a source string(str1) to target(str2).
 * Operations allowed are (on source string):
 * - Insert a character 
 * - Remove a character or
 * - Replace a character
 *
 * Reference:
 * https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
 *
 * Complexity:
 * Time: O(mxn)
 * Space: O(mxn)
 */

#include "stdio.h"
#include "string.h"
#include "stdlib.h"


/* Finds minimum of 3 numbers. */
int min(int a, int b, int c) {
  return a < b ? (a < c ? a : c): (b < c ? b : c);
}

/*
 * Finds minimum distance to convert str1 to str2.
 *
 * Args:
 *  str1: Source string.
 *  str2: Target string.
 *  m: Length of source string.
 *  n: Length of target string.
 */
int edit_distance(char s1[], char s2[], int m, int n) {
  int i = 0, j = 0;

  /* Store results of subproblems. */
  int **dp = (int **)malloc((m + 1)*sizeof(int *));

  for (i = 0; i <= m; i++)
    dp[i] = (int *)malloc(sizeof(n + 1)*sizeof(int));

  /* Fill dp in bottom up manner. */
  for (i = 0; i <= m; i++) {
    for (j = 0; j <= n; j++) {
      /*
       * If first string is empty, insert all characters present in second
       * string.
       */
      if (i == 0)
        dp[i][j] = j;
      /*
       * If second string is empty, remove all characters present in first
       * string.
       */
      else if (j == 0)
        dp[i][j] = i;
      /*
       * If current characters are same in both strings, nothing to do, just
       * copy the operations required till previous string lengths.
       */
      else if (s1[i - 1] == s2[j - 1])
        dp[i][j] = dp[i - 1][j - 1];
      /*
       * If current characters are different, check how minimum can be achieved
       * using inserting, removing or deleting a character.
       */
      else
        dp[i][j] = 1 + min(
            dp[i][j - 1],  // Insert
            dp[i - 1][j],  // Remove
            dp[i - 1][j - 1]);  // Replace
    }
  }
  return dp[m][n];
}

int main() {
  char str1[50] = {'\0'};
  char str2[50] = {'\0'};

  printf("Enter first string: ");
  scanf("%s", str1);
  
  printf("Enter second string: ");
  scanf("%s", str2);

  printf("Operations required to convert from %s to %s: %d\n",
    str1, str2, edit_distance(str1, str2, strlen(str1), strlen(str2)));
 }


/*
 * Output:
 *  Enter first string: sunday
 *  Enter second string: saturday
 *  Operations required to convert from sunday to saturday: 3
 */
