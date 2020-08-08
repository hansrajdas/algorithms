#!/usr/bin/python

# Date: 2020-08-08
#
# Description:
# - Insert in Binary search tree(BST)
# - Inorder, Preorder, Postorder
# - Search in BST
# - Delete from BST
#
# Reference:
# http://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# http://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
#
# Complexity:
# Insert, search, delete - O(logn)
# Traversal - O(n)
#
# Limitation:
# If BST is not balanced (or skwed trees), it becomes a linked list and all
# operations take O(n) complexity. This problem is handled by balancing trees.
# AVL, Red-black, B trees are examples of balanced trees.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def insert(self, root, key):
        """Inserts new node to BST."""
        if root is None:
            return Node(key)
        if root.key > key:
            root.left = self.insert(root.left, key)
        elif root.key < key:
            root.right = self.insert(root.right, key)
        else:
            print('Duplicates[%d] not allowed in BST' % key)
            return root
        return root

    def inorder(self, root):
        """Performs inorder traversal of BST."""
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        """Performs preorder traversal of BST."""
        if root:
            print(root.key, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        """Performs postorder traversal of BST."""
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=' ')
    
    def search(self, root, key):
        """Searches for key in BST."""
        if root is None:
            return False
        if root.key > key:
            return self.search(root.left, key)
        elif root.key < key:
            return self.search(root.right, key)
        else:
            return True

    def find_min(self, root):
        """Return min element in BST."""
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        """Deletes a node from BST."""
        if root is None:
            return root
        if root.key > key:
            root.left = self.delete(root.left, key)
        elif root.key < key:
            root.right = self.delete(root.right, key)
        else:  # Node found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:  # Both child nodes present, find inorder successor
                tmp = self.find_min(root.right)
                root.key = tmp.key
                root.right = self.delete(root.right, tmp.key)  # Delete inorder successor
        return root

def main():
    root = None
    bst = BST()
    for k in [10, 5, 15, 2, 7, 13, 18, 15]:
        root = bst.insert(root, k)

    bst.inorder(root)  # 2 5 7 10 13 15 18
    print()  # newline

    bst.preorder(root)  # 10 5 2 7 15 13 18
    print()

    bst.postorder(root)  # 2 7 5 13 18 15 10
    print()

    print(bst.search(root, 2))  # True
    print(bst.search(root, 13))  # True
    print(bst.search(root, 20))  # False
    print(bst.search(root, 1))  # False

    print('\nDeleting 10')
    root = bst.delete(root, 10)
    bst.inorder(root)

    print('\n\nDeleting 15')
    root = bst.delete(root, 15)
    bst.inorder(root)

    print('\n\nDeleting 17')
    root = bst.delete(root, 17)  # Node not found
    bst.inorder(root)
    print()


if __name__ == '__main__':
    main()
