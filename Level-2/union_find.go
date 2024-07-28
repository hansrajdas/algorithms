/*
Date: 2024-07-28

Description:
Implement disjoint sets(union find) data structure.
Disjoint sets are useful to maintain groups, check for membership and update
membership

Approach:
Implemented using arrays
- parent array keeps parent of an element
- rank array keeps rank of subset

Find is used to find which group a element belongs to, returns parent of that
group. This function also does path compression step

Union is used to merge 2 elements to a single group if already not in the
same group otherwise merges them to single group using rank

References:
https://www.geeksforgeeks.org/disjoint-set-data-structures/
https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/unionfind/UnionFind.java

Complexity:
Find: O(1) amortised
Union: O(1)

Space: O(N)
*/

package main

import "fmt"

type UnionFind struct {
	rank   []int
	parent []int
}

func newUnionFind(n int) *UnionFind {
	u := &UnionFind{}
	for i := 0; i < n; i++ {
		u.rank = append(u.rank, 0)
		u.parent = append(u.parent, i) // All element are parent of itself
	}
	return u
}

// Recursive method of find with path compression. This is same as iterative
// approach implemented here: Level-2/graph_cycle_detection_union_find.py.
// However recursive is more intuitive and readable.
func (u *UnionFind) find(x int) int {
	if u.parent[x] != x {
		u.parent[x] = u.find(u.parent[x]) // Path compression
	}
	return u.parent[x]
}

// Merges element x and y to same group not already in same.
func (u *UnionFind) union(x, y int) {
	xset, yset := u.find(x), u.find(y)
	if xset == yset { // Both elements in same set
		return
	}

	// Put smaller ranked item under bigger ranked item if ranks are different
	if u.rank[xset] < u.rank[yset] {
		u.parent[xset] = yset
	} else if u.rank[xset] > u.rank[yset] {
		u.parent[yset] = xset
	} else {
		// If ranks are same, then move y under x (doesn't matter which
		// one goes where) and increment rank of x's tree
		u.parent[yset] = xset
		u.rank[xset] += 1
	}
}

func main() {
	u := newUnionFind(5)
	u.union(0, 2)
	u.union(4, 2)
	u.union(3, 1)

	fmt.Printf("4->%d, 0->%d\n", u.find(4), u.find(0)) // 4->0, 0->0
	fmt.Printf("1->%d, 0->%d\n", u.find(1), u.find(0)) // 1->3, 0->0
}
