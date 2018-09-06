def print_next_string(string):
  length = len(string)
  ctr = length

  if length == 1:
    if string == 'z' or string == 'Z':
      print 'no answer'
    else:
      print chr(ord(string) + 1)
    return None

  lis = list(string)
  while ctr > 1:
    if lis[ctr - 1] > lis[ctr - 2]:
      lis[ctr - 1], lis[ctr - 2] = lis[ctr - 2], lis[ctr - 1]
      print ''.join(lis)
      return None
    ctr -= 1
  print 'no answer'
  return None


def main():
  n = input('Enter n: ')

  while n:
    string = raw_input('Enter string: ')
    print_next_string(string)
    n -= 1

if __name__  == "__main__":
    main()
