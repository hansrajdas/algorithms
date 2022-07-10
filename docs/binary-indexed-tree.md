## Binary indexed tree (BIT) or fenwick tree
- For answering range queries using prefix sum
- Complexity
  - Build: O(N) time and space
  - Point update: O(logN)
  - Range update: O(logN)
  - Range sum: O(logN)
- Can’t add new element or remove an element from the array
- FT is `1-based` array
- Unlike regular array, in a FT a specific cell is responsible for other cells as well
- The position of the set LSB determines the range of responsibility that cell has to the cells below itself
- If set LSB is at position 0 (like 11 -> 1011) so this index is responsible for 2^0 = 1 cell (itself) only
- In FT we may compute prefix sum upto a certain index, which ultimately lets us perform range sum queries
- _FT can’t be used for other operations_ like min, max, xor directly like with segment tree as FT works on prefix. For range sum, it’s possible to get using `prefixSum(r + 1) - prefixSum(l)`
- _Range update_ is skipped

### Implementation
- https://github.com/hansrajdas/algorithms/blob/master/Level-3/binary-indexed-tree.py

### References
- 4 WilliamFiset lectures: https://www.youtube.com/playlist?list=PLDV1Zeh2NRsCvoyP-bztk6uXAYoyZg_U9
- https://leetcode.com/discuss/general-discussion/1093346/introduction-to-fenwick-treebinary-indexed-treebit
