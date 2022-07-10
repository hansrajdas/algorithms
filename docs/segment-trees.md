## Segment trees
- Used for answering range queries like sum of numbers from `A[i:j]`
- Complexities
  - Build: O(N)
  - Query: O(logN)
  - Update an element: O(logN)
  - Space: O(2N) => O(N)
- Segment trees are binary trees over array where each internal node has exactly 2 children
- _Lazy propagation_ (for range update) skipped

### Implementation
- https://github.com/hansrajdas/algorithms/blob/master/Level-3/segment-tree.py

### References
- https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
