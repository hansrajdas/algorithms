def solve(inp):
    n = len(inp)
    S = sum(inp)
    if S >= n:
        return S - n
    return 1

def main():
    tc = int(input())
    while tc:
        _ = int(input())
        nums = [int(x) for x in input().split(' ')]
        print(solve(nums))
        tc -= 1
        
if __name__ == '__main__':
    main()
