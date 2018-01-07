#include "stdio.h"
#include "stdlib.h"

/*
 * Date: 2017-01-07
 *
 * Implementation: Uses DFS graph traversal approach.
 * 1. Prints current node data.
 * 2. enqueue's both left and right child.
 * 3. dequeue a node from queue.
 * 4. Execute while queue is not empty.
 *
 * Complexity: O(n), n is number of node in tree.
 */

typedef struct node {
  int data;
  struct node *left, *right;
} node;

// Allocate memory for new node and assign given value to it.
node* new_node(int d) {
  node *new_node = (node *)malloc(sizeof(node));
  new_node->data = d;
  new_node->left = NULL;
  new_node->right = NULL;
  return new_node;
}

// Implements a queue to perform level order traversal of tree.
void print_level_order(node *root) {
  printf("********* Level order traversal *********\n");
  printf("\n");
}

int main() {
  node *root = new_node(1);
  root->left = new_node(2);
  root->right = new_node(3);

  root->left->left = new_node(4);
  root->left->right = new_node(5);

  root->left->left->left = new_node(6);

  print_level_order(root);
  return 0;
}

/*
 * Output:
 * ********* Level order traversal *********
 * 1 2 3 4 5 6 
 */
