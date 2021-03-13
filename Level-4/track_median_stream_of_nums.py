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
#     - Always add to min-heap
#     - Take min from min-heap and push to max-heap
#     - If max-heap has more elements, take max from max-heap and push to min-heap
#
# https://leetcode.com/problems/find-median-from-data-stream/submissions/
#
# Complexity:
# O(logn) to track new element
# O(1) to get median


import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        """
        - We has to maintain smaller half elements in max-heap and larger half of elements to min-heap
        - Keep min-heap equal to max-heap or 1 more element
        - Steps:
            - Always add to min-heap
            - Take min from min-heap and push to max-heap
            - If max-heap has more elements, take max from max-heap and push to min-heap
        """
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return self.min_heap[0]


obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())  # 1
obj.addNum(3)
print(obj.findMedian())  # 2.0
obj.addNum(2)
print(obj.findMedian())  # 2
