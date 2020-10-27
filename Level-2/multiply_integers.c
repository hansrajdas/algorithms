/*
 * Date: 2018-08-01
 *
 * Description:
 * Write a recursive function to multiply two positive integers without using
 * multiply (*) operator (/ operator). You can use +, - and bit shifting, but
 * you should minimize the number of those operations.
 *
 * Approach:
 * We iterate smaller number of times, dividing by 2 in every iteration. In
 * every iteration if smaller is even we double the result otherwise for we add
 * bigger number as well. Like suppose P is the current product then:
 * 2P => P + P => P << 1
 * 3P => P + P + P => (P << 1) + P
 *
 * Complexity:
 * O(log(s)), s = smaller number.
 */

#include "stdio.h"

int findProduct(int smaller, int bigger) {
  int halfProduct = 1;
  int s = smaller >> 1;  // Divide smaller by 2.

  if (!smaller) return 0;
  if (smaller == 1) return bigger;

  halfProduct = findProduct(s, bigger);

  // If smaller number is odd, double the product add bigger like:
  // (2x + 1)*y would be 2xy + y.
  // For even just double the existing product.
  if (smaller % 2) return (halfProduct << 1) + bigger;
  return halfProduct << 1;
}

int main() {
  int first = 0, second = 0;
  int smaller = 0, bigger = 0;
  printf("Enter first number: ");
  scanf("%d", &first);
  printf("Enter second number: ");
  scanf("%d", &second);

  smaller = first < second ? first : second;
  bigger = first < second ? second : first;
  printf("Product of 2 numbers: %d\n", findProduct(smaller, bigger));
  return 0;
}

/*
Output:
******************************
Enter first number: 4
Enter second number: 5
Product of 2 numbers: 20

Enter first number: 2
Enter second number: 3
Product of 2 numbers: 6

Enter first number: 5
Enter second number: 4
Product of 2 numbers: 20

Enter first number: 5
Enter second number: 40
Product of 2 numbers: 200

Enter first number: 10
Enter second number: 12
Product of 2 numbers: 120

Enter first number: 100
Enter second number: 200
Product of 2 numbers: 20000

Enter first number: 300
Enter second number: 45
Product of 2 numbers: 13500
*/
