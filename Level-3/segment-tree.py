# Reference:
# - https://codeforces.com/blog/entry/18051
#   - `build` and `update` function
# - https://leetcode.com/problems/range-sum-query-mutable/solution/ [Approach 3 - Segment tree]
#   - `sumRange` function
# - For video explanation: https://www.youtube.com/watch?v=8CuVOdIWLfA

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * self.n + nums
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, pos: int, val: int) -> None:
        pos += self.n
        self.tree[pos] = val
        while pos > 1:
            self.tree[pos >> 1] = self.tree[pos] + self.tree[pos ^ 1]
            pos >>= 1

    def sumRange(self, left: int, right: int) -> int:
        import pdb;pdb.set_trace()
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            # Check if left is right child (2i + 1 = odd) of its parent
            if left & 1:
                res += self.tree[left]
                left += 1

            # Check if right is left child (2i = even) of its parent
            if not (right & 1):
                res += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return res

def main():
    # TC - 1
    a = [2, 4, 5, 7]
    s = SegmentTree(a)
    print(s.sumRange(0, 3))

    # TC - 2
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    s = SegmentTree(a)
    print(s.sumRange(1, 3))
    s.update(2, 1)
    print(s.sumRange(1, 3))
    print(s.sumRange(0, 0))
    print(s.sumRange(len(a) - 1, len(a) - 1))
    print(s.sumRange(0, len(a) - 1))

if __name__ == '__main__':
    main()
