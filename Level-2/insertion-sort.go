/*
Date: 2023-12-29

Description:
Implement insertion sort.

Approach:
Scans from right in sorted sub-array and inserts current element at correct
place by shifting all the elements to right.

Complexity:
O(n^2)
*/

package main

import (
	"fmt"
	"reflect"
)

// Sorts slice in increasing order using insertion sort.
func insertionSort(nums []int) {
	var j int
	for i := 1; i < len(nums); i++ {
		key := nums[i]
		// Loop until elements are sorted.
		// For decreasing order, reverse the condition.
		for j = i; j > 0 && nums[j-1] > key; j-- {
			nums[j] = nums[j-1]
		}
		nums[j] = key
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
		insertionSort(inputCopy)
		if !reflect.DeepEqual(inputCopy, tc.expected) {
			fmt.Printf("\nTC %d failed. Expected %v, got %v", idx, tc.expected, inputCopy)
		}
	}
}
