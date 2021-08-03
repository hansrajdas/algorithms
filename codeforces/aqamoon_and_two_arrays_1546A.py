def solve(a, b):
    if sum(a) != sum(b):
        print(-1)
        return -1

    for i in range(len(a)):
        if a[i] != b[i]:
            break
    else:
        print(0)
        return 0

    pos = {}
    neg = {}
    for i in range(len(a)):
        if b[i] - a[i] > 0:
            pos[i] = b[i] - a[i]
        elif b[i] - a[i] < 0:
            neg[i] = b[i] - a[i]

    resp = []
    for i in pos:
        resp.extend([i] * pos[i])

    resp2 = []
    for j in neg:
        resp2.extend([j] * abs(neg[j]))

    print(len(resp))
    for i in range(len(resp)):
        print(resp2[i] + 1, resp[i] + 1)

def main():
    tc = int(input())
    while tc:
        _ = int(input())
        a = [int(x) for x in input().split(' ')]
        b = [int(x) for x in input().split(' ')]
        solve(a, b)
        tc -= 1
        
if __name__ == '__main__':
    main()
