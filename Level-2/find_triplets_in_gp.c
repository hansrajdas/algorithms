/*
 * Date: 2018-10-03
 *
 * Description:
 * Given a sorted array, print triplets which are in geometric progression.
 *
 * Approach:
 * Take a middle element and scan both of array, check if there is a case which
 * satisfies GP condition i.e b/c = d/c, If yes print 3 elements otherwise
 * increment or decrement appropriate counter value.
 *
 * Complexity:
 * O(N^2)
 */

#include "stdio.h"
#include "stdlib.h"

int main() {
  int i = 0, start = 0, end = 0;
  int n = 0;
  int *A = NULL;
  printf("Enter number of elements: ");
  scanf("%d", &n);
  A = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++) {
    printf("Enter element[%d]: ", i);
    scanf("%d", &A[i]);
  }

  for (i = 1; i < n - 1; i++) {
    start = 0;
    end = n - 1;
    while (start < end) {
      if ((A[i]%A[start] == 0) && (A[end]%A[i] == 0) && \
        (A[i]/A[start] == A[end]/A[i])) {
        printf("Elements in geometric progression are - %d %d %d\n", \
            A[start], A[i], A[end]);
        start++;
        end--;
      }
      /*
       * Here A[i]/A[start] > A[end]/A[i] is not used there may be cases where
       * integral part of division may be equal but end needs to decremented
       * instead of incrementing start.
       * Like if input array is [1, 2, 3, 4, 5], in first iteration
       * i = 1, start = 0 and end = 4 so A[start] = 2, A[i] = 1 and A[end] = 5
       * here A[i]/A[start] would become equal to A[end]/A[i], both as 2
       * but we need to decrement end instead of incrementing start to make end
       * at 4.
       */
      else if (A[i] - A[start] >= A[end] - A[i])
        start++;
      else if (A[i] - A[start] <= A[end] - A[i])
        end--;
      else {
        printf("Should not come in this block - \
            start i end are : %d %d %d\n", start, i, end);
        break;
      }
    }
  }
  return 0;
}


/*
 * Output:
 * --------------
 * Enter number of elements: 6
 * Enter element[0]: 10
 * Enter element[1]: 20
 * Enter element[2]: 30
 * Enter element[3]: 40
 * Enter element[4]: 50
 * Enter element[5]: 90
 * Elements in geometric progression are - 10 20 40
 * Elements in geometric progression are - 10 30 90 
 */
