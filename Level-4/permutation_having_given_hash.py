#!/usr/bin/python

# Date: 2018-
#
# Description:
#
# Approach:
#
# Complexity:
# O(n^2 * n!)

import hashlib


def insertAtPosition(string, char, pos):
  """Inserts a character at given position in string.

  Args:
    string: Given string.
    char: Character to be inserted.
    pos: Position where char needs to be inserted.
  """
  return string[:pos] + char + string[pos:]


def permutation_having_given_hash(string, length, h):
  """Finds permutation of string which computes to given hash.

  Args:
    string: Input string.
    length: Length of string.
  """
  for c in string:
    for i in range(length):
      s = insertAtPosition(string, c, i)
      if hashlib.md5(s).hexdigest() in h:
        return s


def main():
  string = 'poultry outwits ants'
  hash_values = (
      'e4820b45d2277f3844eac66c903e84be',
      '23170acc097c24edb98fc5488ab033fe',
      '665e5bcb0c20062fe8abaaf4628bb154'
  )
  print permutation_having_given_hash(string, len(string), hash_values)


if __name__ == '__main__':
  main()
