#!/usr/bin/python

# Date: 2018-09-23
#
# Description:
# Find GCD(or HCF) and LCM of 2 numbers.

def gcd(a, b):
  return gcd(b, a % b) if b else a


def main():
  a = input('Enter first number: ')
  b = input('Enter second number: ')
  
  g = gcd(a, b)
  print 'GCD is: %d' % g

  l = (a * b) / g  # Because a*b = lcm*hcf
  print 'LCM is: %d' % l


if __name__ == '__main__':
  main()
