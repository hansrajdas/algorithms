#!/usr/bin/python

# Date: 2021-03-29
#
# Description:
# Implement disjoint sets(union find) data structure.
# Disjoint sets are useful to maintain groups, check for membership and update
# membership
#
# Approach:
# Implemented using arrays
# - parent array keeps parent of an element
# - rank array keeps rank of subset
#
# Find is used to find which group a element belongs to, returns parent of that
# group. This function also does path compression step
#
# Union is used to merge 2 elements to a single group if already not in the
# same group otherwise merges them to single group using rank
#
# References:
# https://www.geeksforgeeks.org/disjoint-set-data-structures/
# https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/unionfind/UnionFind.java
# 
# Complexity:
# Find: O(1) amortised
# Union: O(1)
#
# Space: O(N)


class Disjoint:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]  # All element are parent of itself

    def find(self, p):
        """
        Return parent(subset id) of element p. This can also be done *recursively* which is
        more intuitive - please check other disjoint set programs from the list.
        """
        # Find the root of the component/set
        root = p
        while root != self.parent[root]:
            root = self.parent[root]

        # Compress the path leading back to the root.
        # Doing this operation is called "path compression"
        # and is what gives us amortized time complexity.
        while p != root:
            _next = self.parent[p]
            self.parent[p] = root
            p = _next
        return root 

    def union(self, x, y):
        """Merges element x and y to same group not already in same."""
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:  # Both elements in same set
            return

        # Put smaller ranked item under bigger ranked item if ranks are different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            # If ranks are same, then move y under x (doesn't matter which
            # one goes where) and increment rank of x's tree
            self.parent[yset] = xset
            self.rank[xset] += 1

def main():
    obj = Disjoint(5)
    obj.union(0, 2)
    obj.union(4, 2)
    obj.union(3, 1)

    assert obj.find(4) == obj.find(0)
    assert obj.find(1) != obj.find(0)

if __name__ == '__main__':
    main()
