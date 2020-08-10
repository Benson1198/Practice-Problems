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
            minHeapify(self,smallest)
        
    # Extract Min: Method to extract the min. element

    def extractMin(self):
        

        


        


        