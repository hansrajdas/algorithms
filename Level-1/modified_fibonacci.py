def get_nth_fibonacci(a, b, n):
    count = 0
    if n < 2:
      print 'Input is invalid, n should be more than 1.'
      return

    while count < n - 2:
      res = a + b*b
      a = b
      b = res
      count += 1

    print res

def main():
    inp = raw_input()

    list_input = inp.split(' ')

    return get_nth_fibonacci(int(list_input[0]),
                             int(list_input[1]),
                             int(list_input[2]))


if __name__  == "__main__":
    main()
