def solve(nums):
    return 0

def main():
    tc = int(input())
    n = 1
    while tc:
        _ = input()
        nums = [int(i) for i in input().split(' ') if i]
        res = solve(nums)
        print(f'Case #{n}: {res}')
        tc -= 1
        n += 1
        
if __name__ == '__main__':
    main()
