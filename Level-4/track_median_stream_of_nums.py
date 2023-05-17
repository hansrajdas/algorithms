#!/usr/bin/python

# Date: 2020-03-13
#
# Description:
# There is a running stream of numbers, keep track of median.
#
# Approach:
# - We has to maintain smaller half elements in max-heap and larger half of elements to min-heap
# - Keep min-heap equal to max-heap or 1 more element
# - Adding new number:
#   - Always add to min-heap
#   - Take min from min-heap and push to max-heap
#   - If max-heap has more elements, take max from max-heap and push to min-heap
#
# Complexity:
# O(logn) to track new element
# O(1) to get median
#
# Problem link: https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        """
        - We has to maintain smaller half elements in max-heap and larger half of elements to min-heap
        - Keep min-heap equal to max-heap or 1 more element
        - Steps:
          - Always add to min-heap
          - Take min from min-heap and push to max-heap
          - If max-heap has more elements, take max from max-heap and push to min-heap
        """
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        return self.minHeap[0]


obj = MedianFinder()
obj.addNum(1)
assert obj.findMedian() == 1
obj.addNum(3)
assert obj.findMedian() == 2.0
obj.addNum(2)
assert obj.findMedian() == 2
