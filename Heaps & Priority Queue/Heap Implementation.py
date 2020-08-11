class MinHeap:
    def __init__(self):
        self.heap = []
    
    def left(self,i):
        return 2*i+1
    
    def right(self,i):
        return 2*i+2
    
    def parent(self,i):
        return int((i-1)/2)
    
    
    # Method to insert element in the heap
    
    def insert(self,x):
        self.heap.append(x)
        i = len(self.heap)-1

        while (i != 0 and self.heap[parent(i)] > self.heap[i]):
            self.heap[parent(i)],self.heap[i] = self.heap[i],self.heap[parent(i)]
            i = parent(i)

    # Min Heapifying method i.e. there is one given node in the heap that is 
    # violating the heap rules & we have to min heapify the heap
        
    def minHeapify(self,i):
        n = len(self.heap)

        lt = left(i)
        rt = right(i)
        smallest = i

        if (lt < n) and (self.heap[lt] < self.heap[i]):
            smallest = lt
        
        if (rt < n) and (self.heap[rt] < self.heap[i]):
            smallest = rt
        
        if smallest != i:
            self.heap[i],self.heap[smallest] = self.heap[smallest],self.heap[i]
            self.minHeapify(self,smallest)
        
    # Extract Min: Method to extract the min. element

    def extractMin(self):
        n = len(self.heap)

        if n == 0:
            return "Heap is Empty"
        
        if n == 1:
            return self.heap[0]

        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]

        temp = self.heap.pop()

        self.minHeapify(0)

        return temp
    
    #  Method to decrese a given key
    
    def decreaseKey(self,i,k):
        self.heap[i] = k

        while i!= 0 and self.heap[parent(i)] > self.heap[i]:
            self.heap[parent(i)],self.heap[i] = self.heap[i],self.heap[parent(i)]
            i = parent(i)


    # Method to delete a key

    def deleteKey(self,i):
        
        self.decreaseKey(i,float('-inf'))

        self.extractMin()

# Function to buil a min meap out of an unordered array(Heap sort)

def left(i):
    return 2*i+1
    
def right(i):
    return 2*i+2
    
def parent(i):
    return int((i-1)/2)

def minHeapify(heap,i):
    n = len(heap)

    lt = left(i)
    rt = right(i)
    smallest = i

    if (lt < n) and (heap[lt] < heap[i]):
        smallest = lt
        
    if (rt < n) and (heap[rt] < heap[i]):
        smallest = rt
        
    if smallest != i:
        heap[i],heap[smallest] = heap[smallest],heap[i]
        minHeapify(heap,smallest)

def buildHeap(arr):
    '''
    Basic idea is to call minHeapify function first for bottom-most rightmost internal
    node and then go on till index zero.
    '''
    brn = parent(len(arr)-1)

    for i in range(brn,-1,-1):
        minHeapify(arr,i)
