/*
 * Date: 2018-01-11
 *
 * Description:
 * Level order traversal of tree.
 *
 * Approach:
 * Uses DFS traversal approach.
 * 1. Prints current node data.
 * 2. enqueue's both left and right child.
 * 3. dequeue a node from queue.
 * 4. Execute while queue is not empty.
 *
 * Reference:
 * https://www.geeksforgeeks.org/?p=2686
 *
 * Complexity:
 * O(n), n is number of node in tree. Requires extra space to maintain queue.
 */

#include "stdio.h"
#include "stdlib.h"

#define MAX_Q_SIZE 100

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

// Create and initialze an empty Q.
node** createQ(int *front, int *rear) {
  int idx = 0;
  node **Q = (node **)malloc(sizeof(node) * MAX_Q_SIZE);

  for (idx = 0; idx < MAX_Q_SIZE; idx++) {
    Q[idx] = NULL;
  }
  *front = 0;
  *rear = 0;
  return Q;
}

// Insert item at rear.
void enQ(node **Q, int *rear, node *current_node) {
  Q[*rear] = current_node;
  (*rear)++;
}

// Return item at front from the Q.
node* deQ(node **Q, int *front) {
  (*front)++;
  return Q[*front - 1];
}

// Implements a queue to perform level order traversal of tree.
void print_level_order(node *root) {
  int front = 0, rear = 0;
  node *temp_node = root;
  node **tQ = createQ(&front, &rear);

  printf("********* Level order traversal *********\n");
  while (temp_node) {
    printf("%d ", temp_node->data);

    // Check and enQ left/right child of current node to Q.
    if (temp_node->left) {
      enQ(tQ, &rear, temp_node->left);
    }
    if (temp_node->right) {
      enQ(tQ, &rear, temp_node->right);
    }

    // deQ next item from Q.
    temp_node = deQ(tQ, &front);
  }
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
