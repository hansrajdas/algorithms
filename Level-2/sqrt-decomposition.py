#!/usr/bin/python

"""
Date: 2024-08-14

Description
-----------
Implement Square root decomposition method for range sum queries.

Approach
--------
The main idea behind this technique is that if we divide our array into blocks of sizes sqrt(n),
such that each block has sqrt(n) elements. Then we can reduce the overall time complexity by
avoiding traversing over the whole range.

Complexity
----------
- Build: O(n) time and space
- Query: O(sqrt(n))
- Update: O(1)

Reference
---------
- https://leetcode.com/discuss/study-guide/2432715/Tutorial-or-Square-root-decomposition-or-Dynamic-Range-Query
- https://www.geeksforgeeks.org/square-root-sqrt-decomposition-algorithm/
"""

import math

class SqrtDecomposition:
    def __init__(self, nums):
        """Intializes blocks of size sqrt(n) with sum of elememts within that block."""
        self.nums = nums
        self.blockSize = math.ceil(math.sqrt(len(nums)))
        self.blocks = [0] * self.blockSize

        blockIdx = -1
        for i, num in enumerate(nums):
            if i % self.blockSize == 0:
                blockIdx += 1
            self.blocks[blockIdx] += num

    def update(self, idx, val):
        """Updates idx with new value `val`."""
        blockIdx = idx // self.blockSize
        self.blocks[blockIdx] += val - self.nums[idx]
        self.nums[idx] = val

    def query(self, left, right):
        """
        Returns sum of elements from index range left to right (both index included).
        """
        ans = 0

        i = left
        while i <= right:
            # Calculating sum of all complete blocks - traversing whole block at once.
            if i % self.blockSize == 0 and i + self.blockSize - 1 <= right:
                ans += self.blocks[i // self.blockSize]
                i += self.blockSize
            else:
                ans += self.nums[i]  # Sum of nums falling outside of complete blocks.
                i += 1
        return ans


def main():
    # TC - 1
    a = [2, 4, 5, 7]
    s = SqrtDecomposition(a)
    assert s.query(0, 3) == sum(a)
    assert s.query(1, 2) == sum(a[1:3])

    # TC - 2
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    s = SqrtDecomposition(a)
    assert s.query(1, 3) == sum(a[1:4])
    s.update(2, 1)  # Replaces 3 by 1 at position 2
    assert s.query(1, 3) == 7
    assert s.query(0, 0) == 1
    assert s.query(len(a) - 1, len(a) - 1) == 12
    assert s.query(0, len(a) - 1) == 76

if __name__ == '__main__':
    main()
