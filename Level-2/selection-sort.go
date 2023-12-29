/*
Date: 2023-12-29

Description:
Implement selection sort.

Approach:
Finds index of minimum (when sorting in ascending) element from the remaining
array and swap it with element at the end of sorted sub-array.
While sorting in ascending order minimum element reaches at first place after
first iteration of outer loop.

Complexity:
O(n^2)
*/

package main

import (
	"fmt"
	"reflect"
)

// Sorts slice in increasing order using selection sort.
func selectionSort(nums []int) {
	for i := 0; i < len(nums); i++ {
		minIdx := i
		for j := i + 1; j < len(nums); j++ {
			// For sorting in descending order, find maxIdx.
			if nums[j] < nums[minIdx] {
				minIdx = j
			}
		}
		nums[minIdx], nums[i] = nums[i], nums[minIdx]
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
		selectionSort(inputCopy)
		if !reflect.DeepEqual(inputCopy, tc.expected) {
			fmt.Printf("\nTC %d failed. Expected %v, got %v", idx, tc.expected, inputCopy)
		}
	}
}
