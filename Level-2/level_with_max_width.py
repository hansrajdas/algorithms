# Date: 2020-09-26
#
# Description:
# Find the level in tree which has maximum nodes/width.
#
# Approach:
# Do a level order traversal and add all nodes below the current level in
# queue. In each traversal pop all elements currently present in the queue so
# that queue is left with elements that are present just below current level.
# We can take the count of number of nodes present currently in queue and
# compare with previous result, if smaller we can update result.
#
# Complexity:
# O(n), n = number of nodes in tree.

import collections

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_with_max_width(root):
    if root is None:
        return (0, 0)
    q = collections.deque([root])
    max_nodes = 0
    max_node_level = 0
    level = -1
    while q:
        level += 1
        size = len(q)
        if max_nodes < size:
            max_node_level = level
            max_nodes = size
        while size:
            size -= 1
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return (max_nodes, max_node_level)

def main():
  # Level 0
  root = Node(1)

  # Level 1
  root.left = Node(2)
  root.right = Node(3)

  # Level 2
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.left = Node(6)
  root.right.right = Node(7)

  # Level 3
  root.left.left.left = Node(8)

  max_nodes, level = level_with_max_width(root)
  print('Max nodes: %d at level: %d' % (max_nodes, level))


if __name__ == '__main__':
    main()


# Output
# ------
# Max nodes: 4 at level: 2
