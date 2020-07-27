# Min Stack Implementation with Extra Space

class MinStackExtra():

    def __init__(self):
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
        return str(self.lst)
        
stack = MinStackExtra()

stack.push(18)
stack.push(19)
stack.push(29)
stack.push(15)


print(stack)
print(stack.minElement())

stack.pop()

print(stack)
print(stack.minElement())


stack.push(16)

print(stack)
print(stack.minElement())


# Min Stack Implementation in O(1) space

class MinStack