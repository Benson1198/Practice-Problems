class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        if len(self.s) == 0:
            self.s.append(x)
        else:
            self.s.append(x)
            

    def pop(self):
        if len(self.s) is not 0:
            return self.s.pop()
        else:
            return -1
        

    def getMin(self):
        if len(self.s) is not 0:
            return min(self.s)
        else:
            return -1