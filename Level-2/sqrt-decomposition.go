/*
Date: 2024-08-15

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
*/

package main

import (
	"fmt"
	"math"
)

type SqrtDecomposition struct {
	nums      []int
	blockSize int
	blocks    []int
}

// Intializes blocks of size sqrt(n) with sum of elememts within that block.
func newSqrtDecomposition(nums []int) *SqrtDecomposition {
	sqrtd := &SqrtDecomposition{
		nums:      nums,
		blockSize: int(math.Ceil(math.Sqrt(float64(len(nums))))),
	}
	sqrtd.blocks = make([]int, sqrtd.blockSize)

	blockIdx := -1
	for i, num := range sqrtd.nums {
		if i%sqrtd.blockSize == 0 {
			blockIdx += 1
		}
		sqrtd.blocks[blockIdx] += num
	}
	return sqrtd
}

// Updates idx with new value `val`.
func (this *SqrtDecomposition) update(index int, val int) {
	this.blocks[index/this.blockSize] += val - this.nums[index]
	this.nums[index] = val
}

// Returns sum of elements from index range left to right (both index included).
func (this *SqrtDecomposition) query(left int, right int) int {
	sum, i := 0, left
	for i <= right {
		// Calculating sum of all complete blocks - traversing whole block at once.
		if i%this.blockSize == 0 && i+this.blockSize-1 <= right {
			sum += this.blocks[i/this.blockSize]
			i += this.blockSize
		} else {
			sum += this.nums[i] // Sum of nums falling outside of complete blocks.
			i += 1
		}
	}
	return sum
}

func main() {
	// TC-1
	nums := []int{2, 4, 5, 7}
	s := newSqrtDecomposition(nums)
	fmt.Println(s.query(0, len(nums)-1)) // 18
	fmt.Println(s.query(1, 2))           // 9

	// TC-2
	nums = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
	s = newSqrtDecomposition(nums)
	fmt.Println(s.query(1, 3))                     // 9
	s.update(2, 1)                                 // Replaces 3 by 1 at position 2
	fmt.Println(s.query(1, 3))                     // 7
	fmt.Println(s.query(0, 0))                     // 1
	fmt.Println(s.query(len(nums)-1, len(nums)-1)) // 12
	fmt.Println(s.query(0, len(nums)-1))           // 76
}
