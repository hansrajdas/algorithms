/*
 * Date: 2018-07-28
 *
 * Description:
 * Find the level in tree which has maximum nodes/width.
 *
 * Approach:
 * Do a level order traversal and add all nodes below the current level in
 * queue. In each traversal pop all elements currently present in the queue so
 * that queue is left with elements that are present just below current level.
 * We can take the count of number of nodes present currently in queue and
 * compare with previous result, if smaller we can update result.
 *
 * Complexity:
 * O(n), n = number of nodes in tree.
 */

#include "stdio.h"
#include "stdlib.h"

#define MAX_Q_SIZE 100

typedef struct node {
  int data;
  struct node *left, *right;
} node;

// Allocate memory for new node and assign given value to it.
node* newNode(int d) {
  node *newNode = (node *)malloc(sizeof(node));
  newNode->data = d;
  newNode->left = NULL;
  newNode->right = NULL;
  return newNode;
}

node **createQ() {
  int i = 0;
  node **Q = (node **)malloc(sizeof(node) * MAX_Q_SIZE);
  for (; i < MAX_Q_SIZE; i++)
    Q[i] = NULL;
  return Q;
}

void enQ(node **Q, node *item, int *rear) {
  Q[*rear] = item;
  (*rear)++;
}

node *deQ(node **Q, int *front) {
  (*front) += 1;
  return Q[*front - 1];
}

/*
 * Prints tree level which has maximum nodes/width.
 * 
 * Args:
 * root: Pointer to tree root.
 */
void level_with_max_width(node *root) {
  int width = 0, count = 0, level = 0, current_level = 0;
  int front = 0, rear = 0;
  node **Q = createQ();
  node *temp = root;
  enQ(Q, root, &rear);

  // Run loop till Q is not empty.
  while (front != rear) {
    // Number of elements in Q .i.e. nodes at current_level.
    count = rear - front;
    if (count > width) {
      width = count;
      level = current_level;
    }
    // Run loop until all nodes at current_level is traversed and all nodes
    // below that level are added to queue.
    while (count--) {
      temp = deQ(Q, &front);
      if (temp->left)
        enQ(Q, temp->left, &rear);
      if (temp->right)
        enQ(Q, temp->right, &rear);
    }
    current_level++;
  }
  printf("Maximum width [%d] is at tree level [%d]\n", width, level);
}

int main() {
  // Level 0
  node *root = newNode(1);

  // Level 1
  root->left = newNode(2);
  root->right = newNode(3);

  // Level 2
  root->left->left = newNode(4);
  root->left->right = newNode(5);
  root->right->left = newNode(6);
  root->right->right = newNode(7);

  // Level 3
  root->left->left->left = newNode(8);

  level_with_max_width(root);
  return 0;
}

/*
 * Output:
 * Maximum width [4] is at tree level [2]
 */
