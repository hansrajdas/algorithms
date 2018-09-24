/*
 * Date: 2017-12-24
 *
 * Description:
 * Find square root of a number with some error approximation.
 *
 * Approach:
 * This uses convergence theory, The basic idea is that if x is an 
 * overestimate to the square root of a non-negative real number S then S/x
 * will be an underestimate, or vice versa, and so the average of these two
 * numbers may reasonably be expected to provide a better approximation.
 *
 * Complexity:
 *
 * | n      | Loop count |
 * | 0.0001 | 8          |
 * | 0.001  | 7          |
 * | 0.01   | 5          |
 * | 0.1    | 4          |
 * | 1      | 0          |
 * | 10     | 4          |
 * | 100    | 6          |
 * | 1000   | 8          |
 * | 10000  | 10         |
 * |________|____________|
 *
 * So for larger inputs(n > 10) it is very less compared to O(logn).
 *
 * Reference: 
 * https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
 *
 */

package main

import (
  "fmt"
)

func babylonian_square_root(n float64) (float64) {
  var x float64  // Initial assumption x as square root of n
  var y float64  // Lower bound of square root
  var e float64  // Error margin, recommended to provide some non-zero error margin

  if n > 1 {
    x = n
    y = 1
  } else {
    x = 1
    y = n
  }

  e = 0.001

  count := 0
  for x - y > e {
    x = (x + y)/2
    y = n/x
    count++
  }
  fmt.Println("Loop count: ", count)
  return x
}

func main() {
  var n float64
  fmt.Println("Enter number: ")
  _, err := fmt.Scanf("%f", &n)
  if err == nil {
    fmt.Println(babylonian_square_root(n))
  } else {
    fmt.Println("Scanf() failed with error: ", err)
  }
}
