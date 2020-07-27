class Node():
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

# Simple Traversals
def inOrder(temp):
    if (not temp):
        return 
    
    inorder(temp.left)
    print(temp.data,end = ' ')
    inorder(temp.right)

def preOrder(temp):
    if (not temp):
        return 
    
    print(temp.data, end = ' ')
    preOrder(temp.left)
    preOrder(temp.right)

def postOrder(temp):
    if (not temp):
        return

    postOrder(temp.left)
    postOrder(temp.right)
    print(temp.data, end = ' ')


# Level Order Traversal

def levelOrder(temp):
    if (not temp):
        return 

    queue = []

    queue.append(temp)

    while len(queue) != 0:
        t = queue[0]
        print(t.data,end = ' ')
        queue.pop(0)

        if (not t.left):
            queue.append(t.left)
        
        if (not t.right):
            queue.append(t.right)
            