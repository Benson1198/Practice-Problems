# Min Stack Implementation with Extra Space

class MinStackExtra():

    def __init__(self,lst,s_lst):
        self.lst = []
        self.s_lst = []

    def push(self,data):
        self.lst.append(data)

        if len(self.s_lst) == 0:
            self.s_lst.append(data)
        elif data < self.s_lst[-1]:
            self.s_lst.append(data)
        else:
            pass
    

    def pop(self):
        temp = self.lst.pop()
        
        if temp == self.s_lst[-1]:
            self.s_lst.pop()

    
    def minElement(self):
        if len(self.lst) == 0:
            return "The stack is empty"
        else:
            return self.s_lst[-1]

    def __str__(self):
        return str(lst)


    
