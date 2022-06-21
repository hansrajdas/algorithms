def solve(g):
    prefix = 0
    m = {}
    count = 0
    for i in range(1, g + 1):
        prefix += i
        if prefix == g:
            count += 1
        if prefix - g in m:
            count += m[prefix - g]
        if prefix not in m:
            m[prefix] = 0
        m[prefix] += 1
    return count

def main():
    tc = int(input())
    n = 1
    while tc:
        g = int(input())
        res = solve(g)
        print(f'Case #{n}: {res}')
        tc -= 1
        n += 1
        
if __name__ == '__main__':
    main()
