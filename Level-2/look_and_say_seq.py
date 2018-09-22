#!/usr/bin/python

# Date: 2018-09-22
#
# Description:
# Print look and say sequence for given number of lines.
# https://en.wikipedia.org/wiki/Look-and-say_sequence
#
# Approach:
# Count the numbers which appears same in sequence, when number changes append
# to result count and number. Handle edge cases.
#
# Complexity:
# O(N)


def get_next_seq(val):
  if len(val) == 1:
    return '1' + val

  count = 1
  curr = val[0]
  ret = ''
  for i in range(1, len(val)):
    if curr != val[i]:
      ret += str(count) + curr
      curr = val[i]
      count = 1
    else:
      count += 1

    # Copy last element to return string
    if i == len(val) - 1:
      ret += str(count) + curr

  return ret

def print_look_and_say_seq(n):
  val = '1'
  for i in range(1, n + 1):
    print val
    val = get_next_seq(val)


def main():
  a = []
  n = input('Enter number of lines: ')
  print_look_and_say_seq(n)


if __name__ == '__main__':
  main()


# Output:
# -----------
# Enter number of lines: 2
# 1
# 11

# Enter number of lines: 3
# 1
# 11
# 21

# Enter number of lines: 4
# 1
# 11
# 21
# 1211

# Enter number of lines: 5
# 1
# 11
# 21
# 1211
# 111221

# Enter number of lines: 6
# 1
# 11
# 21
# 1211
# 111221
# 312211

# Enter number of lines: 1
# 1
