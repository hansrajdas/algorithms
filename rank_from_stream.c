/*
 * Date: 2018-07-26
 *
 * Description:
 * Imagine you are reading in a stream of integers. Periodically, you wish to be
 * able to look up the rank of a number x (the number of values less than or
 * equal to x). Implement the data structures and algorithms to support these
 * operations. That is, implement the method track(int x), which is called when
 * each number is generated, and the method getRankOfNumber(int x), which
 * returns the number of values less than or equal to x (not including x
 * itself).
 * EXAMPLE
 * Stream (in order of appearance) : 5, 1, 4, 4, 5, 9, 7, 13, 3
 * getRankOfNumber(1) = 0
 * getRankOfNumber(3) = 1
 * getRankOfNumber(4) = 3
 *
 * Implementation:
 * Requirement is just to store the elements in sorted order and return index of
 * the item whose rank is required but as items are generated periodically,
 * using an array would be costly as shifting would be required to insert new
 * element at correct(to maintain sorted order) place.
 *
 * So to overcome this problem we can use binary search tree and store
 * additional info (number of nodes in left sub tree, left_size) with data.
 * We can track and update left_size of each node on every insert operation with
 * below approach while inserting in BST:
 * - Increment parent node's left_size if next element needs to be inserted in
 *   left sub tree.
 *
 * While fetching rank we just have to add left_size when traversing in right
 * sub tree.
 *
 * Complexity:
 * Insert: O(log(n)), find rank: O(log(n)) 
 */

#include "stdio.h"
#include "stdlib.h"

typedef struct NODE {
  int data;
  int left_size;  // Number of nodes in left sub tree.
  struct NODE *left, *right;
} NODE;

NODE *new_node(int x) {
  NODE *node = (NODE *)malloc(sizeof(NODE));
  node->data = x;
  node->left_size = 0;
  node->left = NULL;
  node->right = NULL;
  return node;
}

/*
 * Inserts a new node in BST. Also increments size of left sub tree when new
 * element is going to insert in left sub tree of a node.
 *
 * root: Root pointer of tree.
 * x: New element.
 */
NODE* track(NODE *root, int x) {
  if (root == NULL) {
    return new_node(x);
  } else {
    if (root->data == x) {
      root->left_size++;
    } else if (root->data < x) {
      root->right = track(root->right, x);
    } else {
      root->left_size++;
      root->left = track(root->left, x);
    }
  }
  return root;
}

/*
 * Finds rank of an element from BST. Keeps on adding size of left sub tree when
 * searching in right part.
 *
 * root: Root pointer of tree.
 * x: Element for which rank is required.
 */
int getRankOfNumber(NODE *root, int x) {
  NODE *tmp = root;
  int rank = 0;
  while (tmp) {
    if (tmp->data == x) {
      return rank + tmp->left_size;
    } else if (tmp->data < x) {  // Search in right sub tree.
      rank += tmp->left_size + 1;
      tmp = tmp->right;
    } else
      tmp = tmp->left;
  }
  return -1;
}

int main() {
  NODE *root = NULL;
  int num = 0;

  printf("***** Insert elements *****\n");
  while (1) {
    printf("Enter next number(0 to end): ");
    scanf("%d", &num);
    if (!num) break;
    root = track(root, num);
  }
  printf("\n\n***** Get rank of elements *****\n");
  while (1) {
    printf("Get rank of number(0 to end): ");
    scanf("%d", &num);
    if (!num) break;
    printf("Rank of %d is: %d\n", num, getRankOfNumber(root, num));
  }
  return 0;
}
