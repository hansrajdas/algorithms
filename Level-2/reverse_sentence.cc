/*
 * Date: 2018-11-10
 *
 * Description:
 * Given a sentence, reverse it's individual words. For example if sentence is
 * "Hello World" it should be changed to "World Hello".
 *
 * Approach:
 * - First, reverse whole string
 * - Take individual words from reversed string and reverse them
 * - Above 2 steps will result in reversed words in sentence.
 *
 * Complexity:
 * O(N)
 */

#include "iostream"

using namespace std;

string reverse_string(string s) {
  int start = 0;
  int end = s.size() - 1;
  char c;

  while (start < end) {
    c = s[start];
    s[start] = s[end];
    s[end] = c;
    start += 1;
    end -= 1;
  }
  return s;
}

int main() {
  string input;
  string reversed;
  string temp = "";
  string result = "";
  int i = 0;

  cout << "Enter a sentence: ";
  getline(cin, input);

  // Step 1: Reverse whole string
  reversed = reverse_string(input);
  cout << "Reversed string: " << reversed << endl;

  // Step 2: Now reverse individual words
  while (i <= reversed.size()) {
    if (reversed[i] == ' ' || reversed[i] == '\0') {
      result += reverse_string(temp) + ' ';
      temp = "";
    }
    else
      temp += reversed[i];
    i += 1;
  }
  result += temp;
  cout << "Reversed words in sentence: " << result << endl;
}


/*
 * Output:
 * -------------------
 * Enter a sentence: Coding is fun
 * Reversed string: nuf si gnidoC
 * Reversed words in sentence: fun is Coding 
 *
 * Enter a sentence: hello
 * Reversed string: olleh
 * Reversed words in sentence: hello 
 */
