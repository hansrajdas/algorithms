#!/usr/bin/python

# Date: 2018-10-10
#
# Description:
# Given a string and 3 md5 hashes, find the anagram of given string which has
# given md5 hash.
# You are also given a wordlist file having around 0.1 million words, which
# might help you out.
#
# Approach:
# - Filter words from wordlist file given, which can't be anagram.
# - Find the length of maximum string left in wordlist after filtering, it
# comes out to be 11.
#
# - We know length of input string is 18(20 - 2) so we find all triplets which
# sums to 18 and compute all combinations.
#
# Solution:
# printout stout yawls
# ty outlaws printouts


import collections
import hashlib


def is_valid(word, char_freq):
  """
  Checks whether given word has character counts not more than counts given in
  dictionary.

  Args:
    word: A word from wordlist.
    char_freq: Dictionary with frequency of each character in input string.
  """
  char_count = collections.defaultdict(int)
  for c in word:
    char_count[c] += 1

  for c in char_count:
    if char_count[c] > char_freq[c]:
      return False
  return True


def get_valid_words(char_count):
  """
  Reads wordlist and filter words which can be part of anagram of given string.

  Args:
    char_count: Dictionary with frequency of each character in input string.
  """
  with open('/home/hansraj/Downloads/wordlist') as fp:
    valid_words = []
    word = fp.readline().strip()
    while word:
      if is_valid(word, char_count):
        valid_words.append(word)
      word = fp.readline()
      if word:
        word = word.strip()

  return valid_words


def string_anagram_with_given_md5hash(string, length, expected_hash):
  """Finds anagram of given string which has expected md5 hash.

  Args:
    string: Input string.
    length: Length of input string.
    expected_hash: Tuple with expected hash values.
  """

  # Compute count of each character in input string.
  char_count = collections.defaultdict(int)
  for c in string:
    char_count[c] += 1

  valid_words = get_valid_words(char_count)

  # Create a dictionary to group all words with same length.
  word_lengths = collections.defaultdict(list)
  for word in valid_words:
    word_lengths[len(word)].append(word)

  # We are left with 1788 words from wordlist which can be part of anagram of
  # given string.
  # Also strings with which we are left with has lengths from 1 to 11.
  # And length of given string 'poultry outwits ants' is 20 and if we exclude
  # 2 spaces we are left with string length of 18. So effectively now we have
  # to generate a string which has length of 18 using 1788 words.
  triplets_with_sum_18 = []
  max_len = max(l for l in word_lengths)  # 11

  # Find triplets which sums to 18, using numbers from 1 to 11.
  for i in range(1, max_len + 1):
    for j in range(1, max_len + 1):
      for k in range(1, max_len + 1):
        if i + j + k == length - 2:  # -2 for 2 spaces
          triplets_with_sum_18.append((i, j, k))

  # Iterate over all triplets and check for strings having required lengths.
  for i, j, k in triplets_with_sum_18:
    for s1 in word_lengths[i]:
      for s2 in word_lengths[j]:
        for s3 in word_lengths[k]:
            string = s1 + ' ' + s2 + ' ' + s3
            if hashlib.md5(string).hexdigest() in expected_hash:
              print string

def main():
  string = 'poultry outwits ants'
  hash_values = (
    'e4820b45d2277f3844eac66c903e84be',
    '23170acc097c24edb98fc5488ab033fe',
    '665e5bcb0c20062fe8abaaf4628bb154'
  )
  string_anagram_with_given_md5hash(string, len(string), hash_values)


if __name__ == '__main__':
  main()
