/*
Date: 2023-12-30

Description:
Transform an array to max heap and sort in ascending order. Max heap has
largest element at 0th index always. In sorting we can copy 0th index element
to last and run max-heapify again to have next max at 0th index.
So max heap is used to sort array in ascending order and min heap can be used
to sort array in descending order.

Complexity:
Building heap has O(n)
Sorting takes O(n*log(n))
*/

package main

import (
	"fmt"
	"reflect"
)

func maxHeapify(nums []int, n, idx int) {
	largestIdx := idx
	left := 2*idx + 1
	right := 2*idx + 2

	// Select min b/w left and right child if current(i) is not maximum then
	// swap. Compared with left child fist because heap should always be left
	// filled.
	if left < n && nums[left] > nums[largestIdx] {
		largestIdx = left
	}
	if right < n && nums[right] > nums[largestIdx] {
		largestIdx = right
	}

	// If current index element is not largest than it's left and right child
	// then swap current index element with larger element.
	if largestIdx != idx {
		nums[largestIdx], nums[idx] = nums[idx], nums[largestIdx]
		maxHeapify(nums, n, largestIdx)
	}
}

func heapSort(nums []int) {
	// Building max or min heap. Building max or min heap has total complexity of O(n).
	// Refer: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
	// This loop is run from n/2 down to 0 with an assumption that lower level
	// elements (from n/2+1 to n) in heap is already heapfied.
	// Build max heap for sorting in ascending order. For sorting in descending
	// order build min heap and rest remains same.
	for i := len(nums) / 2; i >= 0; i-- {
		maxHeapify(nums, len(nums), i)
	}

	// Sort in ascending order.
	// Swap 0th with last element of heap and then heapify w.r.t to first element.
	for i := len(nums) - 1; i > 0; i-- {
		nums[i], nums[0] = nums[0], nums[i]
		maxHeapify(nums, i, 0)
	}
}

func main() {
	testCases := []struct {
		input, expected []int
	}{
		{input: []int{5, 4, 3, 2, 1, 10, 28, 7, 6}, expected: []int{1, 2, 3, 4, 5, 6, 7, 10, 28}},
		{input: []int{3, 4, 5, 2, 1}, expected: []int{1, 2, 3, 4, 5}},
		{input: []int{3, 4, 5, 2, 1, 6}, expected: []int{1, 2, 3, 4, 5, 6}},
		{input: []int{}, expected: []int{}},
		{input: []int{1}, expected: []int{1}},
		{input: []int{2, 1}, expected: []int{1, 2}},
	}
	for idx, tc := range testCases {
		inputCopy := make([]int, len(tc.input))
		copy(inputCopy, tc.input)
		heapSort(inputCopy)
		if !reflect.DeepEqual(inputCopy, tc.expected) {
			fmt.Printf("\nTC %d failed. Expected %v, got %v", idx, tc.expected, inputCopy)
		}
	}
}
