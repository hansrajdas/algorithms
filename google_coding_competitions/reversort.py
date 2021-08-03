def get_min(nums, start):
    mn = start
    for i in range(start, len(nums)):
        if nums[i] < nums[mn]:
            mn = i
    return mn

def reverse(nums, left, right):
    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def solve(nums):
    cost = 0
    for i in range(len(nums) - 1):
        j = get_min(nums, i)
        reverse(nums, i, j)
        cost += j - i + 1
    return cost

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
