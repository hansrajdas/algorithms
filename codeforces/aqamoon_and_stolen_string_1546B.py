def solve(s, n):
    res = [0] * len(s[0])
    for i in range(2*n - 1):
        for index, c in enumerate(s[i]):
            res[index] ^= ord(c)
    return ''.join(chr(c) for c in res)

def main():
    tc = int(input())
    while tc:
        n, m = [int(x) for x in input().split(' ')]
        i = 0
        s = []
        while i < n * 2 - 1:
            s.append(input().strip())
            i += 1
        print(solve(s, n), flush=True)
        tc -= 1
        
if __name__ == '__main__':
    main()
