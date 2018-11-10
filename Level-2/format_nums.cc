/*
 * Date: 2018-11-10
 *
 * Description:
 * Convert a integer to string representing Indian or US formats like:
 *
 * 1234 => 1,234 in Indian and US format
 * 123456 => 1,23,456 in Indian and 123,456 in US format
 *
 * Approach:
 * Scan each digit from right and place comma after 3 digits. Now check if it's
 * indian format, update comma position to 2 otherwise it will be 3 itself.
 *
 * Complexity:
 * O(N), N is the number of digits in given integer
 */

#include "iostream"
#include "string"  // For to_string()
#include "bits/stdc++.h"  // For reverse()

using namespace std;

#define US 0
#define INDIAN 1

string format_num(int num, int style) {
  string res = "";
  int count = 0;
  int comma_pos = 3;
  bool is_first_comma_added = false;

  // Special case when num = 0
  if (!num) {
    return "0";
  }

  while (num) {
    if (count && !(count % comma_pos)) {
      res += ",";
      if (!is_first_comma_added && style == INDIAN) {
        comma_pos = 2;
        count = 0;
        is_first_comma_added = true;
      }
    }
    res += to_string(num % 10);
    num = num / 10;
    count += 1;
  }
  reverse(res.begin(), res.end());
  return res;
}

int main() {
  cout << "US 123: " << format_num(123, US) << endl;
  cout << "INDIAN 123: " << format_num(123, INDIAN) << endl;

  cout << "US 1234: " << format_num(1234, US) << endl;
  cout << "INDIAN 1234: " << format_num(1234, INDIAN) << endl;

  cout << "US 1234567: " << format_num(1234567, US) << endl;
  cout << "INDIAN 1234567: " << format_num(1234567, INDIAN) << endl;

  cout << "US 12345678: " << format_num(12345678, US) << endl;
  cout << "INDIAN 12345678: " << format_num(12345678, INDIAN) << endl;
}


/*
 * Output:
 * -----------------
 * US 123: 123
 * INDIAN 123: 123
 * US 1234: 1,234
 * INDIAN 1234: 1,234
 * US 1234567: 1,234,567
 * INDIAN 1234567: 12,34,567
 * US 12345678: 12,345,678
 * INDIAN 12345678: 1,23,45,678
*/
