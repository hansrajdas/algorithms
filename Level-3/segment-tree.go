/*
Date: 2024-08-16

Description
-----------
Implement segment tree with `update` and `sumRange` support.

Approach
--------
Segment tree is 1-indexed array based tree data structure like heap.
N leaf nodes are same as array and parent contains result of operation (sum in this case, can be
anything) of left and right child.

For parent p, left and right child will be at 2*p and 2*p + 1 respectively. Below we have
implemented iterative way, each function doc has implementation detail.

Complexity
----------
Implementing segment tree takes O(2*N) => O(N) space complexity, time complexties of
different operations are listed below:
- Build: O(N)
- Update: O(logN)
- Query: O(logN), sumRange in this case, can be any other operation also

Reference
---------
- https://codeforces.com/blog/entry/18051
  - `build` and `update` function
- https://leetcode.com/problems/range-sum-query-mutable/solution/ [Approach 3 - Segment tree]
  - `sumRange` function
- For video explanation: https://www.youtube.com/watch?v=8CuVOdIWLfA
*/

package main

import "fmt"

type SegmentTree struct {
	tree []int
	n    int
}

// Builds segment tree using nums.
//
// Segment tree has 2N - 1 elements, N leaf elements are same as array elements and N - 1
// elements are internal nodes which hold sum (or any other operation result like min, max,
// xor, etc.) of it's child elements. So in segment tree left child is at index 2i and right
// child at index 2i + 1 for parent at index i.
//
// Also, segment tree is 1-indexed array so 0th position of segment tree is not used - notice
// the loop conditions in build and updated methods.
func newSegmentTree(nums []int) *SegmentTree {
	sg := &SegmentTree{
		tree: make([]int, len(nums)),
		n:    len(nums),
	}
	sg.tree = append(sg.tree, nums...)
	for i := len(nums) - 1; i > 0; i-- {
		sg.tree[i] = sg.tree[i<<1] + sg.tree[i<<1|1]
	}
	return sg
}

// Updates segment tree with new value (replaces) at index pos (original array position).
//
// It first updates the leaf node with new value then travels back to root updating all
// ancestor nodes.
func (this *SegmentTree) update(index int, val int) {
	index += this.n
	// If we want to perform differential update, we can update below statement with
	// self.tree[pos] += val and rest of tree will be build using this new value.
	this.tree[index] = val
	for index > 1 {
		// XOR operation ensures that RHS always add up to 2i (left child) and 2i + 1 (right
		// child) positions for parent i. XOR will make odd to even and vice versa.
		this.tree[index>>1] = this.tree[index] + this.tree[index^1]
		index >>= 1
	}
}

// Returns sum of elements from range left to right (both index included).
//
// Start from the leaf boundary and check if
// - Current left node is right child (at 2i + 1) then we are NOT interested in it's parent
// as it will be fall outside the range so we add left node to res and increment left such
// that half of it goes one next parent
// - Similarly, If right node is left child (at 2i) then we are NOT interested in it's parent
// as it will be fall outside the range so we add right node to res and decrement right such
// that half of it goes to one previous parent
//
// Note: To better understand this function, take an example to draw tree. Make sure to use
// index from 1 instead of 0.
func (this *SegmentTree) sumRange(left int, right int) int {
	res := 0
	left += this.n
	right += this.n
	for left <= right {
		// Check if left is right child (2i + 1 = odd) of its parent
		if left&1 == 1 {
			res += this.tree[left]
			left += 1
		}
		// Check if right is left child (2i = even) of its parent
		if right&1 == 0 {
			res += this.tree[right]
			right -= 1
		}
		left >>= 1
		right >>= 1
	}
	return res
}

func main() {
	// TC-1
	nums := []int{2, 4, 5, 7}
	s := newSegmentTree(nums)
	fmt.Println(s.sumRange(0, len(nums)-1)) // 18
	fmt.Println(s.sumRange(1, 2))           // 9

	// TC-2
	nums = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
	s = newSegmentTree(nums)
	fmt.Println(s.sumRange(1, 3))                     // 9
	s.update(2, 1)                                    // Replaces 3 by 1 at position 2
	fmt.Println(s.sumRange(1, 3))                     // 7
	fmt.Println(s.sumRange(0, 0))                     // 1
	fmt.Println(s.sumRange(len(nums)-1, len(nums)-1)) // 12
	fmt.Println(s.sumRange(0, len(nums)-1))           // 76
}
