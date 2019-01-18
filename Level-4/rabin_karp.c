/*
 * Date: 2017-12-16
 *
 * Description:
 * Rabin karp algo to find all occurrences of a pattern string from a large text
 * string.
 * 
 * Approach:
 * Idea behind rabin karp is a rolling hash is used which can be used to
 * compute new hash from existing hash when a new character is added at end and
 * an existing character is removed from beginning.
 *
 * Reference:
 * http://www-igm.univ-mlv.fr/~lecroq/string/node5.html#SECTION0050
 *
 * Complexity:
 * Space: O(1)
 * Time: Average case - O(n + m), Worst case - O(m*(n-m))
 */

#include "stdio.h"
#include "string.h"

#define MAX_STRING_LEN 1024
#define MAX_PATTERN_LEN 256

/*
 * Finds new hash value having 2 characters different from previous hash.
 * 
 * Args:
 *    first: First character of new string.
 *    last: Last character of new string.
 *    prev_hash: Hash value of previous substring.
 *    d: 2^(m - 1), m is length of pattern string.
 *    
 * Returns:
 *    New hash value.   
 */
unsigned long long int rehash(
  unsigned short int first,
  unsigned short int last,
  unsigned long long int prev_hash,
  unsigned long long int d) {

  unsigned long long int new_hash = ((prev_hash - first*d) << 1) + last;
  return new_hash;
}

/*
 * Description: 
 *    Rabin karp algo to search a substring string. Prints the indexes where
 *    match is found.
 *
 * Args:
 *    str: Bigger text string.
 *    n: length of text string.
 *    pat: pattern string.
 *    m: length of pattern string.
 */
void karp_rabin(char *str, int n, char *pat, int m) {
   unsigned long long d = 1;
   unsigned long long hx = 0, hy = 0;
   unsigned long long i = 0, j = 0;

   /* Preprocessing to computes 2^(m-1) */
   d = d << m - 1;

   for (i = 0; i < m; ++i) {
      hx = ((hx<<1) + pat[i]);
      hy = ((hy<<1) + str[i]);
   }

   /* Searching */
   while (j <= n-m) {
      if (hx == hy && memcmp(pat, str + j, m) == 0) {
         printf("Pattern found at index: %llu\n", j);
      }
      hy = rehash(str[j], str[j + m], hy, d);
      ++j;
   }
}

int main() {
  char text[MAX_STRING_LEN];
  char pattern[MAX_PATTERN_LEN];

  printf("Enter text string: ");
  fgets(text, MAX_STRING_LEN, stdin);

  printf("Enter patter to be searched: ");
  fgets(pattern, MAX_PATTERN_LEN, stdin);

  karp_rabin(text, strlen(text) - 1, pattern, strlen(pattern) - 1);
}
