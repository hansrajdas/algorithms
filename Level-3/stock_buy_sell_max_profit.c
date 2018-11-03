/*
 * Date: 2018-10-03
 *
 * Description:
 * The cost of a stock on each day is given in an array, find the max profit
 * that you can make by buying and selling in those days.
 *
 * For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the
 * maximum profit can earned by buying on day 0, selling on day 3. Again buy on
 * day 4 and sell on day 6. If the given array of prices is sorted in decreasing
 * order, then profit cannot be earned at all.
 *
 * Approach:
 * Scan array from starting and find a number is smaller than it's next element,
 * this would be our buying day(local minima).
 * Now start from buying day and scan array till array elements are in
 * increasing order, as next element decreases, it is our selling day(local
 * maxima).
 * Repeat above steps as we are done scanning all elements.
 *
 * Complexity:
 * O(N)
 */

#include "stdio.h"
#include "stdlib.h"

typedef struct interval {
  int buy;
  int sell;
} interval;

void stockBuySell(int a[], int n) {
  int i = 0;
  int count = 0;
  interval *p = NULL;
  p = (interval *)malloc(sizeof(interval)*(n/2 + 1));

  while (i < n - 1) {
    while ((i < n - 1) && (a[i + 1] <= a[i])) // Find Local minima
      i++;

    if (i == n - 1)
      break;
    p->buy = i++;
    
    while ((i < n) && (a[i - 1] <= a[i])) // Find local maxima
      i++;
    p->sell = i - 1;

    p = p + sizeof(interval);
    count++;
  }
  if (!count)
    printf("No day when buying stocks will make profit\n");
  else {
    p = p - sizeof(interval)*count;
    for (i = 0; i < count; i++) {
      printf("Buy on %d\tSell on %d\n",p->buy, p->sell);
      p = p + sizeof(interval);
    }
  }
}
int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &a[i]);
  }
  stockBuySell(a, n);
  return 0;
}


/*
 * Output:
 * ----------------------------
 * Enter number of elements: 7
 * Enter element[0]: 100
 * Enter element[1]: 180
 * Enter element[2]: 260
 * Enter element[3]: 310
 * Enter element[4]: 40
 * Enter element[5]: 535
 * Enter element[6]: 695
 * Buy on 0	Sell on 3
 * Buy on 4	Sell on 6
 *
 * Enter number of elements: 4
 * Enter element[0]: 1
 * Enter element[1]: 2
 * Enter element[2]: 3
 * Enter element[3]: 4
 * Buy on 0	Sell on 3
 *
 * Enter number of elements: 4
 * Enter element[0]: 4
 * Enter element[1]: 3
 * Enter element[2]: 2
 * Enter element[3]: 1
 * No day when buying stocks will make profit 
 */
