#!/usr/bin/python

# Date: 2020-08-08
#
# Description:
# Implement AVL tree with insert and delete operations.
# AVL tree is a balanced tree in which height of left and right sub trees is
# not more than 1 for every node. This can be achieved by rotating the tree
# after every insert and delete operations if not balanced.
#
# Reference:
# http://www.geeksforgeeks.org/avl-tree-set-1-insertion/
# http://www.geeksforgeeks.org/avl-tree-set-2-deletion/
#
# Complexity:
# All operations can be done in log(n) time complexity in AVL trees.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def height(self, node):
        """Returns height of a node."""
        if node is None:
            return 0
        return node.height

    def get_balance_factor(self, node):
        """Return difference in heights of left and right subtree of node."""
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        """Right rotates given subtree."""
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return x

    def left_rotate(self, x):
        """Left rotates given subtree."""
        y = x.right
        t = y.left

        x.right = t
        y.left = x

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, root, key):
        """Inserts new node in AVL tree."""
        if root is None:
            return Node(key)
        if root.key > key:
            root.left = self.insert(root.left, key)
        elif root.key < key:
            root.right = self.insert(root.right, key)
        else:
            print('Duplicate[%d] key not allowed' % key)
            return root

        root.height = max(self.height(root.left), self.height(root.right)) + 1

        balance_factor = self.get_balance_factor(root)
        print('Balance factor of node %d after inserting %d is %d' % (
            root.key, key, balance_factor))
        if balance_factor > 1:  # Left subtree is heavy
            if key < root.left.key:  # Case 1: Left left case
                return self.right_rotate(root)
            else:  # Case 2: Left right case
                root.left = self.left_rotate(root.left)
                return right_rotate(root)
        elif balance_factor < -1:  # Right subtree is heavy
            if key > root.right.key:  # Case 3: Right right case
                return self.left_rotate(root)
            else:  # Case 4: Right left case
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        else:
            print('Subtree rooted with %d is balanced' % root.key)
        return root

    def find_min(self, root):
        """Returns node with min element in tree."""
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        """Deletes a node from AVL tree."""
        if root is None:
            return root
        if root.key > key:
            root.left = self.delete(root.left, key)
        elif root.key < key:
            root.right = self.delete(root.right, key)
        else:  # Found node to be deleted
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:  # Node to be deleted has both childs
                node = self.find_min(root.right)
                root.key = node.key
                root.right = self.delete(root.right, node.key)

        # After deletion tree is empty
        if root is None:
            return root

        # Update height and balance if not balanced
        root.height = max(self.height(root.left), self.height(root.right)) + 1
        balance_factor = self.get_balance_factor(root)
        print('Balance factor of node %d after inserting %d is %d' % (
            root.key, key, balance_factor))

        if balance_factor > 1:  # Left subtree is heavy
            if key > root.left.key:  # Case 1: Left left
                return self.right_rotate(root)
            else:  # Case 2: Left right
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        elif balance_factor < -1:  # Right subtree is heavy
            if key < root.right.key:  # Case 3: Right right
                return self.left_rotate(root)
            else:  # Case 4: Right left
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        else:
            print('Subtree rooted with %d is balanced' % root.key)
        return root

    def inorder(self, R):
        if R:
            self.inorder(R.left)
            print('%d[%d]' % (R.key, self.get_balance_factor(R)), end=' ')
            self.inorder(R.right)


def main():
    root = None
    avl = AVL()

    for k in range(10, 0, -1):
        print('\nInserting %d' % k)
        root = avl.insert(root, k)

    avl.inorder(root)
    print()

    for k in range(12):
        print('\nDeleting %d' % k)
        root = avl.delete(root, k)
        avl.inorder(root)
        print()

if __name__ == '__main__':
    main()
