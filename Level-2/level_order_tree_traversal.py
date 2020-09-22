# Date: 2020-09-22
#
# Dessciption:
# Print level order traversal of binary tree
#
# Approach:
# Find height of tree and traverse recursively printing left and right node
# for each level starting from top(level 1)
#
# Complexity:
# Time: Worst case would be O(n^2), in case of skewed tree
# Space: O(1)
#
# Refer: Level-2/level_order_tree_traversal_using_queue.c


class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


def get_tree_height(root):
    if root is None:
        return 0
    return 1 + max(get_tree_height(root.left), get_tree_height(root.right))


def level_order_traversal(root):
    height = get_tree_height(root)
    print('Height of tree: %d' % height)
    for h in range(height):
        print_given_level(root, h)
    print()


def print_given_level(root, height):
    if root is None:
        return
    if not height:
        print(root.data, end=' ')
        return
    print_given_level(root.left, height - 1)
    print_given_level(root.right, height - 1)


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
# Height of tree: 4
# 1 2 3 4 5 6
