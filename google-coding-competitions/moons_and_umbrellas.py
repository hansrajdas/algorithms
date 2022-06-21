def solve(cj, jc, string):
    min_cost = float('inf')
    def get_cost(string):
        cost = 0
        for i in range(len(string) - 1):
            if string[i] == '?' or string[i + 1] == '?':
                return None
            elif string[i] == 'C' and string[i + 1] == 'J':
                cost += cj
            elif string[i] == 'J' and string[i + 1] == 'C':
                cost += jc
        return cost

    def _solve(idx, string):
        nonlocal min_cost
        for i in range(idx, len(string)):
            if string[i] == '?':
                string[i] = 'C'
                _solve(i, string)
                string[i] = 'J'
                _solve(i, string)
                string[i] = '?'
        cost = get_cost(string)
        if cost is not None and cost < min_cost:
            min_cost = cost
    _solve(0, list(string))
    return min_cost

def main():
    tc = int(input())
    n = 1
    while tc:
        data = input().split(' ')
        tc -= 1
        res = solve(int(data[0]), int(data[1]), data[2])
        print(f'Case #{n}: {res}')
        n += 1
        
if __name__ == '__main__':
    main()
