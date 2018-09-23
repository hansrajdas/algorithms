#!/usr/bin/python

# Date: 2018-09-23
#
# Description:
# There is a running stream of numbers, keep track of kth largest number.
#
# Approach:
# Implement a min heap of size k as min heap always has smallest element at
# root index or kth largest(as there are k elements in min heap).
# When there is an element smaller than root, we can ignore them as they can't
# contribute to first k elements otherwise we replace that element with root
# and min heapfies again.
#
# Complexity:
# O(k) Space, O(logk) Time


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


def build_heap(a, n):
  """Builds a heap of size n."""
  for idx in range(n/2, -1, -1):
    min_heapify(a, n, idx)


def main():
  min_heap = []
  k = input('Enter k: ')
  while True:
    n = input('Enter next number: ')
    if len(min_heap) < k - 1:
      print 'Kth largest is: None'
      min_heap.append(n)
    elif len(min_heap) == k - 1:
      min_heap.append(n)  # Now length of min_heap list is k
      build_heap(min_heap, k)
      print 'Kth largest is: %d' % min_heap[0]
    else:
      if min_heap[0] < n:
        min_heap[0] = n
        min_heapify(min_heap, k, 0)
      else:
        pass  # Element is smaller than current kth largest, Ignore that
      print 'Kth largest is: %d' % min_heap[0]


if __name__ == '__main__':
  main()


# Output:
# ---------
# Enter k: 3
# Enter next number: 10
# Kth largest is: None
# Enter next number: 2
# Kth largest is: None
# Enter next number: 3
# Kth largest is: 2
# Enter next number: 1
# Kth largest is: 2
# Enter next number: 11
# Kth largest is: 3
# Enter next number: 14
# Kth largest is: 10
# Enter next number: 13
# Kth largest is: 11
# Enter next number: 0
# Kth largest is: 11
# Enter next number: 50
# Kth largest is: 13
