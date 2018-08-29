#!/usr/bin/python

# Date: 2018-08-11
#
# Description:
# Print all prime numbers from 1 to n.
#
# Approach:
# Basic idea used is "All non prime numbers are divisible by a prime number".
# Taken a boolean list to store status of all numbers from 1 to n and traversed
# the list with each prime numbers. At each multiple of prime number set index
# to false as they can't be prime because they are multiple of a prime number.
#
# Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#
# Complexity:
# Time: O(sqrt(n)*log(log(n))), Space: O(n)

def crossOff(primeNumbers, prime):
  """Sets indexes of non prime numbers (multiples of 'prime') as false.

  Args:
    primeNumbers: List having true and false.
    prime: Prime Number.
  """
  idx = prime*prime
  while idx < len(primeNumbers):
    primeNumbers[idx] = False
    idx += prime

def getNextPrime(primeNumbers, prime):
  """Fetches and returns next prime number from primeNumbers list.

  Args:
    primeNumbers: List having true and false.
    prime: Prime Number.
  """
  nextPrime = prime + 1
  while nextPrime < len(primeNumbers) and (not primeNumbers[nextPrime]):
    nextPrime += 1
  return nextPrime

def sieveOfEratosthenes(n):
  """Prints all prime numbers from 1 to n.

  Args:
    n: Number till where prime numbers are required.
  """
  # Initially assume all numbers are prime.
  primeNumbers = [True for i in range(n + 1)]
  primeNumbers[0] = False
  primeNumbers[1] = False
  prime = 2

  while prime * prime < n:
    crossOff(primeNumbers, prime)
    prime = getNextPrime(primeNumbers, prime)

  # Print all prime numbers.
  for idx in range(n + 1):
    if primeNumbers[idx]:
      print '{prime} '.format(prime=idx)

def main():
  n = input('Enter number: ')
  sieveOfEratosthenes(n)


if __name__ == '__main__':
  main()
