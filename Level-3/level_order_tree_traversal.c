#include "stdio.h"
#include "stdlib.h"

/*
 * Date: 2018-01-07
 *
 * Implementation:
 * Find height of tree and traverse recursively printing left and right node
 * for each level starting from top(level 1).
 *
 * Complexity:
 * Worst case would be O(n^2), in case of skewed tree.
 *
 * Refer: Level-2/level_order_tree_traversal_using_queue.c
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

// Return height of tree with given root.
int height(node *root) {
  if (NULL == root) {
    return 0;
  } else {
    int tright = height(root->right);
    int tleft = height(root->left);

    if (tright > tleft) {
      return (tright + 1);
    } else {
      return (tleft + 1);
    }
  }
}

// Prints all elements at a given level in tree.
void print_given_level(node* root, int level) {
  if (NULL == root) {
    return;
  }
  if (1 == level) {
    printf("%d ", root->data);
  } else {
    print_given_level(root->left, level - 1);
    print_given_level(root->right, level - 1);
  }
}

// Iterates over height over tree and prints all elements level by level.
void print_level_order(node *root) {
  int idx = 0;
  int h = height(root);
  printf("height is: %d\n", h);
  printf("********* Level order traversal *********\n");
  for (idx = 1; idx <= h; idx++) {
    print_given_level(root, idx);
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
 * height is: 4
 * ********* Level order traversal *********
 * 1 2 3 4 5 6 
 * 
 */
