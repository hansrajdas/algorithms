/*
 * Date: 2017-12-23
 *
 * Description:
 * Check if a number is prime or not.
 *
 * Approach:
 * 1. All numbers can be represented in the form of 6k + i for i = -1, 0, 1, 2,
 *    3 and 4.
 * 2. And 6k, 6k + 2, 6k + 4 will always be divisible by 2.
 * 3. 6k + 3 will always be divisible by 3.
 * 4. So we are only left with (6k - 1) and (6k + 1) which can be prime with
 *    exception of 2 and 3.
 * 5. Also we don't have to check for 1 to n or n/2, we only have to check upto
 *    sqrt(n) as larger factor n must be multiple of smaller factor of n that
 *    has been already checked. 
 *
 * Reference:
 * http://www.geeksforgeeks.org/primality-test-set-1-introduction-and-school-method/
 *
 * Complexity:
 * O(sqrt(n))
 */

package main

import (
  "fmt"
)

func is_prime(n uint64) (bool) {
  var i uint64

  if (n <= 1) {
    return false
  }

  // Special case
  if (n == 2 || n == 3) {
    return true
  }

  /*
   * Check for numbers of form 6k, 6k+2, 6k+3, 6k+4, step 2 and 3 above
   */
  if (n % 2 == 0 || n % 3 == 0) {
    return false
  }

  for i = 5; i*i <= n; i = i + 6 {
    if (n % i == 0 || n % (i + 2) == 0) {
      return false
    }
  }
  return true
}

func main() {
  var n uint64
  fmt.Println("Enter number: ")
  _, err := fmt.Scanf("%d", &n)
  if (err == nil) {
    fmt.Println(is_prime(n))
  } else {
    fmt.Println("Scanf failed with error: %v", err)
  }
}
