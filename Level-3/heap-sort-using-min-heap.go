/*
Date: 2023-12-30

Description:
Transform an array to min heap and sort in descending order. Min heap has
smallest element at 0th index always. In sorting we can copy 0th index
element to last index and run min-heapify again to have next min at 0th
index.
So min heap is used to sort array in descending order and max heap can be
used to sort array in ascending order.

Complexity:
Building heap has O(n)
Sorting takes O(n*log(n))
*/

package main

import (
	"fmt"
	"reflect"
)

func minHeapify(nums []int, n, idx int) {
	smallestIdx := idx
	left := 2*idx + 1
	right := 2*idx + 2

	// Check if current element is smaller than it's left and right child.
	// If not take index of smaller element between left and right child as
	// smallest index. Also smaller among left and right child should become parent
	// of current node so 2 if used instead of if..else if.
	if left < n && nums[left] < nums[smallestIdx] {
		smallestIdx = left
	}
	if right < n && nums[right] < nums[smallestIdx] {
		smallestIdx = right
	}

	// If current index element is not smallest than it's left and right child
	// then swap current index element with smaller element.
	if smallestIdx != idx {
		nums[smallestIdx], nums[idx] = nums[idx], nums[smallestIdx]
		minHeapify(nums, n, smallestIdx)
	}
}

func heapSort(nums []int) {
	// Building max or min heap. Building max or min heap has total complexity of O(n).
	// Refer: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
	// This loop is run from n/2 down to 0 with an assumption that lower level
	// elements (from n/2+1 to n) in heap is already heapfied.
	// Build min heap for sorting in descending order. For sorting in ascending
	// order build max heap and rest remains same.
	for i := len(nums) / 2; i >= 0; i-- {
		minHeapify(nums, len(nums), i)
	}

	// Sort in descending order.
	// Swap 0th with last element of heap and then heapify w.r.t to first element.
	for i := len(nums) - 1; i > 0; i-- {
		nums[i], nums[0] = nums[0], nums[i]
		minHeapify(nums, i, 0)
	}
}

func main() {
	testCases := []struct {
		input, expected []int
	}{
		{input: []int{5, 4, 3, 2, 1, 10, 28, 7, 6}, expected: []int{28, 10, 7, 6, 5, 4, 3, 2, 1}},
		{input: []int{3, 4, 5, 2, 1}, expected: []int{5, 4, 3, 2, 1}},
		{input: []int{3, 4, 5, 2, 1, 6}, expected: []int{6, 5, 4, 3, 2, 1}},
		{input: []int{}, expected: []int{}},
		{input: []int{1}, expected: []int{1}},
		{input: []int{2, 1}, expected: []int{2, 1}},
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
