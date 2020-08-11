// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


void swap(int* x, int* y); 
  
// A class for Min Heap 
class MaxHeap { 
    int* harr; // pointer to array of elements in heap
    int capacity; // maximum possible size of min heap 
    int heap_size; // Current number of elements in min heap 
public: 
    MaxHeap(int a[], int size); // Constructor 
    void MaxHeapify(int i); // To minheapify subtree rooted with index i 
    int parent(int i) { return (i - 1) / 2; } 
    int left(int i) { return (2 * i + 1); } 
    int right(int i) { return (2 * i + 2); } 
  
    int extractMax(); // extracts root (minimum) element 
    int getMax() { return harr[0]; } // Returns minimum 
}; 
  
MaxHeap::MaxHeap(int a[], int size) 
{ 
    heap_size = size; 
    harr = a; // store address of array 
    int i = (heap_size - 1) / 2; 
    while (i >= 0) { 
        MaxHeapify(i); 
        i--; 
    } 
} 
  
// Method to remove minimum element (or root) from min heap 
int MaxHeap::extractMax() 
{ 
    if (heap_size == 0) 
        return INT_MIN; 
  
    // Store the minimum vakue. 
    int root = harr[0]; 
  
    // If there are more than 1 items, move the last item to root 
    // and call heapify. 
    if (heap_size > 1) { 
        harr[0] = harr[heap_size - 1]; 
        MaxHeapify(0); 
    } 
    heap_size--; 
  
    return root; 
} 
  
// A recursive method to heapify a subtree with root at given index 
// This method assumes that the subtrees are already heapified 
void MaxHeap::MaxHeapify(int i) 
{ 
    int l = left(i); 
    int r = right(i); 
    int largest = i; 
    if (l < heap_size && harr[l] > harr[i]) 
        largest = l; 
    if (r < heap_size && harr[r] > harr[largest]) 
        largest = r; 
    if (largest != i) { 
        swap(&harr[i], &harr[largest]); 
        MaxHeapify(largest); 
    } 
} 
  
// A utility function to swap two elements 
void swap(int* x, int* y) 
{ 
    int temp = *x; 
    *x = *y; 
    *y = temp; 
} 
  
// Function to return k'th smallest element in a given array 
int kthLargest(int arr[], int n, int k) 
{ 
    // Build a heap of n elements: O(n) time 
    MaxHeap mh(arr, n); 
  
    // Do extract min (k-1) times 
    for (int i = 0; i < k - 1; i++) 
        mh.extractMax(); 
  
    // Return root 
    return mh.getMax(); 
}