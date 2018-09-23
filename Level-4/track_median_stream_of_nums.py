#!/usr/bin/python

# Date: 2018-09-23
#
# Description:
# There is a running stream of numbers, keep track of median.
#
# Approach:
# Maintain 2 heaps - One max and one min. Put all smaller half elements in max
# heap and larger half in min heap.
# When new element is streamed - if it is more than previous median then it
# should go in min heap otherwise in max heap.
# Another important point to notice is difference between number of elements in
# both heaps should not exceed 1, need to move elements from min to max or vice
# versa if this is the case.
#
# At any time median will be:
# - Avg of root elements of 2 heaps, if they have number of elements
# - Root element of heap which has one more element.
#
# Algorithm reference:
# https://www.geeksforgeeks.org/median-of-stream-of-running-integers-using-stl/
#
# Complexity:
# O(nlogn) Time, O(n) Space


def min_heapify(a, n, idx):
  """Min heapifies an array of size n w.r.t index idx."""
  min_idx = idx
  left = 2*idx + 1
  right = 2*idx + 2

  if left < n and a[left] < a[min_idx]:
    min_idx = left
  if right < n and a[right] < a[min_idx]:
    min_idx = right

  if min_idx != idx:
    a[min_idx], a[idx] = a[idx], a[min_idx]
    min_heapify(a, n, min_idx)

def max_heapify(a, n, idx):
  """Max heapifies an array of size n w.r.t index idx."""
  max_idx = idx
  left = 2*idx + 1
  right = 2*idx + 2

  if left < n and a[left] > a[max_idx]:
    max_idx = left
  if right < n and a[right] > a[max_idx]:
    max_idx = right

  if max_idx != idx:
    a[max_idx], a[idx] = a[idx], a[max_idx]
    max_heapify(a, n, max_idx)

def main():
  max_heap = []
  min_heap = []
  while True:
    n = input('Enter next number: ')
    if not max_heap:
      median = n
      max_heap.append(n)
    elif len(max_heap) > len(min_heap):
      if n < median:
        # Pop max from max heap and insert in min heap
        min_heap.append(max_heap[0])
        min_heap[0], min_heap[len(min_heap) - 1] = min_heap[len(min_heap) - 1], min_heap[0]
        min_heapify(min_heap, len(min_heap), 0)

        # Insert n in max_heap
        max_heap[0] = n
        max_heapify(max_heap, len(max_heap), 0)
      else:
        # Insert in min heap
        min_heap.append(n)
        min_heap[0], min_heap[len(min_heap) - 1] = min_heap[len(min_heap) - 1], min_heap[0]
        min_heapify(min_heap, len(min_heap), 0)

      median = (max_heap[0] + min_heap[0]) / 2.0
    elif len(max_heap) < len(min_heap):
      if n > median:
        # Pop min from min heap and insert in max heap
        max_heap.append(min_heap[0])
        max_heap[0], max_heap[len(max_heap) - 1] = max_heap[len(max_heap) - 1], max_heap[0]
        max_heapify(max_heap, len(max_heap), 0)

        # Insert n in min heap
        min_heap[0] = n
        min_heapify(min_heap, len(min_heap), 0)
      else:
        # Insert in max heap
        max_heap.append(n)
        max_heap[0], max_heap[len(max_heap) - 1] = max_heap[len(max_heap) - 1], max_heap[0]
        max_heapify(max_heap, len(max_heap), 0)

      median = (max_heap[0] + min_heap[0]) / 2.0
    elif len(max_heap) == len(min_heap):
      if n > median:
        # Insert in min heap
        min_heap.append(n)
        min_heap[0], min_heap[len(min_heap) - 1] = min_heap[len(min_heap) - 1], min_heap[0]
        min_heapify(min_heap, len(min_heap), 0)

        median = min_heap[0]
      else:
        # Insert in max heap
        max_heap.append(n)
        max_heap[0], max_heap[len(max_heap) - 1] = max_heap[len(max_heap) - 1], max_heap[0]
        max_heapify(max_heap, len(max_heap), 0)

        median = max_heap[0]

    print 'Median is: %f' % median


if __name__ == '__main__':
  main()


# Output:
# -------
# Enter next number: 20
# Median is: 20.000000
# Enter next number: 22
# Median is: 21.000000
# Enter next number: 1
# Median is: 20.000000
# Enter next number: 21
# Median is: 20.500000
# Enter next number: 5
# Median is: 20.000000
