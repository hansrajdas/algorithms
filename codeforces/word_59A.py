def solve(inp):
    upper = lower = 0
    for c in inp:
        if c < 'a':
            upper += 1
        else:
            lower += 1
    if upper > lower:
        return inp.upper()
    return inp.lower()

def main():
    inp = input()
    print(solve(inp))
        
if __name__ == '__main__':
    main()
