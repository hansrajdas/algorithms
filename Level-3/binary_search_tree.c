/*
 * Date: 07-Nov-2017
 *
 * Description:
 * - Insert in Binary search tree(BST)
 * - Inorder, Preorder, Postorder
 * - Search in BST
 * - Delete from BST
 *
 * Complexity:
 * Insert, search, delete - O(logn)
 * Traversal - O(n)
 *
 * Limitation:
 * If BST is not balanced (or skwed trees), it becomes a linked list and all
 * operations take O(n) complexity. This problem is handled by balancing trees.
 * AVL, Red-black, B trees are examples of balanced trees.
 */

#include "stdio.h"
#include "stdlib.h"

typedef struct node {
  int key;
  struct node *left;
  struct node *right;
}node;

void print_array(int arr[], int n, char *msg) {
  int i = 0;
  printf("*********** %s *****************\n", msg);
  for (i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n\n");
}

node* new(int k) {
  node *ptr = (node *)malloc(sizeof(node));
  ptr->key = k;
  ptr->left = NULL;
  ptr->right = NULL;
  return ptr;
}

node* insert(node *root, int k) {
  if (root == NULL)
     return new(k);
  else if (root->key > k)
    root->left = insert(root->left, k);
  else if (root->key < k)
    root->right = insert(root->right, k);
  else {
    printf("[ERROR]: Duplicate key[%d] not allowed in BST\n", k);
    return root;
  }
  return root;
}

void preorder(node *root) {
  if (root != NULL) {
    printf ("%d ", root->key);
    preorder(root->left);
    preorder(root->right);
  }
}

void inorder(node *root) {
  if (root != NULL) {
    inorder(root->left);
    printf ("%d ", root->key);
    inorder(root->right);
  }
}

void postorder(node *root) {
  if (root != NULL) {
    postorder(root->left);
    postorder(root->right);
    printf ("%d ", root->key);
  }
}

node* search(node *root, int k) {
  if (root == NULL)
     return NULL;
  else if (root->key == k)
    return root;
  else if(root->key > k)
    search(root->left, k);
  else
    search(root->right, k);
}

/*
 * Finds minimum element in the sub tree rooted with node passed.
 *
 * Args:
 *   node: Root of sub tree(whose min element is required).
 *
 * Returns: Reference to min element.
 */
node* find_min_element_in_bst(node *node) {
  while (node->left != NULL)
    node = node->left;

  return node;
}

node* delete(node *root, int key) {
  node *tmp = NULL;

  if (root == NULL)
    return root;
  else if (root->key > key)
    root->left = delete(root->left, key);
  else if (root->key < key)
    root->right = delete(root->right, key);
  else
  {
    // Node to be deleted has 1 or 0 child nodes - Copy the leaf node to
    // current node and deleted copied node.
    if (root->left == NULL) {
      tmp = root->right;
      free(root);
      return tmp;
    }
    else if (root->right == NULL) {
      tmp = root->left;
      free(root);
      return tmp;
    }
    // Node to be deleted has 2 child nodes - find in-order successor(smallest
    // element) in right sub tree and copy data of in-order successor to current
    // node and delete in-order successor.
    else {
      tmp = find_min_element_in_bst(root->right);
      root->key = tmp->key;
      root->right = delete(root->right, tmp->key);
    }
  }
}

int main() {
  int i = 0;
  int n = 0;
  int *a = NULL;
  int element = 0;
  node *root = NULL;
  node *curr_node = NULL;
  printf("Enter number of elements: ");
  scanf("%d",&n);
  a = (int *)malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    printf("Enter element [%d]: ", i);
    scanf("%d",&a[i]);
  }
  print_array(a, n, "Inserted Array");

  // Driver loop to insert in BST
  for (i = 0; i < n; i++) {
    root = insert(root, a[i]);
  }

  printf("*********** PreOrder Traversal *****************\n");
  preorder(root);
  printf("\n\n");

  printf("*********** Inorder Traversal *****************\n");
  inorder(root);
  printf("\n\n");

  printf("*********** Postorder Traversal *****************\n");
  postorder(root);
  printf("\n\n");

  // Search in a BST
  printf("Enter element to be searched in BST: ");
  scanf("%d", &element);
  curr_node = search(root, element);
  if (curr_node)
    printf("%d found in BST\n\n", element);
  else
    printf("%d not found in BST\n\n", element);

  // Delete from BST
  printf("Enter element to be deleted from BST: ");
  scanf("%d", &element);
  delete(root, element);

  printf("*********** Inorder traversal after deletion *****************\n");
  inorder(root);
  printf("\n\n");

  return 0;
}
