# Date: 2020-09-22
#
# Description:
# Level order traversal of tree
#
# Approach:
# Uses DFS traversal approach.
# 1. Prints current node data.
# 2. enqueue's both left and right child.
# 3. dequeue a node from queue.
# 4. Execute while queue is not empty.
#
# Reference:
# https://www.geeksforgeeks.org/?p=2686
#
# Complexity:
# Time: O(n), n is number of node in tree
# Space: O(n), Requires extra space to maintain queue

import collections


class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


def level_order_traversal(root):
    Q = collections.deque()
    Q.append(root)
    while Q:
        node = Q.popleft()
        if node.left:
            Q.append(node.left)
        if node.right:
            Q.append(node.right)
        print(node.data, end=' ')
    print()


def main():
    root = Node(1);
    root.left = Node(2);
    root.right = Node(3);

    root.left.left = Node(4);
    root.left.right = Node(5);

    root.left.left.left = Node(6);

    level_order_traversal(root)


if __name__ == '__main__':
    main()

# Output
# -----------------
# 1 2 3 4 5 6
