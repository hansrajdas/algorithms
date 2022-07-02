#!/usr/bin/python

"""
Date: 2022-06-29

Description
-----------
Implement binary indexed tree (fenwick tree) with `update` and `sumRange` support.

Approach
--------
BIT is implemeted using an 1-indexed array. Each element is responsible for other elements below
it. The position of the set LSB determines the range of responsibility that cell has to the cells
below itself. If set LSB is at position 0 (like 11 -> 1011) so this index is responsible for
2^0 = 1 cell (itself) only.

Complexity
----------
- Build: O(N) time and space
- Update: O(logN)
- sumRange: O(logN)

Reference
---------
https://leetcode.com/discuss/general-discussion/1093346/introduction-to-fenwick-treebinary-indexed-treebit
"""

class BIT:

    @staticmethod
    def _RSB(i):
        """Returns right most set bit position of a number."""
        return i & -i

    def __init__(self, nums):
        """Builds BIT for given list of numbers `nums`."""
        self.n = len(nums) + 1
        self.tree = [0] + nums
        for child in range(1, self.n):
            parent = child + self._RSB(child)
            if parent < self.n:
                self.tree[parent] += self.tree[child]

    def _increase(self, index, toAdd):
        """Adds `toAdd` at given index."""
        # 1-based indexing so add one here to the original 0-index passed. Another way to
        # remember is if we pass index as 0, below loop will never end (stuck in infinite loop)
        index += 1
        while index < self.n:
            self.tree[index] += toAdd
            index += self._RSB(index)

    def _prefixSum(self, index):
        """Returns prefix sum till given `index` (inclusive)."""
        ans = 0
        while index != 0:
            ans += self.tree[index]
            index -= self._RSB(index)
        return ans

    def update(self, pos: int, val: int) -> None:
        """
        Updates (replace) element at index `pos` with `val`.
        BIT doesn't support replacing element at specific index, it supports adding differential
        at a index so:
        - First we need to get actual element using `sumRange` and find the difference then
        - Use `increase` method to add differential to that index
        """
        currentVal = self.sumRange(pos, pos)
        self._increase(pos, val - currentVal)

    def sumRange(self, left: int, right: int) -> int:
        """Returns sum of elements from index left to right (both inclusive)."""
        return self._prefixSum(right + 1) - self._prefixSum(left)

def main():
    # TC - 1
    a = [2, 4, 5, 7]
    b = BIT(a)
    assert b.sumRange(0, 3) == sum(a)

    # TC - 2
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    b = BIT(a)
    assert b.sumRange(1, 3) == sum(a[1:4])
    b.update(2, 1)  # Replaces 3 by 1 at position 2
    assert b.sumRange(1, 3) == 7
    assert b.sumRange(0, 0) == 1
    assert b.sumRange(len(a) - 1, len(a) - 1) == 12
    assert b.sumRange(0, len(a) - 1) == 76

if __name__ == '__main__':
    main()
