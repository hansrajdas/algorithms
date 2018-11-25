#include "stdio.h"
#include "string.h"

/*
 * Date: 2018-05-21
 *
 * Problem description:
 * You are a gate keeper and there is a queue of people wearing caps in
 * forward or backward directions. Your job is to change the orientation of
 * cap for everyone (either all wearing forward or backward) with minimum
 * commands. Everyone in the queue knows his position. You can give command
 * "Person in position x through y(inclusive), flip your caps".
 *
 * Like caps orientations are:
 * ['F', 'B', 'F', 'F']
 * - Person in position 1, flip your cap(s).
 *
 * ['B', 'F', 'F', 'B', 'B', 'F']   
 * - Person in position 1 through 2, flip your cap(s).
 * - Person in position 5, flip your cap(s).
 *
 * For further details, please refer: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s095-programming-for-the-puzzled-january-iap-2018/puzzle-1-you-will-all-conform/MIT6_S095IAP18_Puzzle_1.pdf
 *
 * Approach:
 * Take first person as reference, all who has orientation opposite to first,
 * flip his cap. This approach helps to get all caps in same orientation with
 * minimum commands and one iteration only.
 *
 * Reference:
 * https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s095-programming-for-the-puzzled-january-iap-2018/puzzle-1-you-will-all-conform/MIT6_S095IAP18_Puzzle_1.pdf
 *
 * Complexity: O(n)
 */


 int main() {
  char caps[50] = {'\0'};
  int i = 0, len = 0, num = 0, start = 0;

  printf("Enter cap positions(string of 'F' and 'B' like FBBFF: ");
  scanf("%s", caps);
  len = strlen(caps);

  printf("**************** Cap indexes *************************\n");
  for (i = 0; i < len; i++) {
    printf("%c \t%d\n", caps[i], i);
  }
  printf("******************************************************\n");

  // This saves from scenario when there is only one person in queue as we are
  // starting from index 1.
  caps[len] = caps[0];
  len += 1;
  for (i = 1; i < len; i++) {
    if (caps[i] != caps[i - 1]) {
      if (caps[i] != caps[0]) {
        start = i;
        printf("Command-%d: Person in position %d", ++num, i);
      } else {
        if (start == i -1)
          printf(", flip your cap\n");
        else 
          printf(" through %d, flip your caps\n", i - 1);
      }
    }
  }
  return 0;
 }
