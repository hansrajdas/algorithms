/*
 * Date: 15-Nov-2017
 *
 * Description:
 * Implement AVL tree with insert and delete operations.
 * AVL tree is a balanced tree in which height of left and right sub trees is
 * not more than 1 for every node. This can be achieved by rotating the tree
 * after every insert and delete operations if not balanced.
 *
 * Complexity:
 * All operations can be done in log(n) time complexity in AVL trees.
 */

#include "stdio.h"
#include "stdlib.h"

typedef struct node {
  int key;
  struct node *left;
  struct node *right;
  int height;
}node;

int height(node *N) {
  if (N == NULL)
    return 0;
  else
    return N->height;
}

int get_balance_factor(node *N) {
  if (N == NULL)
    return 0;
  else
    return (height(N->left) - height(N->right));
}

void inorder(node *root) {
  if (root != NULL) {
    inorder(root->left);
    printf("%d[%d] ", root->key, get_balance_factor(root));
    inorder(root->right);
  }
}

node *new_node(int key) {
  node *new = (node *)malloc(sizeof(node));
  new->key = key;
  new->left = NULL;
  new->right = NULL;
  new->height = 1;
  return new;
}

int max(int a, int b) {
  return (a > b ? a : b);
}

node* right_rotate(node *y) {
  node *x = y->left;
  node *t = x->right;

  // Update pointers to perform rotation.
  x->right = y;
  y->left = t;

  x->height = max(height(x->left), height(x->right)) + 1;
  y->height = max(height(y->left), height(y->right)) + 1;

  // New root
  return x;
}

node* left_rotate(node *x) {
  node *y = x->right;
  node *t = y->left;

  y->left = x;
  x->right = t;

  x->height = max(height(x->left), height(x->right)) + 1;
  y->height = max(height(y->left), height(y->right)) + 1;

  // New root
  return y;
}

node* insert(node *root, int k) {
  int balance_factor = 0;
  if (root == NULL)
    return new_node(k);
  else if (root->key > k)
    root->left = insert(root->left, k);
  else if (root->key < k)
    root->right = insert(root->right, k);
  else {
    printf("[ERROR]: Duplicate key[%d] not allowed\n", k);
    return root;
  }

  // Update height of each node traversed while insertion.
  root->height = max(height(root->left), height(root->right)) + 1;

  // Get balance factor to this ancestor node.
  balance_factor = get_balance_factor(root);
  printf("After adding node: %d, Balance factor of node: %d is %d\n",
      k, root->key, balance_factor);

  if (balance_factor > 1) {  // Left sub-tree is heavy
    if(k < root->left->key) {  // Case 1: left-left case
      printf("Left Left Case\n");
      return right_rotate(root);  // Right rotate
    }
    else {  // Case 2: left-right case
      printf("Left Right Case\n");
      root->left = left_rotate(root->left);  // Left rotate
      return right_rotate(root);  // Right rotate
    }
  }
  else if(balance_factor < -1) {  // Right sub-tree is heavy
    if(k > root->right->key) {  // Case 3: right-right case
      printf("Right Right Case\n");
      return left_rotate(root);  // Left rotate
    }
    else {  // Case 4: right-left case
      printf("Right Left Case\n");
      root->right = right_rotate(root->right);  // Right rotate
      return left_rotate(root);  // Left rotate
    }
  }
  else
    printf("Node: %d already balanced\n", root->key);

  return root;
}

node* find_min(node *N) {
  while (N->left != NULL)
    N = N->left;
  return N;
}

node* delete(node *root, int k) {
  if (root == NULL)
    return root;
  else if (root->key > k)
    root->left = delete(root->left, k);
  else if (root->key < k)
    root->right = delete(root->right, k);
  else
  {
    if (root->left == NULL) {
      node *temp = root->right;
      free(root);
      return temp;
    }
    else if (root->right == NULL) {
      node *temp = root->left;
      free(root);
      return root;
    }
    else {
      // Find in-order successor
      node *min = find_min(root->right);
      root->key = min->key;
      root->right = delete(root->right, min->key);
    }
  }

  // After deletion if tree is empty then return
  if (root == NULL)
    return root;

  root->height = max(height(root->left), height(root->right)) + 1;

  int balance_factor = get_balance_factor(root);

  if (balance_factor > 1) {  // Left sub-tree is heavy
    if (k > root->left->key) {  // Case 1: Left Left case
      printf("Left Left Case\n");
      return right_rotate(root);  // Right rotate
    }
    else {  // Case 2: Left Right case
      printf("Left Right Case\n");
      root->left = left_rotate(root->left); // Left rotate
      return right_rotate(root);  // Right rotate
    }
  }
  else if (balance_factor < -1) {  // Right subtree is heavy
    if (k < root->right->key) {  // Case 3: Right right case
      printf("Right Right Case\n");
      return left_rotate(root); // Left rotate
    }
    else {  // Case 4: Right left case
      printf("Right Left Case\n");
      root->right = right_rotate(root->right); // Right rotate
      return left_rotate(root); // Left rotate
    }
  }
  else
    printf("Node: %d already balanced\n", root->key);
  return root;
}

void print_array(int arr[], int n, char *msg) {
  int i = 0;
  printf("*********** %s *****************\n", msg);
  for (i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n\n");
}

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  int element = 0;
  node *root = NULL;

  printf("Enter number of elements : ");
  scanf("%d",&n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element [%d] : ", i);
    scanf("%d",&a[i]);
  }
  print_array(a, n, "Inserted Array");

  // Insert in AVL and balance it.
  for (i = 0; i < n; i++)
    root = insert(root, a[i]);

  printf("***************** Inorder traversal *************\n");
  inorder(root);
  printf("\n\n");

  printf("Enter element to be deleted: ");
  scanf("%d",&element);
  root = delete(root, element);
  printf("***************** Inorder traversal *************\n");
  inorder(root);
  printf("\n\n");
  return 0;
}
