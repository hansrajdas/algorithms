def solve(inp):
    return 0

def main():
    tc = int(input())
    while tc:
        _ = int(input())
        nums = [int(x) for x in input().split(' ')]
        print(solve(nums))
        tc -= 1
        
if __name__ == '__main__':
    main()
