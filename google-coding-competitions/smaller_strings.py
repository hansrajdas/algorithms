def is_palindrome(ls):
    left = 0
    right = len(ls) - 1
    while left < right:
        if ls[left] != ls[right]:
            return False
        left += 1
        right -= 1
    return True

def solve(n, k, s):
    count = 0
    def compute(values):
        nonlocal count
        for v in range(97, 97 + k):
            if len(values) == len(s):
                if  ''.join(values) < s and is_palindrome(values):
                    count += 1
                break
            values.append(chr(v))
            compute(values)
            values.pop()
    values = []
    compute(values)
    return count

            

def main():
    tc = int(input())
    tc_num = 1
    while tc:
        n, k = input().split(' ')
        s = input()
        res = solve(int(n), int(k), s)
        print(f'Case #{tc_num}: {res}')
        tc -= 1
        tc_num += 1
        
if __name__ == '__main__':
    main()
