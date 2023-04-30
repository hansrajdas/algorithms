#include <stdio.h>
#include <stdlib.h>
#define N 15 // Max length of the array, could be changed...

int length(); // How much does the user want to be the length of the array
void load(int[], int); // Put some values in the array
void Print_Array(int[], int); // Print the array
void Selection_Sort_ASCENDING(int[], int); // Sort the array in ascending order
void Selection_Sort_DESCENDING(int[], int); // Sort the array in descending order

int main(){
  int arr[N], len;

  do{
    len = length();
  }while(len<=0 || len > N);

  load(arr, len);
  printf("The array before the ascending sorting:\n");
  Print_Array(arr, len);

  Selection_Sort_ASCENDING(arr, len);
  printf("\nThe array after the ascending sorting:\n");
  Print_Array(arr, len);

  Selection_Sort_DESCENDING(arr, len);
  printf("\nThe array after the descending sorting:\n");
  Print_Array(arr, len);
  return 0;
}

int length(){
  int len;

  printf("Put the size of the array: ");
  scanf("%d", &len);

  return len;
}

void load(int arr[], int len){
 for(int i = 0; i<len; i++){
   printf("#%d value: ");
   scanf("%d", &arr[i]);
 }
}

void Print_Array(int arr[], int len){
  for(int i = 0; i<len; i++){
   printf("value at the index(%d) = %d", i, arr[i]);
 }
}

void Selection_Sort_ASCENDING(int arr[], int len){
  int i, j, temp;

  for(i=0; i<len-1; i++){
    for(j=i+1; j<len; j++){
      if(arr[j]<arr[i]){
        temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
      }
    }
  }
}

void Selection_Sort_DESCENDING(int arr[], int len){
  int i, j, temp;

  for(i=0; i<len-1; i++){
    for(j=i+1; j<len; j++){
      if(arr[j]>arr[i]){
        temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
      }
    }
  }
}
