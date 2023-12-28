/*
Date: 2018-09-08

Description:
Implement bubble sort.

Approach:
Compares adjacent elements and pushes to it's extreme end. While
sorting in ascending order largest element reaches at last place after first
iteration of outer loop. For descending smallest reaches to the last place.

Complexity:
O(n^2)
*/

package main

import (
	"fmt"
	"reflect"
)

func bubbleSort(nums []int) {
	swap := true
	for i := 0; i < len(nums); i++ {
		swap = false
		for j := 0; j < len(nums)-1-i; j++ {
			if nums[j] > nums[j+1] { // For descending order, reverse this condition.
				nums[j], nums[j+1] = nums[j+1], nums[j]
				swap = true
			}
		}
		if !swap {
			break
		}
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
		bubbleSort(inputCopy)
		if !reflect.DeepEqual(inputCopy, tc.expected) {
			fmt.Printf("\nTC %d failed. Expected %v, got %v", idx, tc.expected, inputCopy)
		}
	}
}
