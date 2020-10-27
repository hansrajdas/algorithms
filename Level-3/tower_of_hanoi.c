/*
 * Date: 2018-08-02
 *
 * Description:
 * Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
 * The objective of the puzzle is to move the entire stack to another rod,
 * obeying the following simple rules:
 * 1) Only one disk can be moved at a time.
 * 2) Each move consists of taking the upper disk from one of the stacks and
 *    placing it on top of another stack i.e. a disk can only be moved if it is
 *    the uppermost disk on a stack.
 * 3) No disk may be placed on top of a smaller disk.
 *
 * Approach:
 * We can try solving this problem with n = 1, 2, 3 and follow the pattern
 * recursively.
 * Calling 3 towers with character - A, B and C.
 *
 * Reference:
 * https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
 *
 * Complexity:
 * O(2^n), For n disks 2^n - 1 steps are required.
 */

#include "stdio.h"

/*
 * Prints steps to solve TOH problem, moves disks from srcTower to dstTower.
 *
 * Args:
 * n: Number of disks.
 * srcTower: Tower which contains all disks.
 * dstTower: Tower where all disks needs to be moved.
 * bufferTower: Buffer tower.
 */
void towerOfHanoi(int n, char srcTower, char dstTower, char bufferTower) {
  if (n <= 0) return;
  if (n == 1) {
    printf("Move disk 1 from tower %c to %c\n", srcTower, dstTower);
    return;
  }
  towerOfHanoi(n - 1, srcTower, bufferTower, dstTower);
  printf("Move dist %d from tower %c to %c\n", n, srcTower, dstTower);
  towerOfHanoi(n - 1, bufferTower, dstTower, srcTower);
}

int main() {
  int i = 0;
  int n = 0;
  printf("Enter number of disks: ");
  scanf("%d", &n);
  towerOfHanoi(n, 'A', 'B', 'C');
  return 0;
}

/*
Output:
************************
Enter number of disks: 2
Move disk 1 from tower A to C
Move dist 2 from tower A to B
Move disk 1 from tower C to B
************************
Enter number of disks: 3
Move disk 1 from tower A to B
Move dist 2 from tower A to C
Move disk 1 from tower B to C
Move dist 3 from tower A to B
Move disk 1 from tower C to A
Move dist 2 from tower C to B
Move disk 1 from tower A to B
************************
Enter number of disks: 1
Move disk 1 from tower A to B
*/
