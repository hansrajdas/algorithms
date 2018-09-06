/*
 * Date: 2018-09-06
 *
 * Description:
 * Compute 7/8 of a number (7n/8) without using * and / operator.
 *
 * Approach:
 * Shifting left thrice will give n/8 and subtracting this from n will give
 * 7n/8.
 *
 * Complexity:
 * O(1)
 */

int main() {
  int n = 0;
  int res;
  scanf("%d", &n);
  res = (n - (n >> 3));
  printf("%d\n", res);
  return 0;
}
