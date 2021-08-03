import itertools

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

def solve(n, expected_cost):
    if expected_cost > n * n:
        return 'IMPOSSIBLE'
    nums = [i for i in range(1, n + 1)]
    perms = itertools.permutations(nums)
    for perm in perms:
        cost = 0
        ls = list(perm)
        for i in range(len(ls) - 1):
            j = get_min(ls, i)
            reverse(ls, i, j)
            cost += j - i + 1
        if cost == expected_cost:
            return ' '.join(str(n) for n in perm)
    return 'IMPOSSIBLE'

def main():
    tc = int(input())
    n = 1
    while tc:
        data = input().split(' ')
        res = solve(int(data[0]), int(data[1]))
        print(f'Case #{n}: {res}')
        tc -= 1
        n += 1
        
if __name__ == '__main__':
    main()
