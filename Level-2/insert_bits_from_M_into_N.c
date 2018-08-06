/*
 * Date: 2018-07-04
 *
 * Description:
 * Given 2 32-bit numbers, N and M, and 2 bit positions i and j. Write a method
 * to insert M into N such that M starts at bit j and ends at bit i (j > i).
 * 
 * Example:
 * Input: N = 10000000000, M = 10011, i = 2, j = 6
 * Output: 10001001100
 *
 * Approach:
 * Create a mask which clears bits between i and j in N => First number
 * Shift M left by i positions => Second number
 * Take OR of first and second number.
 *
 * Complexity:
 * O(1)
 */

#include "stdio.h"

void binary_representation(int n) {
  unsigned short int size = sizeof(int) * 8;
  unsigned short int space = 0;
  unsigned int i = 0;
  printf("Binary representation of %d is: ", n);

  // Checking bit at individual position and printing 0 or 1.
  for (i = 1 << size - 1; i > 0; i = i/2) {
    if (space == 4) {
      space = 0;
      (n & i) ? printf(" 1") : printf(" 0");  // Add space between each nibble.
    } else {
      (n & i) ? printf("1") : printf("0");
    }
    space++;
  }
  printf("\n");
}

/*
 * Inserts M into N at positions between i and j.
 * 
 * Args:
 * M: Number to be inserted.
 * N: Number in which M needs to inserted.
 * i: Starting bit position (right)
 * j: End bit position (left), j > i.
 */
void insert_M_into_N(int M, int N, int i, int j) {
  int m_shifted = M << i;
  int all_ones = ~0;
  int right = (1 << i) - 1;  // Create a sequence of 0s then 1s.
  int left = all_ones << (j + 1);  // Create a sequence of 1s then 0s.

  // Create a mask which is 0s at position between i and j and 1s at other
  // positions.
  int mask = left | right;
  int n_masked = N & mask;

  int res = n_masked | m_shifted;
  
  binary_representation(res);
}

int main() {
  int N = 0, M = 0;
  int i = 0, j = 0;
  
  printf("Enter M: ");
  scanf("%d", &M);
  binary_representation(M);

  printf("Enter N: ");
  scanf("%d", &N);
  binary_representation(N);

  printf("Enter i and j (starting and end position): ");
  scanf("%d", &i);
  scanf("%d", &j);

  insert_M_into_N(M, N, i, j);
  return 0;
}

/*
 Enter M: 10
 Binary representation of 10 is: 0000 0000 0000 0000 0000 0000 0000 1010
 Enter N: 1024
 Binary representation of 1024 is: 0000 0000 0000 0000 0000 0100 0000 0000
 Enter i and j (starting and end position): 2
 5
 Binary representation of 1064 is: 0000 0000 0000 0000 0000 0100 0010 1000
*/
