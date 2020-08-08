class MinHeap:
    def __init__(self):
        self.heap = []
    
    def left(self,i):
        return 2*i+1
    
    def right(self,i):
        return 2*i+2
    
    def parent(self,i):
        return int((i-1)/2)
    
    
