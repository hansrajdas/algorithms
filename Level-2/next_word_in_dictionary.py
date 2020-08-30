# Date: 2018-09-06
#
# Description:
# Given a string, find the next dictionary word using the characters in given
# string. If given string is the last dictionary word, return 'no answer'
# For example:
# 'abc' => 'acb'
# 'cba' => 'no answer'
# 'z' => 'no answer'
#
# Approach:
# Scan string from last till we find character which is less than adjacent
# right char. Swap those 2 chars, this will give the next dictionary word.
#
# Complexity:
# Time - O(n), n is the length of string

def print_next_string(string):
  if len(string) == 1:
    if string == 'z' or string == 'Z':
      return 'no answer'
    return chr(ord(string) + 1)

  ctr = len(string)
  lis = list(string)
  while ctr > 1:
    if lis[ctr - 1] > lis[ctr - 2]:
      lis[ctr - 1], lis[ctr - 2] = lis[ctr - 2], lis[ctr - 1]
      return ''.join(lis)
    ctr -= 1
  return 'no answer'

assert print_next_string('z') == 'no answer'
assert print_next_string('zzzz') == 'no answer'
assert print_next_string('cba') == 'no answer'
assert print_next_string('abc') == 'acb'
assert print_next_string('a') == 'b'
